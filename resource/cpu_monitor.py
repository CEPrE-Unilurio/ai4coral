import sys
import psutil
import time
from pathlib import Path
from re import findall 
from time import sleep 
from subprocess import check_output 
from od.utils.logger import logger


def get_temp():
    """
        THIS FUCNTION ONLY RUN ON RASPBERRY TO GET THE ACTUAL TEMPERATURE OF THE DEVICE
    """
    temp = check_output(["vcgencmd","measure_temp"]).decode()
    temp = float(findall('\d+\.\d+', temp)[0])
    return(temp)

def cpu_stats():

    HEADER = 'TIME,TEMPERATURE,CPU_USAGE,CPU_1,CPU_2,CPU_3,CPU_4'
    cpu_log.info(HEADER)

    try:
        while True:

            temp = get_temp()
            cpu_percent = psutil.cpu_percent(interval=1)
            cpu_percents = psutil.cpu_percent(interval=1, percpu=True)
            now = time.time()

            cpu_var = f'{now},{temp},{cpu_percent},{cpu_percents[0]},{cpu_percents[1]},{cpu_percents[2]},{cpu_percents[3]}'
                        
            cpu_log.info(cpu_var)
            
            sleep(1)

    except KeyboardInterrupt:
        print("Exit pressed Ctrl+C")

if __name__ == '__main__':
    
    LOG_DIR = Path(__file__).parent.parent / "../logs/cpu_log.csv"

    cpu_log = logger(name='cpu_log', filename=LOG_DIR, fmt='%(message)s')
    
    cpu_stats()