import cv2
import numpy as np
import sys
from time import sleep
from matplotlib import pyplot as plt

def nothing(x):pass

cv2.namedWindow("trackbars")
cv2.createTrackbar("blursize", "trackbars", 1, 10, nothing)
cv2.createTrackbar("canny", "trackbars", 0, 1, nothing)

m1 = -(cos(theta1)/sin(theta1))
m2 = -(cos(theta2)/sin(theta2))
b1 = r1/sin(theta1)
b2 = r2/sin(theta2)

x = ((b2-b1)/(m1-m2))
y = ((m1*(b2-b1))/(m1-m2))+b1

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
			#go through for loop and find thetas then average them out
			numoflines = 3
			totheta = 0
			for count, line in enumerate(lines):
				if count > numoflines:
					break

				for rho,theta in line:
					totheta += theta
			avgtheta = totheta / max(numoflines, count)
			lc = 0
			totheta2 = 0
			ang90 = avgtheta + np.pi/2
			tol = 15 * (np.pi / 180)
			for count, line in enumerate(lines):
				for rho,theta in line:
					if abs(theta - ang90) < tol:
						totheta2 += theta
						lc += 1
			print(theta)
			if lc != 0:
				avgtheta2 = totheta2/lc
				print(f"Theta 1: {avgtheta * (180 / np.pi)}")
				print(f"Theta 2: {avgtheta2 * (180 / np.pi)}")
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
		corner1 = (line1 == line2)
		corner2 = (line3 == line2)
		cv2.imshow('image', frame)

		if cv2.waitKey(25) & 0xFF == ord('q'):
			break
	else:
		break
plt.show()
camera.release()