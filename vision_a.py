import cv2
import numpy as np
import sys
from time import sleep
from matplotlib import pyplot as plt

def nothing(x):pass

camera = cv2.VideoCapture(sys.argv[1])
while (camera.isOpened()):
	(grabbed, frame) = camera.read()
	if grabbed == True:
		cv2.imshow('image', frame)
		gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
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