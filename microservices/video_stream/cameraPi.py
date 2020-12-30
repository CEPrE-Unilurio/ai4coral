import time
import picamera
import numpy as np
import cv2

with picamera.PiCamera() as camera:
    camera.resolution = (640, 640)
    camera.framerate = 30
    time.sleep(2)
    image = np.empty((640 * 640 * 3,), dtype=np.uint8)
    camera.capture(image, 'bgr')
    image = image.reshape((640, 640, 3))