import win32gui
import time
import datetime
from tkinter.messagebox import showinfo

# Create a function that acts as a countdown:
def timer(h, m, s):
    total_sec = h * 3600 + m * 60 + s
    while total_sec > 0:
        time_left_countdown = datetime.timedelta(seconds=total_sec)
        print(time_left_countdown)
        time.sleep(1)
        total_sec -= 1
    print("The timer = 0 seconds")
#Create function that return the current app on focus:
def current_app_on_focus():
    while True:
        time.sleep(1)
        window_name = win32gui.GetWindowText(win32gui.GetForegroundWindow())
        print(window_name)

#Create a function that call a popup window message
def popup_message(message):
    return showinfo(title="Warning", message=message)

popup_message("You've been on Facebook for more than 20 minutes, I'm sorry but that's enough, take a break!")