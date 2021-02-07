import cv2 as cv
import sys
import requests
import time
import numpy as np
import psutil
import threading
from threading import Thread
from queue import  Queue
from datetime import datetime
from pathlib import Path
from fe.config import W, H, FPS, urlapi, CORAL_DATA_DIR, img_format, num_thread
from fe.thread_request import Request_api as request_api

class VideoStream():
    """ 
    The VideoStream class is responsible for grap frame for a given source (camara or video file).

        args:
            src(int, path): is a path to video source, it can be
                (int): the id of any camara atached or
                (path): the path to a video file
            show_frame(bool): defin either the frame is shown or not.
            save_frame(bool) : defin if the frame should be saved in disk or not.
        
        
        Attributes:
            capture(obj):
            num_fps(int): number of the frame graped
            t_Lock(:obj: int): the semaphore to control the number of threa opened
            thread_list(list): the lista of all thread created
            thread_id(int): the id of a given thread
            show_frame(bool): defin either the frame is shown or not.
            save_frame(bool) : defin if the frame should be saved in disk or not.
        
        """
    def __init__(self, src=0, show_frame = True, save_frame =True):
        
        self.capture = cv.VideoCapture(src)
        self.capture.set(cv.CAP_PROP_FRAME_WIDTH,W) # set Width
        self.capture.set(cv.CAP_PROP_FRAME_HEIGHT,H) # set Height
        self.num_fps = 0
        self.t_lock = threading.Semaphore(num_thread)
        self.thread_list = []
        self.thread_id = 0
        self.show_frame = show_frame
        self.save_frame = save_frame
        self.start_time = time.time()  
        self.frame_grab()
              
    def frame_grab(self):

        # Time wich last frame processed 
        self.prev_time = 0        

        while (self.capture.isOpened()):
            self.actual_time = 0
            (self.status, self.frame) = self.capture.read()          

            if self.num_fps == self.capture.get(cv.CAP_PROP_FRAME_COUNT):
                self.num_fps=0
                self.capture.set(cv.CAP_PROP_POS_FRAMES, 0)
            
            if self.status == True:
                self.num_fps +=1
                self.frame = cv.resize(self.frame, (W, H), interpolation = cv.INTER_AREA)
                                
                now = datetime.now()
                timestamp = datetime.timestamp(now)
                # Launch Thread for each frame
                self.thread_id +=1
                thread = request_api(self.frame, str(timestamp), self.thread_id, self.t_lock, self.save_frame)
                # self.thread_list.append(thread)
                thread.join()
                
                # time when we finish processing for this frame 
                self.atual_time = time.time() 
                fps = 1/(self.atual_time-self.prev_time) 
                self.prev_time = self.atual_time                 
                fps = "FPS : %0.1f" % fps
                
                if self.show_frame:

                    # puting the FPS count on the frame
                    cv.putText(self.frame, fps, (0, 100), cv.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 3) 
                    cv.imshow('frame', self.frame)
                    
                k = cv.waitKey(30) & 0xFF
                if k == 27: # press 'ESC' to quit
                    self.exit()      
                    break  
    def exit(self):
        self.capture.release() 
        # Wait to all thread complete
        # for thread in self.thread_list:
            # thread.join()
        print('The program process {num_fps} frame in {time:.2f}s ' .format(num_fps=self.num_fps, time=time.time() - self.start_time))
        cv.destroyAllWindows()

