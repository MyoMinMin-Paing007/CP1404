import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np
import cv2
import tempfile
import os
from datetime import datetime

# ------------------------------
# APP CONFIG
# ------------------------------
st.set_page_config(page_title="Seat Occupancy • MVP", layout="wide")
st.title("Seat Occupancy • MVP")

# ------------------------------
# MODEL LOADING (cached)
# ------------------------------
@st.cache_resource
def load_model():
    # Use small, fast model for demo. Replace with your trained 'best.pt' later.
    return YOLO("yolov8n.pt")

model = load_model()

# ------------------------------
# SIDEBAR CONTROLS
# ------------------------------
st.sidebar.header("Settings")
total_seats = st.sidebar.number_input("Total seats in room", min_value=1, max_value=500, value=40, step=1)
conf_thresh = st.sidebar.slider("Confidence threshold", 0.1, 0.9, 0.35, 0.05)
iou_thresh = st.sidebar.slider("IoU threshold (NMS)", 0.1, 0.9, 0.45, 0.05)

# ------------------------------
# UPLOAD IMAGE
# ------------------------------
uploaded_file = st.file_uploader("Upload classroom image", type=["jpg", "jpeg", "png"])

col1, col2 = st.columns(2, gap="large")

if uploaded_file:
    # Read image with PIL and show preview
    pil_img = Image.open(uploaded_file).convert("RGB")
    col1.image(pil_img, caption="Original image", use_container_width=True)

    # Run detection
    if st.button("Run detection", type="primary"):
        with st.spinner("Running YOLO detection..."):
            # Save to temp for Ultralytics predict()
            with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp:
                pil_img.save(tmp.name)
                tmp_path = tmp.name

            # Inference
            results = model.predict(
                source=tmp_path,
                conf=conf_thresh,
                iou=iou_thresh,
                verbose=False
            )

            # Expect one image result for single upload
            result = results[0]

            # Count 'person' class only (COCO class id/name is 'person')
            # Ultralytics v8 stores boxes and class names in model.names
            names = model.names
            boxes = result.boxes
            cls_ids = boxes.cls.cpu().numpy().astype(int) if boxes is not None else np.array([])
            person_label_ids = [k for k, v in names.items() if v == "person"]
            person_count = int(np.sum(np.isin(cls_ids, person_label_ids))) if len(person_label_ids) > 0 else 0

            occupied = person_count
            empty = max(total_seats - occupied, 0)
            usage_pct = (occupied / total_seats) * 100 if total_seats > 0 else 0.0

            # Render annotated image
            annotated = result.plot()  # numpy array (BGR)
            annotated_rgb = cv2.cvtColor(annotated, cv2.COLOR_BGR2RGB)

            # Show results
            col2.image(annotated_rgb, caption="Detections (persons)", use_container_width=True)

            # Metrics row
            m1, m2, m3 = st.columns(3)
            m1.metric("Occupied", occupied)
            m2.metric("Empty", empty)
            m3.metric("Usage", f"{usage_pct:.1f}%")

            # Save outputs for download
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            out_img_path = f"output_{timestamp}.jpg"
            Image.fromarray(annotated_rgb).save(out_img_path)

            # Simple CSV summary
            csv_path = f"summary_{timestamp}.csv"
            with open(csv_path, "w") as f:
                f.write("total_seats,occupied,empty,usage_percent\n")
                f.write(f"{total_seats},{occupied},{empty},{usage_pct:.2f}\n")

            st.download_button("Download annotated image", data=open(out_img_path, "rb"), file_name=out_img_path, mime="image/jpeg")
            st.download_button("Download CSV summary", data=open(csv_path, "rb"), file_name=csv_path, mime="text/csv")

            # Clean temp
            try:
                os.remove(tmp_path)
            except Exception:
                pass

else:
    st.info("Upload a classroom image (JPG/PNG) to start.")
