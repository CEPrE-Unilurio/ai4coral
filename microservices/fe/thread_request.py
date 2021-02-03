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

class Request_api (threading.Thread):
    """ 
        The request_ api class is responsible for create thread for each graped frame.

        args:
            frame(obj): a byte of image
            framename(str): a timestanp used to named the frame
            thread_id(int): the id of a given thread
            t_Lock(:obj: int): the semaphore to control the number of threa opened
            isSave_Frame(bool) : defin if the frame should be saved in disk or not.       
        
        Attributes:
            frame(obj): a byte of image
            framename(str): a timestanp used to named the frame
            t_Lock(:obj: int): the semaphore to control the number of threa opened
            thread_id(int): the id of a given thread
            isSave_Frame(bool) : defin if the frame should be saved in disk or not.
        
        Return:
            None
    """

    def __init__(self, frame, framename, threadID, t_Lock, isSave_Frame):
        threading.Thread.__init__(self, daemon=False)    
        self.frame = frame
        self.framename = framename
        self.threadID = threadID
        self.t_Lock = t_Lock
        self.isSave_Frame = isSave_Frame
        self.start()
      
    def run (self):
        
        with self.t_Lock: 

            print('Initialize thread -{thread_id} at {time} ' .format(thread_id =self.threadID, time= time.asctime()))
            
            self.imencoded = cv.imencode('.PNG', self.frame)[1].tobytes()

            self.session = requests.Session()
                    
            try:
                                       
                self.response = self.session.post(url= urlapi +'/'+ self.framename, data=self.imencoded)
                
                print(self.response.status_code)            

                if self.isSave_Frame:
                    cv.imwrite(str(CORAL_DATA_DIR) +'/'+ self.framename + img_format, self.frame)
                    with open(str(CORAL_DATA_DIR) +'/'+ self.framename + '.xml', 'wb') as f:
                        f.write(self.response.content)
                    print('Thread - {thread_id}  Saved Frame & Anotation at {time} ' .format(thread_id =self.threadID, time= time.asctime()))
                           
            except :
                self.response = requests.exceptions.RequestException
                if self.isSave_Frame:
                    cv.imwrite(str(CORAL_DATA_DIR) +'/'+ self.framename + img_format, self.frame)
                    print('Thread - {thread_id} Only  Saved Frame and Anotation Not Found at {time} ' .format(thread_id =self.threadID, time= time.ctime()))               
            
            print('Exiting thread - {thread_id} at {time} ' .format(thread_id =self.threadID, time= time.asctime()))
            
            self.session.close()
            return None        

