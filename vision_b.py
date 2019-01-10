import cv2
import numpy as np
vid = cv2.VideoCapture(0)
vid.set(10,.05)

while(True):
    ret, frame = vid.read()
    cv2.imread
    lower_green = np.array([40,20,20])
    upper_green = np.array([70,255,255])
    mask = cv2.inRange(hsv, lower_green, upper_green)
    res = cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow('orig',frame)
    cv2.imshow('fff',res)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
vid.release()
cv2.destroyAllWindows()