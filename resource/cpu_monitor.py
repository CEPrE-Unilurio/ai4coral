import sys
import psutil
from pathlib import Path
from re import findall 
from time import sleep 
from subprocess import check_output 
from od.utils.logger import logger

def get_temperature():
    """
        THIS FUCNTION ONLY RUN ON RASPBERRY TO GET THE ACTUAL TEMPERATURE OF THE DEVICE
    """
    temp = check_output(["vcgencmd","measure_temp"]).decode()
    temp = float(findall('\d+\.\d+', temp)[0])
    return(temp)

def cpu_stats():

    HEADER = 'TEMPERATURE,CPU_USAGE,CPU_1,CPU_2,CPU_3,CPU_4'
    cpu_log.info(HEADER)

    try:
        while True:

            # temp = get_temperature()
            cpu_percent = psutil.cpu_percent(interval=1)
            cpu_percents = psutil.cpu_percent(interval=1, percpu=True)

            cpu_var = f'{86},{cpu_percent},{cpu_percents[0]},{cpu_percents[1]},{cpu_percents[2]},{cpu_percents[3]}'
                        
            cpu_log.info(cpu_var)
            
            sleep(1)

    except KeyboardInterrupt:
        print("Exit pressed Ctrl+C")

if __name__ == '__main__':
    
    LOG_DIR = Path(__file__).parent.parent / "../logs/cpu_log.csv"

    cpu_log = logger(name='cpu_log', filename=LOG_DIR, fmt='%(message)s')
    
    cpu_stats()