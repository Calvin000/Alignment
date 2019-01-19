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

	blursize = cv2.getTrackbarPos("blursize", "trackbars")*2 + 1

	if grabbed == True:
		gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

		ret, thr = cv2.threshold(gray_frame, 0, 255, cv2.THRESH_OTSU)
		cv2.imshow('threshold', thr)

		blurred = cv2.GaussianBlur(gray_frame, (blursize, blursize), 0)
		cv2.imshow('blur', blurred)
		edges = cv2.Canny(blurred,50,150,apertureSize = 3)
		cv2.imshow('edges', edges)
		lines = cv2.HoughLines(edges,1,np.pi/180,20)
		if lines is not None:
			#go through for lop and find thetas then average them out
			numoflines = 3
			totheta = 0

			for count, line in enumerate(lines):
				if count > numoflines:
					break

				for rho,theta in line:
					totheta += theta 
			totheta2 = 0
			lc = 0
			ang90 = theta-.15np.pi
			for count, line in enumerate(lines):
				for rho,theta in line:
					
			
			for count, line in enumerate(lines):
				if count > 10:
					break

				for rho,theta in line:
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

		if cv2.waitKey(25) & 0xFF == ord('q'):
			break
	else:
		break
plt.show()
camera.release()