# Coordinates of each seat bounding box (x1, y1, x2, y2)
seat_coords = [(50, 60, 120, 150), (200, 60, 270, 150), (350, 60, 420, 150)]
occupied = [True, False, True]

import cv2
import numpy as np

img = cv2.imread('classroom.jpg')
seat_coords = [(50, 60, 120, 150), (200, 60, 270, 150), (350, 60, 420, 150)]
occupied = [True, False, True]  # Replace with results from model

for (seat, occ) in zip(seat_coords, occupied):
    color = (0, 0, 255) if occ else (0, 255, 0)
    cv2.rectangle(img, (seat[0], seat[1]), (seat[2], seat[3]), color, 2)
    label = 'Occupied' if occ else 'Empty'
    cv2.putText(img, label, (seat[0], seat[1]-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

cv2.imwrite('seat_map_demo.jpg', img)
