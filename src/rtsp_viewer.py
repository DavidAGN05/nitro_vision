"""
Using the NanoCamera with RTSP Source Cameras
@author: Ayo Ayibiowu

"""

import cv2

cap = cv2.VideoCapture("rtsp://192.168.1.34:8554/stream", cv2.CAP_FFMPEG)
frame_count = 0
while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to read frame")
        continue
    # Save every 10th frame as an image
    if frame_count % 10 == 0:
        cv2.imwrite(f"frame_{frame_count}.jpg", frame)
    frame_count += 1
    # Add a break condition if needed
cap.release()

