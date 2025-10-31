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
# MODEL LOADING
# ------------------------------
@st.cache_resource
def load_model():
    return YOLO("yolov8n.pt")  # small, fast COCO-pretrained model

model = load_model()

# ------------------------------
# SIDEBAR SETTINGS
# ------------------------------
st.sidebar.header("Settings")
conf_thresh = st.sidebar.slider("Confidence threshold", 0.1, 0.9, 0.35, 0.05)
iou_thresh = st.sidebar.slider("IoU threshold (NMS)", 0.1, 0.9, 0.45, 0.05)

# ------------------------------
# IMAGE UPLOAD
# ------------------------------
uploaded_file = st.file_uploader("Upload classroom image", type=["jpg", "jpeg", "png"])

col1, col2 = st.columns(2, gap="large")

if uploaded_file:
    pil_img = Image.open(uploaded_file).convert("RGB")
    col1.image(pil_img, caption="Original image", use_container_width=True)

    if st.button("Run detection", type="primary"):
        with st.spinner("Running YOLO detection..."):

            # Save temp image
            with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp:
                pil_img.save(tmp.name)
                tmp_path = tmp.name

            # Run YOLO on person (0) + chair (56)
            results = model.predict(
                source=tmp_path,
                conf=conf_thresh,
                iou=iou_thresh,
                classes=[0, 56],  # detect only person and chair
                verbose=False
            )

            result = results[0]
            names = model.names
            boxes = result.boxes
            cls_ids = boxes.cls.cpu().numpy().astype(int) if boxes is not None else np.array([])

            # Separate chair and person boxes
            chairs = []
            people = []
            for box, cid in zip(boxes.xyxy.cpu().numpy().astype(int), cls_ids):
                if names[cid] == "chair":
                    chairs.append(box)
                elif names[cid] == "person":
                    people.append(box)

            # ------------------------------
            # Helper function: IoU
            # ------------------------------
            def iou(boxA, boxB):
                xA = max(boxA[0], boxB[0])
                yA = max(boxA[1], boxB[1])
                xB = min(boxA[2], boxB[2])
                yB = min(boxA[3], boxB[3])
                inter = max(0, xB - xA) * max(0, yB - yA)
                if inter == 0:
                    return 0.0
                boxA_area = (boxA[2] - boxA[0]) * (boxA[3] - boxA[1])
                boxB_area = (boxB[2] - boxB[0]) * (boxB[3] - boxB[1])
                return inter / float(boxA_area + boxB_area - inter)

            # ------------------------------
            # Draw results manually
            # ------------------------------
            annotated_rgb = np.array(pil_img)
            occupied = 0

            for chair in chairs:
                taken = False
                for person in people:
                    if iou(chair, person) > 0.2:  # overlap threshold
                        taken = True
                        break
                color = (255, 0, 0) if taken else (0, 255, 0)  # red or green
                cv2.rectangle(annotated_rgb, (chair[0], chair[1]), (chair[2], chair[3]), color, 3)
                if taken:
                    occupied += 1

            empty = len(chairs) - occupied
            usage_pct = (occupied / len(chairs)) * 100 if len(chairs) > 0 else 0.0

            # ------------------------------
            # DISPLAY OUTPUT
            # ------------------------------
            col2.image(annotated_rgb, caption="Red = Occupied | Green = Empty", use_container_width=True)

            m1, m2, m3 = st.columns(3)
            m1.metric("Occupied", occupied)
            m2.metric("Empty", empty)
            m3.metric("Usage", f"{usage_pct:.1f}%")

            # Save output for download
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            out_img_path = f"output_{timestamp}.jpg"
            Image.fromarray(annotated_rgb).save(out_img_path)

            st.download_button(
                "Download annotated image",
                data=open(out_img_path, "rb"),
                file_name=out_img_path,
                mime="image/jpeg"
            )

            try:
                os.remove(tmp_path)
            except Exception:
                pass

else:
    st.info("Upload a classroom image (JPG/PNG) to start detection.")
