import cv2 as cv
import sys
import requests
import time
import threading
from threading import Thread
from queue import Queue
from datetime import datetime
from pathlib import Path
from config import W, H, FPS, urlapi, CORAL_DATA_DIR, img_format

class request_api (threading.Thread):

    def __init__(self, frame, framename, threadID, t_Lock):
        threading.Thread.__init__(self, daemon=True)    
        self.frame = frame
        self.framename = framename
        self.threadID = threadID
        self.t_Lock = t_Lock
        self.start()
      
    def run (self):
        
        with self.t_Lock: 

            # self.t_Lock.acquire()
             
            print('Initialize thread -{thread_id} at {time} ' .format(thread_id =self.threadID, time= time.ctime()))
            
            self.imencoded = cv.imencode('.PNG', self.frame)[1].tobytes()

            self.session = requests.Session()
                    
            try:
                                       
                self.response = self.session.post(url= urlapi +'/'+ self.framename, data=self.imencoded)            

                cv.imwrite(str(CORAL_DATA_DIR) +'/'+ self.framename + img_format, self.frame)
                with open(str(CORAL_DATA_DIR) +'/'+ self.framename + '.xml', 'wb') as f:
                    f.write(self.response.content)
                print('Thread - {thread_id}  Saved Frame & Anotation at {time} ' .format(thread_id =self.threadID, time= time.ctime()))
                           
            except :
                # self.response = requests.exceptions.RequestException
                cv.imwrite(str(CORAL_DATA_DIR) +'/'+ self.framename + img_format, self.frame)
                print('Thread - {thread_id} Only  Saved Frame and Anotation Not Found at {time} ' .format(thread_id =self.threadID, time= time.ctime()))
            
            print('Exiting thread - {thread_id} at {time} ' .format(thread_id =self.threadID, time= time.ctime()))
            
            self.session.close()            
