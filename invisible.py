"""
INVISIBLE CLOAK PROJECT (Lime Green Color Cloaking)
Developed by: Mayush Sharma
When the webcam detects LIME GREEN color,
that region becomes INVISIBLE (shows background).
"""

import cv2
import numpy as np
import time

# Start webcam
cap = cv2.VideoCapture(0)

# Allow camera to warm up
time.sleep(2)
background = None

print("Capturing background... ")
for i in range(60):
    ret, background = cap.read()
background = np.flip(background, axis=1)  # Flip for natural view

print("Background captured. Cloak activated!")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = np.flip(frame, axis=1)

    # Convert to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # -----------------------
    # Detect LIME GREEN color range
    # -----------------------
    lower_lime = np.array([25, 52, 72])
    upper_lime = np.array([102, 255, 255])

    lime_mask = cv2.inRange(hsv, lower_lime, upper_lime)

    # Clean the mask
    lime_mask = cv2.morphologyEx(lime_mask, cv2.MORPH_OPEN, np.ones((3,3), np.uint8))
    lime_mask = cv2.morphologyEx(lime_mask, cv2.MORPH_DILATE, np.ones((3,3), np.uint8))

    # Invert mask
    mask_inv = cv2.bitwise_not(lime_mask)

    # Part without lime green
    visible_part = cv2.bitwise_and(frame, frame, mask=mask_inv)

    # Part where lime is detected → replace with background
    invisible_part = cv2.bitwise_and(background, background, mask=lime_mask)

    # Final output
    final_output = visible_part + invisible_part

    cv2.imshow("Invisible Cloak (LIME GREEN Color)", final_output)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()