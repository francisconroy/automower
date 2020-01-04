import cv2 as cv2

import time

import numpy as np

url = "rtsp://192.168.1.23:8080/h264_ulaw.sdp"

vcap = cv2.VideoCapture(url)

result, frame = vcap.read()

while(True):
    # Capture frame-by-frame
    ret, frame = vcap.read()
    #print cap.isOpened(), ret
    if frame is not None:
        # Display the resulting frame
        cv2.imshow('frame', frame)
        # Press q to close the video windows before it ends if you want
        if cv2.waitKey(22) & 0xFF == ord('q'):
            break
    else:
        print("Frame is None")
        break