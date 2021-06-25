
  
About the  $$ALARM CLOCK$$
It is no doubt that an alarm clock is always handy to alert us whenever we sleep, take a short nap, or to remind us about the work, we always get oblivious about.

::::::::::::::::::::::::Develop an Alarm Clock:::::::::::::::::::::::
About the Python Project
~~The objective of our project is to implement an alarm clock using Python.
~~ Python consists of some very innovative libraries such as datetime and tkinter which help us to build the project using the current      date and time as well as to provide a user interface to set the alarm according to the requirement  'HH:MM:SS AM/PM' in format.

#Source Code

# Importing required libraries
from datetime import datetime   #To set date and time
def validate_time(alarm_time):
    if len(alarm_time) != 11:
        return "Invalid time format! Please try again..."
    else:
        if int(alarm_time[0:2]) > 12:
            return "Invalid HOUR format! Please try again..."
        elif int(alarm_time[3:5]) > 59:
            return "Invalid MINUTE format! Please try again..."
        elif int(alarm_time[6:8]) > 59:
            return "Invalid SECOND format! Please try again..."
        else:
            return "ok"
    while True:
    alarm_time = input("Enter time in 'HH:MM:SS AM/PM' format: ")
    
    validate = validate_time(alarm_time.lower())
    if validate != "ok":
        print(validate)
    else:
        print(f"Setting alarm for {alarm_time}...")
        break
    alarm_hour = alarm_time[0:2]
    alarm_min = alarm_time[3:5]
    alarm_sec = alarm_time[6:8]
    alarm_period = alarm_time[9:].upper()
while True:
    now = datetime.now()
    current_hour = now.strftime("%I")
    current_min = now.strftime("%M")
    current_sec = now.strftime("%S")
    current_period = now.strftime("%p")

    if alarm_period == current_period:
        print("done 1")
        if alarm_hour == current_hour:
            print("done 2")
            if alarm_min == current_min:
                print("done 3")
                if alarm_sec == current_sec:
                    print("Wake Up!")
                    playsound('D:/Library/Documents/Projects/Coding/Beginner Python Projects/Alarm Clock/alarm.wav')
                    break

About my team::
Member1 = {Purva Kishor Sant}  {197050} {IT}
Member2 = {Sakshi Sanjay Kakde}  {197024} {IT} 