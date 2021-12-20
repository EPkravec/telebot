import datetime
from time import sleep


def time_print():
    while True:
        now = datetime.datetime.now()
        real_time = now.strftime("%d-%m-%Y %H:%M:%S")
        sleep(1)
        return real_time
