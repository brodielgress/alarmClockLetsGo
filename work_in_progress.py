from datetime import datetime
import time

# def display_time(t):
#     while t:
#         now = datetime.now()
#         current_time = now.strftime('%H:%M:%S')
#         print('The time now is', current_time, end="\r")
#         if t == 1:
#             break
#     return current_time

def clock():
    t = ''
    while t == '':
        print('The time is', datetime.now().strftime("%H:%M:%S"), end="\r")
        time.sleep(1)
        if t != '':
            break

def get_user_time():
    clock()
    user_input_str = str(input('Please enter a time for your alarm(HH:MM:SS): '))
    t = 'a'
    return user_input_str

get_user_time()

now = datetime.now()
alarm_time = now.strftime('%H:%M:%S')
m = time.localtime()
epoch_seconds = time.mktime(m)

def get_sec(time_str):
    h, m, s = time_str.split(':')
    s = int(h) * 3600 + int(m) * 60 + int(s)
    return s

def check_alarm():
    day_seconds = epoch_seconds - get_sec(alarm_time)
    alarm_seconds = day_seconds + get_sec(get_user_time())
    how_many_seconds_left = alarm_seconds - epoch_seconds
    if how_many_seconds_left < 0:
        print('Please enter a future time.')
    else:
        print ('Your set alarm time is', get_user_time())
        return how_many_seconds_left

def countdown_timer(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print("You have", timer, "until your alarm goes.", end="\r")
        time.sleep(1)
        t -= 1
    print('\033[K','Wake up!')
    return t

countdown_timer(int(check_alarm()))

#todo Make exit option for alarm

#todo Make display time tick down like alarm before user inputs alarm

#todo Allow user to set multiple alarms