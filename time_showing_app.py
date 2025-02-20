import datetime 
import time 

def show_time():
    while True: 
        now = datetime.datetime.now()
        print(now)
        time.sleep(1)

show_time()