import cv2 as cv
import sys
import requests
import time
import threading
from threading import Thread
from queue import Queue
from datetime import datetime
from pathlib import Path
from fe.settings import common as config

class Request_api (threading.Thread):
    """ 
        The request_ api class is responsible for create thread for each graped frame.

        args:
            frame(obj): a byte of image
            framename(str): a timestanp used to named the frame
            thread_id(int): the id of a given thread
            t_Lock(:obj: int): the semaphore to control the number of threa opened
            save_frame(bool) : defin if the frame should be saved in disk or not.       
        
        Attributes:
            frame(obj): a byte of image
            framename(str): a timestanp used to named the frame
            t_Lock(:obj: int): the semaphore to control the number of threa opened
            thread_id(int): the id of a given thread
            save_frame(bool) : defin if the frame should be saved in disk or not.
        
        Return:
            None
    """

    def __init__(self, frame, framename, threadID, t_Lock, save_frame):
        threading.Thread.__init__(self, daemon=False)    
        self.frame = frame
        self.framename = framename
        self.threadID = threadID
        self.t_Lock = t_Lock
        self.save_frame = save_frame
        self.start()
      
    def run (self):
        
        with self.t_Lock: 

            print('Initialize thread -{thread_id} at {time} ' .format(thread_id =self.threadID, time= time.asctime()))
            
            self.imencoded = cv.imencode(config.IMG_FORMAT, self.frame)[1].tobytes()

            self.session = requests.Session()
                    
            try:
                                       
                self.response = self.session.post(url= config.URL_API +'/'+ self.framename, data=self.imencoded)
                
                print(self.response.status_code)            

                if self.save_frame:
                    cv.imwrite(str(config.CORAL_DATA_DIR) +'/'+ self.framename + config.IMG_FORMAT, self.frame)
                    with open(str(config.CORAL_DATA_DIR) +'/'+ self.framename + '.xml', 'wb') as f:
                        f.write(self.response.content)
                    print('Thread - {thread_id}  Saved Frame & Anotation at {time} ' .format(thread_id =self.threadID, time= time.asctime()))
                           
            except :
                self.response = requests.exceptions.RequestException
                if self.save_frame:
                    cv.imwrite(str(config.CORAL_DATA_DIR) +'/'+ self.framename + config.IMG_FORMAT, self.frame)
                    print('Thread - {thread_id} Only  Saved Frame and Anotation Not Found at {time} ' .format(thread_id =self.threadID, time= time.ctime()))               
            
            print('Exiting thread - {thread_id} at {time} ' .format(thread_id =self.threadID, time= time.asctime()))
            
            self.session.close()
            return None        

