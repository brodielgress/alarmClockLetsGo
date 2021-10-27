from datetime import datetime

now = datetime.now()
display_time = now.strftime('%H:%M')

    #todo Figure out how to convert user's input into datetime format: https://www.educative.io/edpresso/how-to-convert-a-string-to-a-date-in-python
def convert_user_time():
    user_input_str = str(input('Please enter a time for your alarm(HH:MM): '))

    date_time_obj = datetime.strptime(user_input_str, '%H:%M')

    print ('Your set alarm time is', date_time_obj)
    return date_time_obj

    #todo Check out timezone import.
def time_check():
    converted_time = convert_user_time()
    print(converted_time)
    print(display_time)
    print('The time now is', display_time)

    if converted_time == display_time:
        print('Wake up!')
    else:
        print('zzz...')
    
time_check()