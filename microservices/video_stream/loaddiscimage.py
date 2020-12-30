import cv2 as cv
import sys
import requests
from pathlib import Path
import os
from datetime import datetime
# from .microservices.object_detection.config import *

W = 640
H = 640
#Underwater Api url
urlapi = 'http://127.0.0.1:8080'
# BASE_DIR = Path('/')
data_directory = Path(__file__).parent / "../object_detection/test_images/"

file_names = [os.path.join(data_directory, f)
                for f in os.listdir(data_directory)]

for f in file_names:
    print(f)
    frame = cv.imread(f, 1)
    frame = cv.resize(frame,(W,H))

    cv.imshow('Image', frame)

    ## Make request do Underwater detection Api
    response = requests.post(url = urlapi, data=frame)

    now = datetime.now()
    timestamp = datetime.timestamp(now)
    
    ##Save image and anotation xml
    
    # if response.status_code == 200:
    #     cv.imwrite(str(timestamp) + '.png', frame)
    #     with open(str(timestamp) + '.xml', 'wb') as f:
    #         f.write(response.content)
    #     print('Success!')
    # elif response.status_code == 404:
    #     cv.imwrite(str(timestamp) + '.png', frame)
    #     print('Not Found.')
    
    cv.waitKey(0)
    cv.destroyAllWindows()