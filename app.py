#Here are my imports.
from datetime import datetime
import time
import re
import logging

#This shows the user their options from the main menu.
def print_menu():
    print('Time to set an alarm!')
    print('---------------------')
    print('Please select an option:')
    print()
    print('1) Set an alarm')
    print('2) Check the time')
    print('3) Exit')

#This function creates the options for the user to set an alarm, check the time, or exit.
def handle_choice():
    choice = input('Choice: ')
    if choice == '1':
        get_user_time()
    elif choice == '2':
        now = datetime.now()
        display_time = now.strftime('%H:%M:%S')
        print('The time now is', display_time)
        handle_choice()
    elif choice == '3':
        return False
    else:
        error_A = [choice, ' is an invalid option; please try again.']
#The logging code here writes errors to the error.txt file, in case the user inputs something incorrect.
        logging.error(f'{choice} is an invalid option; please try again.')
        with open('error.txt', 'a') as f:
            f.write(time.ctime())
            f.write('\n')
            f.writelines(error_A)
            f.write('\n')
            f.write('\n')
        main()

#This function handles the user's inputted time, and allows the user to exit the input if they change their mind.
def get_user_time():
    print('Please enter your time in 24-hr format! (e.g. 13:00:00, not 1:00:00)')
    print('Type cancel to exit.')
    user_input_str = input('HH:MM:SS: ')
    if user_input_str == 'cancel':
        main()
    elif re.match('\d{2}:\d{2}:\d{2}', user_input_str):
        print('Your alarm is set to', user_input_str)
        h, m, s = user_input_str.split(':')
        s = int(h) * 3600 + int(m) * 60 + int(s)
        countdown_timer(int(check_alarm(user_input_str)))
        return user_input_str
    else:
        error_B = [user_input_str, ' is an invalid option; please try again.']
#The logging code here writes errors to the error.txt file, in case the user inputs something incorrect.
        logging.error(f'{user_input_str} is an invalid option; please try again.')
        with open('error.txt', 'a') as g:
            g.write(time.ctime())
            g.write('\n')
            g.writelines(error_B)
            g.write('\n')
            g.write('\n')
        main()

#This function changes the user's inputted time into a quantity of seconds, so it can play nicely with the 'now' quantity of seconds.
def get_sec(time_str):
    h, m, s = time_str.split(':')
    s = int(h) * 3600 + int(m) * 60 + int(s)
    return s

#I think I need to refactor this, but it ensures that the countdown is a positive number, in case the user enters an alarm for the next day.
def check_alarm(t):
    now = datetime.now()
    alarm_time = now.strftime('%H:%M:%S')
    m = time.localtime()
    epoch_seconds = time.mktime(m)

    user_alarm_time = t
    day_seconds = epoch_seconds - get_sec(alarm_time)
    alarm_seconds = day_seconds + get_sec(user_alarm_time)
    how_many_seconds_left = alarm_seconds - epoch_seconds
    if how_many_seconds_left < 0:
        how_many_seconds_left = how_many_seconds_left + 86400
    return how_many_seconds_left

#This creates the countdown timer the user sees on the terminal. There is no escape.
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

#This is the main function over all the code.
def main():
    print_menu()
    while handle_choice():
        print_menu()

main()