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

class request_api ():

    def __init__(self, frame, framename, threadID, t_Lock):    
        self.frame = frame
        self.framename = framename
        self.threadID = threadID
        self.t_Lock = t_Lock
        self.thread = Thread(target=self.run)
        self.thread.daemon = True
        self.thread.start()
      
    def run (self):

        self.t_Lock.acquire()

        print('Initialize thread - ' + str(self.threadID))
        self.imencoded = cv.imencode('.PNG', self.frame)[1].tobytes()

        self.session = requests.Session()
                
        try:

            start_at = time.time()          
            self.response = self.session.post(url= urlapi +'/'+ self.framename, data=self.imencoded)            

            cv.imwrite(str(CORAL_DATA_DIR) +'/'+ self.framename + img_format, self.frame)
            with open(str(CORAL_DATA_DIR) +'/'+ self.framename + '.xml', 'wb') as f:
                f.write(self.response.content)
            print("Frame and anotation saved")           
            
        except :
            # self.response = requests.exceptions.RequestException
            cv.imwrite(str(CORAL_DATA_DIR) +'/'+ self.framename + img_format, self.frame)
            print('Frame Saved and Anotation Not Found.')
        
        print("Time taken {:.2f}" .format(time.time()-start_at) )
        print('Exiting thread - ' + str(self.threadID))
        self.session.close()
        self.t_Lock.release()            
        

    def join(self):
        self.thread.join()   
            