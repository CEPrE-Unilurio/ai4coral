import os
from pathlib import  Path
from od.utils.logger import logger

CORAL_DATA_DIR = Path(__file__).parent.parent / "../coral_data/"
LOG_DIR = Path(__file__).parent.parent / "../logs/"

frame_size_log = logger(name='frame_size_log', filename=Path.joinpath(LOG_DIR,'frame_size_log.csv'), fmt='%(message)s')
xml_size_log = logger(name='xml_size_log', filename=Path.joinpath(LOG_DIR,'xml_size_log.csv'), fmt='%(message)s')

HEADER = 'SIZE FRAME'
frame_size_log.info(HEADER)

HEADER = 'XML FRAME'
xml_size_log.info(HEADER)

for f in os.listdir(CORAL_DATA_DIR):
    
    ext = os.path.splitext(f)[1]

    if ext == '.png':
        img_size = os.path.getsize(Path.joinpath(CORAL_DATA_DIR, f))
        img_size/=1024
        frame_size_log.info((f'{img_size:.2f}') )
    if ext == '.xml':
        xml_size =  os.path.getsize(Path.joinpath(CORAL_DATA_DIR, f))
        xml_size/=1024
        xml_size_log.info((f'{xml_size:.2f}') )
    