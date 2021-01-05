import cv2 as cv
import sys
import requests
from pathlib import Path
import os
from datetime import datetime
from  config import *

file_names = [os.path.join(data_test_directory, f)
                for f in os.listdir(data_test_directory)]

for filename in file_names:
    print(filename)
    frame = cv.imread(filename, 1)
    frame = cv.resize(frame,(W,H))

    cv.imshow('Image', frame)

    ## Make request do Underwater detection Api
    response = requests.post(url= urlapi, data=frame.tobytes())

    # now = datetime.now()
    # timestamp = datetime.timestamp(now)
    
    ##Save anotation xml
    if response.status_code == 200:
        with open(str(filename) + '.xml', 'wb') as f:
            f.write(response.content)
        print('Success!')
    elif response.status_code == 404:
        print('Not Found.')
    
    cv.waitKey(0)
    cv.destroyAllWindows()