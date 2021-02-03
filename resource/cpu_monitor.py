import sys
import psutil
import time
from re import findall 
from time import sleep 
from subprocess import check_output 

def get_temp():
    """
        THIS FUCNTION ONLY RUN ON RASPBERRY TO GET THE ACTUAL TEMPERATURE OF THE DEVICE
    """
    temp = check_output(["vcgencmd","measure_temp"]).decode()
    temp = float(findall('\d+\.\d+', temp)[0])
    return(temp)

def cpu_stats():

    try:
        while True:
            temp = get_temp()
            cpu_percent = psutil.cpu_percent(interval=1)
            
            print('Time - {time}  temperature = {temp} - cpu_usage = {cpu} '
             .format(time= time.asctime(), temp= temp, cpu=cpu_percent ))

            sleep(1)

    except KeyboardInterrupt:
        print("Exit pressed Ctrl+C")


if __name__ == '__main__':
    cpu_stats()