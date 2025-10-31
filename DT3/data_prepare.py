# SmartSeat ML Data Preparation Script
# Sprint 1 - Data collection and setup

import os
import cv2

DATA_DIR = "data_set"
CATEGORIES = ["occupied", "empty"]

def check_dataset():
    for category in CATEGORIES:
        path = os.path.join(DATA_DIR, category)
        print(f"{category.upper()} - {len(os.listdir(path))} images found")

if __name__ == "__main__":
    print("SmartSeat ML Data Check")
    check_data_set()
# SmartSeat ML - Generate Sample Dataset
# Creates simple colored images for testing

import cv2
import numpy as np
import os

DATASET_PATH = "data_set"
CATEGORIES = ["occupied", "empty"]


def create_sample_images():
    os.makedirs(DATASET_PATH, exist_ok=True)
    for category in CATEGORIES:
        folder_path = os.path.join(DATASET_PATH, category)
        os.makedirs(folder_path, exist_ok=True)

        for i in range(5):
            # make random colored image
            img = np.zeros((100, 100, 3), dtype=np.uint8)
            color = (0, 255, 0) if category == "empty" else (0, 0, 255)
            img[:] = color

            cv2.putText(img, category, (5, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
            filename = os.path.join(folder_path, f"{category}_{i + 1}.jpg")
            cv2.imwrite(filename, img)
            print(f"✅ Created {filename}")


if __name__ == "__main__":
    create_sample_images()
