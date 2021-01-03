import cv2 as cv
import sys
import requests
import time
from datetime import datetime
from pathlib import Path
from config import *

cap = cv.VideoCapture(0)

cap.set(cv.CAP_PROP_FPS, FPS) # set Frame por Seconds
cap.set(cv.CAP_PROP_FRAME_WIDTH,W) # set Width
cap.set(cv.CAP_PROP_FRAME_HEIGHT,H) # set Height

#Underwater Api url

numberFrame = 0

def sendApi(frame, framename):
    
    # content_type = 'image/jpg'
    # headers = {'content-type': content_type}
    imencoded = cv.imencode(".png", frame)[1].tobytes()

    response = requests.post(url= urlapi +'/'+framename, data=imencoded, timeout=5)
    return response

start = time.time()

while(True):
    ret, frame = cap.read()
    # frame = cv.flip(frame, -1) # Flip camera vertically
    # gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    cv.imshow('frame', frame)
    numberFrame = numberFrame + 1

    #Get the time for generate file name
    now = datetime.now()
    timestamp = datetime.timestamp(now)


    ## Make request do Underwater detection Api
    response = sendApi(frame, str(timestamp))
       
    #Save image and anotation xml
    if response.status_code == 200:
        cv.imwrite(str(CORAL_DATA_DIR) +'/'+ str(timestamp) + '.png', frame)
        with open(str(CORAL_DATA_DIR) +'/'+ str(timestamp) + '.xml', 'wb') as f:
            f.write(response.content)
        print('Success!')

    elif response.status_code == 404:
        cv.imwrite(str(CORAL_DATA_DIR) +'/'+ str(timestamp) + '.png', frame)
        print('Not Found.')
    
    k = cv.waitKey(30) & 0xff
    if k == 27: # press 'ESC' to quit
        break

end = time.time()

seconds = end - start
print ("Time taken : {0} seconds".format(seconds))
print ("Frame taken : ", numberFrame)

cap.release()
cv.destroyAllWindows()
