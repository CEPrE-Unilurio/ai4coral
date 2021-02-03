import sys
import time
from datetime import datetime
from pathlib import Path
from config import data_test_directory
from frame_stream import VideoStream
    
if __name__ == '__main__':

    """
    The VideoStream has the following argument:
        src(path): indicate the source of video, the default is camera with id =0
        show_frame(bool): indicate if the frame will be displayed or not, the default is TRUE
        isSave_Frame(bool): indicate if the frame will be saved or not, the default is TRUE
        
        Examples of usage:
            1 - VideoStream() - this will run openning the camera with id=0 and will display and save frame
            2 - VideoStream(show_frame=False) - this will not display the windows with frame
            3 - VideoStream(isSave_Frame=False) - this will not save frame
            
    """
    
    VideoStream(src = str(data_test_directory) + '/test_video.mp4')
    