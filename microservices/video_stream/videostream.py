import cv2 as cv
import sys
import requests
from datetime import datetime
from pathlib import Path

cap = cv.VideoCapture(0)

cap.set(cv.CAP_PROP_FPS, 30.0)
cap.set(cv.CAP_PROP_FRAME_WIDTH,1280) # set Width
cap.set(cv.CAP_PROP_FRAME_HEIGHT,720) # set Height

#Underwater Api url
urlapi = 'http://127.0.0.1:8080'
BASE_DIR = Path('/')

while(True):
    ret, frame = cap.read()
    # frame = cv.flip(frame, -1) # Flip camera vertically
    # gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    cv.imshow('frame', frame)

    ## Make request do Underwater detection Api
    # response = requests.post(url = urlbase, data=frame)

    now = datetime.now()
    timestamp = datetime.timestamp(now)
    
    ##Save image and anotation xml
    # cv.imwrite(BASE_DIR+ str(timestamp) + '.jpg', frame)

    # if response.status_code == 200:
    #     cv.imwrite(str(timestamp) + '.jpg', frame)
    #     # print('Success!')
    # elif response.status_code == 404:
    #     print('Not Found.')
    
    k = cv.waitKey(30) & 0xff
    if k == 27: # press 'ESC' to quit
        break

cap.release()
cv.destroyAllWindows()