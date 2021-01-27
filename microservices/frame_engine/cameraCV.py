import cv2 as cv
import sys
import requests
import time
import threading
from datetime import datetime
from pathlib import Path
from requests import ReadTimeout, ConnectTimeout, HTTPError, Timeout, ConnectionError
from config import W, H, FPS, urlapi, CORAL_DATA_DIR, img_format
from frame_stream import VideoStream
    
if __name__ == '__main__':

    thread_list = []
    
    start_time = time.time()
    
    VideoStream(src = 'test_video.mp4')
    
    print("Time take to process {:.2f}s" .format(time.time() - start_time))

cv.destroyAllWindows()
