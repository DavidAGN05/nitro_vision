"""
Using the NanoCamera with RTSP Source Cameras
@author: Ayo Ayibiowu

"""

import cv2

cap = cv2.VideoCapture("rtsp://192.168.1.34:8554/stream", cv2.CAP_FFMPEG)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to read frame")
        continue
    
    # Display the live video feed
    cv2.imshow("RTSP Stream", frame)
    
    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

