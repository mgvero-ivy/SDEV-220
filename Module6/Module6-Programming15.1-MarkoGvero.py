# 15.1
from multiprocessing import Process
from datetime import datetime
import time
import random

def wait_random():
    wait_time = random.random()
    time.sleep(wait_time)

    c_time = datetime.now()

    c_time_formatted = c_time.strftime("%H:%M:%S")

    print(wait_time , "seconds waited, the current time is ", c_time_formatted)


if __name__ == "__main__":
    p1 = Process(target=wait_random)
    p2 = Process(target=wait_random)
    p3 = Process(target=wait_random)

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()

    print("multiprocessing completed")