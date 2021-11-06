from datetime import datetime
import time

now = datetime.now()
display_time = now.strftime('%H:%M:%S')
print('The time now is', display_time)

def convert_user_time():
    user_input_str = str(input('Please enter a time for your alarm(HH:MM:SS): '))
    print ('Your set alarm time is', user_input_str)
    return user_input_str

now = datetime.now()
alarm_time = now.strftime('%H:%M:%S')
m = time.localtime()
epoch_seconds = time.mktime(m)

def get_sec(time_str):
    h, m, s = time_str.split(':')
    s = int(h) * 3600 + int(m) * 60 + int(s)
    return s

day_seconds = epoch_seconds - get_sec(alarm_time)
alarm_seconds = day_seconds + get_sec(convert_user_time())
how_many_seconds_left = alarm_seconds - epoch_seconds

def countdown_timer(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print("You have", timer, "until your alarm.", end="\r")
        time.sleep(1)
        t -= 1

    print('\033[K','Wake up!')
    return t

countdown_timer(int(how_many_seconds_left))

#todo Make exit option for alarm

#todo Make display time tick down like alarm before user inputs alarm

#todo Allow user to set multiple alarms