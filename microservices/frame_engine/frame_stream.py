import cv2 as cv
import sys
import requests
import time
import numpy as np
import threading
from threading import Thread
from queue import  Queue
from datetime import datetime
from pathlib import Path
from config import W, H, FPS, urlapi, CORAL_DATA_DIR, img_format
from thread_request import request_api

class VideoStream():

    def __init__(self, src=0):
        self.capture =cv.VideoCapture(src)
        self.capture.set(cv.CAP_PROP_FRAME_WIDTH,W) # set Width
        self.capture.set(cv.CAP_PROP_FRAME_HEIGHT,H) # set Height
        self.num_fps = 0
        self.t_lock = threading.Lock()
        self.thread_list = []
        self.thread_id =1
        self.framegrab()        

    def framegrab(self):        
        # Time wich last frame processed 
        self.prev_time = 0
        # Current frame 
        self.actual_time = 0

        while (self.capture.isOpened()):
            (self.status, self.frame) = self.capture.read()
            self.num_fps +=1

            if self.num_fps == self.capture.get(cv.CAP_PROP_FRAME_COUNT):
                self.num_fps=0
                self.capture.set(cv.CAP_PROP_POS_FRAMES, 0)
            
            if self.status == True:
                self.frame = cv.resize(self.frame, (W, H), interpolation = cv.INTER_AREA)
                
                # time when we finish processing for this frame 
                self.atual_time = time.time() 
                fps = 1/(self.atual_time-self.prev_time) 
                self.prev_time = self.atual_time 
            
                fps = "FPS : %0.1f" % fps
            
                # puting the FPS count on the frame
                cv.putText(self.frame, fps, (0, 100), cv.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 3) 
                cv.imshow('frame', self.frame)

                now = datetime.now()
                timestamp = datetime.timestamp(now)
                # Launch Thread for each frame
                self.thread_id +=1
                thread = request_api(self.frame, str(timestamp), self.thread_id, self.t_lock)
                self.thread_list.append(thread)
                                
                k = cv.waitKey(30) & 0xff
                if k == 27: # press 'ESC' to quit
                    self.exit()      
                    break  
    def exit(self):
        self.capture.release() 
        # Wait to all thread complete
        for thread in self.thread_list:
            thread.join()
