import cv2
import numpy as np
from time import sleep

def nothing(x):pass

camera = cv2.VideoCapture(1)
cv2.namedWindow('videoUI', cv2.WINDOW_NORMAL)
cv2.createTrackbar('T', 'videoUI', 0, 255, nothing)
while True:
	(grabbed, frame) = camera.read()
	frame = cv2.resize(frame, (640, 480))
	frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	thresh = cv2.getTrackbarPos('T', 'videoUI');
	frame = cv2.threshold(frame, thresh, 255, cv2.THRESH_BINARY)[1]
	cv2.imshow('image', frame)
	cv2.waitKey(1)
