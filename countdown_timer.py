import time

#todo Figure out how to connect countdown_timer to alarm_clock
def countdown_timer(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print('Fire in the hole!!')

t = input("Enter the time in seconds: ")

countdown_timer(int(t))