from datetime import datetime
import time
import re
import logging

# DEBUG: Detailed information, typically of interest only when diagnosing problems.

# INFO: Confirmation that things are working as expected.

# WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.

# ERROR: Due to a more serious problem, the software has not been able to perform some function.

# CRITICAL: A serious error, indicating that the program itself may be unable to continue running.

def print_menu():
    print('Time to set an alarm!')
    print('---------------------')
    print('Please select an option:')
    print()
    print('1) Set an alarm')
    print('2) Check the time')
    print('3) Exit')

def handle_choice():
    choice = input('Choice: ')
    if choice == '1':
        countdown_timer(int(check_alarm()))
        main()
    elif choice == '2':
        now = datetime.now()
        display_time = now.strftime('%H:%M:%S')
        print('The time now is', display_time)
        handle_choice()
    elif choice == '3':
        return False
    else:
        logging.error('Invalid option; please try again.')
        main()

def get_user_time():
    print('Please enter your time in 24-hr format! (e.g. 13:00:00, not 1:00:00)')
    print('Type cancel to exit.')
    user_input_str = str(input('HH:MM:SS: '))
    if user_input_str == 'cancel':
        user_input_str = datetime.now()
        main()
    elif re.match('\d{2}:\d{2}:\d{2}', user_input_str):
        print('Your alarm is set to', user_input_str)
        h, m, s = user_input_str.split(':')
        s = int(h) * 3600 + int(m) * 60 + int(s)
        return user_input_str
    else:
        logging.error('Invalid time; please try again')
        main()

def get_sec(time_str):
    h, m, s = time_str.split(':')
    s = int(h) * 3600 + int(m) * 60 + int(s)
    return s

def check_alarm():
    now = datetime.now()
    alarm_time = now.strftime('%H:%M:%S')
    m = time.localtime()
    epoch_seconds = time.mktime(m)

    user_alarm_time = get_user_time()
    day_seconds = epoch_seconds - get_sec(alarm_time)
    alarm_seconds = day_seconds + get_sec(user_alarm_time)
    how_many_seconds_left = alarm_seconds - epoch_seconds
    if how_many_seconds_left < 0:
        how_many_seconds_left = how_many_seconds_left + 86400
    return how_many_seconds_left

def countdown_timer(t):
    while t:
        mins, secs = divmod(t, 60)
        hrs, mins = divmod(mins, 60)
        timer = '{:02d}:{:02d}:{:02d}'.format(hrs, mins, secs)
        if t > 0:
            print("You have", timer, "until your alarm.", end="\r")
            time.sleep(1)
            t -= 1
        else:
            print('Invalid option; please try again.')
            main() 
    print('\033[K','Wake up!')
    main()
    return t

def main():
    print_menu()
    while handle_choice():
        print_menu()

main()