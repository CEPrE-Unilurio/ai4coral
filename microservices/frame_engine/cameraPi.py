import time
import picamera
import numpy as np
import cv2

from config import *

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
rawCapture = PiRGBArray(camera)
# allow the camera to warmup
time.sleep(0.1)
# grab an image from the camera
camera.capture(rawCapture, format="bgr")
image = rawCapture.array
# display the image on screen and wait for a keypress
cv2.imshow("Image", image)
cv2.waitKey(0)

# with picamera.PiCamera() as camera:
#     camera.resolution = (640, 640)
#     camera.framerate = 30
#     time.sleep(2)
#     image = np.empty((640 * 640 * 3,), dtype=np.uint8)
#     camera.capture(image, 'bgr')
#     image = image.reshape((640, 640, 3))