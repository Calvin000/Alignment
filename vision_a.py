import cv2
import numpy as np
import sys
from time import sleep
from matplotlib import pyplot as plt

def nothing(x):pass

cv2.namedWindow("trackbars")
cv2.createTrackbar("blursize", "trackbars", 1, 10, nothing)
cv2.createTrackbar("canny", "trackbars", 0, 1, nothing)

camera = cv2.VideoCapture(sys.argv[1])
while (camera.isOpened()):
	(grabbed, frame) = camera.read()

	test = cv2.getTrackbarPos("test", "frame")

	if grabbed == True:
		gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

		ret, thr = cv2.threshold(gray_frame, 0, 255, cv2.THRESH_OTSU)
		cv2.imshow('threshold', thr)





		blurred = cv2.GaussianBlur(gray_frame, (3, 3), 0)
		edges = cv2.Canny(blurred,50,150,apertureSize = 3)
		cv2.imshow('edges', edges)
		lines = cv2.HoughLines(edges,1,np.pi/180,200)
		for rho,theta in lines[0]:
			a = np.cos(theta)
			b = np.sin(theta)
			x0 = a*rho
			y0 = b*rho
			x1 = int(x0 + 1000*(-b))
			y1 = int(y0 + 1000*(a))
			x2 = int(x0 - 1000*(-b))
			y2 = int(y0 - 1000*(a))
			cv2.line(frame,(x1,y1),(x2,y2),(0,0,255),2)
		
		cv2.imshow('image', frame)

		hist = cv2.calcHist([gray_frame],[0],None,[256],[0,256])
		hist,bins = np.histogram(gray_frame.ravel(),256,[0,256])
		plt.hist(gray_frame.ravel(),256,[0,256])
		plt.pause(0.05)
		if cv2.waitKey(25) & 0xFF == ord('q'):
			break
	else:
		break
plt.show()
camera.release()