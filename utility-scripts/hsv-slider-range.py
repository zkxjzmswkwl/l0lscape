import cv2
import numpy as np

img = cv2.imread('to_read.png')

def cb(x):
    pass

cv2.namedWindow('image')
cv2.createTrackbar('lowH', 'image', 0, 179, cb)
cv2.createTrackbar('highH', 'image', 0, 179, cb)
cv2.createTrackbar('lowS', 'image', 0, 255, cb)
cv2.createTrackbar('highS', 'image', 0, 255, cb)
cv2.createTrackbar('lowV', 'image', 0, 255, cb)
cv2.createTrackbar('highV', 'image', 0, 255, cb)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

while True:
    low_h = cv2.getTrackbarPos('lowH', 'image')
    high_h = cv2.getTrackbarPos('highH', 'image')
    low_s = cv2.getTrackbarPos('lowS', 'image')
    high_s = cv2.getTrackbarPos('highS', 'image')
    low_v = cv2.getTrackbarPos('lowV', 'image')
    high_v = cv2.getTrackbarPos('highV', 'image')

    lower_hsv = np.array([low_h, low_s, low_v])
    upper_hsv = np.array([high_h, high_s, high_v])
    mask = cv2.inRange(hsv, lower_hsv, upper_hsv)

    res = cv2.bitwise_and(img, img, mask=mask)

    cv2.imshow('image', res)
    k = cv2.waitKey(1000) & 0xFF
    if k == 27:
        break

