# A Simple Alarm Clock

Hello! Welcome to my alarm clock app, a simple alarm clock that ticks down the time until you wake up.

**In order to use this app, open a terminal (either Powershell or the command prompt are recommended) and type "python app.py" to launch it.** 
**Do NOT use work_in_progress.py, nor error.txt. The former was how I tested new code out, while the latter is a record of errors.** 


## Python Features

###### 1. Master Loop
(Implement a “master loop” console application where the user can repeatedly enter commands/perform actions, including choosing to exit the program.)

The user has three options upon startup; the user can either 1) input a time, 2) check the current time, or 3) exit the program. If the user selects 1), the user can then either enter an alarm time that's formatted 24-hr style (##:##:##), or they can center 'cancel' to exit the input.

There's no way to cancel the alarm once it's been set; check incomplete code.


###### 2. Countdown Timer
(Calculate and display data based on an external factor (ex: get the current date, and display how many days remaining until some event.)

I use the datetime module several times in this app, to calculate the current time and create an effective timer. The user also has the ability to view the current time by selecting option 2 from the first menu.

###### 3. Regular Expression - Timer
(Implement a regular expression (regex) to ensure a field either a phone number or an email address 
is always stored and displayed in the same format.)

I imported re to help check whether the user inputs an appropriate alarm time that fits the parameters the printed instructions lay out. Re works in conjunction with the import logging to inform both the user and myself about errors.

## Other Python Features

###### 4. Logging errors

(Implement a log that records errors, invalid inputs, or other important events and writes them to a text file.)

This is here to log and record errors when users input incorrect options, such as a wrong choice or time. The log records the errors into the error.txt file as well. I think I should probably separate errors meant for the coder from errors meant for the user, however.

## Incomplete Code

When the user enters an appropriate alarm, the alarm begins ticking down, but I couldn't figure out how to let the user input a command to cancel the alarm while the alarm is ticking down. I tried to use import threading code, and it was able to read a commmand and input it later, but the problem was that the input was covered by the ticking alarm. Using '\n' just made the code enter a new line over and over again. I'm not sure if the terminal allows the user to input new commands while another code is still running. More research is required.

## Thank You!

That's my Python project. Thank you all; I hope you enjoy it a little! 

I mostly fell into the Python track by accident; the C# class I had intended to take had filled up, and so I selected Python 
because it was the one I knew the most about. I'm not sure I want to make Python my career. It seems mostly used for data analysis, 
which doesn't really complement my background. Yet, I find the language incredibly intuitive and easier to write than JavaScript, 
although I did enjoy the combination of HTML, CSS, and JavaScript in my previous tracks.