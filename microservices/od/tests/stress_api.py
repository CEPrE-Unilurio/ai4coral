from fe.frame_stream import VideoStream
from fe.settings import common as fe_config

VideoStream(src =str(fe_config.DATA_TEST_DIR) + '/test_video.mp4', show_frame=False, save_frame=False)
    