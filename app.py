from datetime import datetime
import time

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
    elif choice == '2':
        now = datetime.now()
        display_time = now.strftime('%H:%M:%S')
        print('The time now is', display_time)
        handle_choice()
    elif choice == '3':
        return False
    else:
        print('Invalid option; please try again.')
        handle_choice()

now = datetime.now()
alarm_time = now.strftime('%H:%M:%S')
m = time.localtime()
epoch_seconds = time.mktime(m)

def get_user_time():
    user_input_str = str(input('Please enter a time for your alarm(HH:MM:SS): '))
    print('Your alarm is set to', user_input_str)
    return user_input_str

def get_sec(time_str):
    h, m, s = time_str.split(':')
    s = int(h) * 3600 + int(m) * 60 + int(s)
    return s

def check_alarm():
    user_alarm_time = get_user_time()
    day_seconds = epoch_seconds - get_sec(alarm_time)
    alarm_seconds = day_seconds + get_sec(user_alarm_time)
    how_many_seconds_left = alarm_seconds - epoch_seconds
    if how_many_seconds_left < 0:
        print('Please enter a future time.')
    return how_many_seconds_left

def countdown_timer(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print("You have", timer, "until your alarm.", end="\r")
        time.sleep(1)
        t -= 1
    print('\033[K','Wake up!')
    return t

def main():
    print_menu()
    while handle_choice():
        print_menu()

main()