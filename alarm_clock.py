from datetime import datetime

now = datetime.now()
display_time = now.strftime('%H:%M')

    #todo create a function to allow a user to input a time for alarm
def user_inputs_alarm():
    pass

    #todo Figure out how to convert user's input into datetime format: https://www.educative.io/edpresso/how-to-convert-a-string-to-a-date-in-python
def convert_user_time():
    user_input_str = str(input('Please enter a time for your alarm(yyyy-mm-dd HH:MM): '))

    date_time_obj = datetime.strptime(user_input_str, '%Y-%m-%d %H:%M')

    print ('Your set alarm time is', date_time_obj)
    return date_time_obj

    #todo Check out timezone import.
def time_check():
    converted_time = convert_user_time()
    print(converted_time)

    if converted_time == now:
        print('Wake up!')
    else:
        print('The time now is', display_time)
        print('zzz...')
    
time_check()