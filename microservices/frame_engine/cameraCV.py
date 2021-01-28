import cv2 as cv
import sys
import requests
import time
import threading
from datetime import datetime
from pathlib import Path
from config import data_test_directory
from frame_stream import VideoStream
    
if __name__ == '__main__':

    start_time = time.time()
    
    VideoStream(src = str(data_test_directory) + '/test_video.mp4')
    
    print("Time take to process {:.2f}s" .format(time.time() - start_time))

    cv.destroyAllWindows()
