from threading import Thread
from datetime import datetime
import time

thread_running = True

def clock():
    global thread_running

    while thread_running:
        time.sleep(1)
        if thread_running == True:
            print(datetime.now().strftime("%H:%M:%S"), end="\r")

def get_user_time():
    user_input_str = str(input('\n Please enter a time for your alarm(HH:MM:SS): '))
    print('Your alarm is set to ', user_input_str)
    return user_input_str

if __name__ == '__main__':
    t1 = Thread(target=get_user_time)
    t2 = Thread(target=clock)

    t1.start()
    t2.start()

    t2.join()
    thread_running = False