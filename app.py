import win32gui
import time
import datetime
from tkinter.messagebox import showinfo
from tkinter import Tk
import webbrowser


message = "You've been on Facebook for more than 20 minutes, I'm sorry but that's enough, take a break!"
# Create a function that acts as a countdown:
def timer(h, m, s):
    total_sec = h * 3600 + m * 60 + s
    social_media = ["YouTube", "Facebook", "Instagram"]
    while total_sec > 0:
        app_name = current_app_on_focus()
        print(app_name)
        for social in social_media:
            if social in app_name:
                time_left_countdown = datetime.timedelta(seconds=total_sec)
                time.sleep(1)
                total_sec -= 1
    return popup_message(message), redirect_to_homepage()

#Create function that return the current app on focus:
def current_app_on_focus():
    window_name = win32gui.GetWindowText(win32gui.GetForegroundWindow())
    return window_name

#Create a function that call a popup window message:
def popup_message(message):
    window = Tk()
    window.attributes('-topmost', 1)
    window.withdraw()
    return showinfo(title="Warning", message=message)

#Create a function to redirect to homepage:
def redirect_to_homepage():
    url = 'https://google.com'
    webbrowser.register('chrome',
                    None,
                    webbrowser.BackgroundBrowser("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"))
    webbrowser.get('chrome').open(url, new=0)
