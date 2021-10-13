import datetime

now = datetime.datetime.now()
display_time = now.strftime("%H:%M:%S")

def user_inputs_alarm():
    #todo create a function to allow a user to input a time for alarm
    pass

def convert_user_time():
    #todo Figure out how to convert user's input into datetime format: https://www.educative.io/edpresso/how-to-convert-a-string-to-a-date-in-python
    pass

def time_check():
    #todo Check out timezone import.
    converted_time = convert_user_time()
    if converted_time == now:
        print("Wake up!")
    else:
        print(display_time)
        print("zzz...")
    
time_check()