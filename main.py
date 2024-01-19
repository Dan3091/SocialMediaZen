import win32gui
import time
from tkinter.messagebox import showinfo
from tkinter import Tk
import webbrowser


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
    try:
        webbrowser.register('chrome',
                            None,
                            webbrowser.BackgroundBrowser("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"))
        webbrowser.get('chrome').open(url, new=0)
    except:
        pass

#The main logic function:
def main(h, m, s):
    """
    Given the time in hours, minutes and seconds format to the main function,
     it returns the popup_message(message) and redirect_to_homepage() functions.
     """

    name = ""
    total_sec = h * 3600 + m * 60 + s
    social_media = ["YouTube", "Facebook", "Instagram"]
    while total_sec > 0:
        app_name = current_app_on_focus()
        for social in social_media:
            if social in app_name:
                name = social
                time.sleep(1)
                total_sec -= 1
    return popup_message(f"You've been on {name} for more than 20 minutes, I'm sorry but that's enough, take a break!"),\
        redirect_to_homepage()

if __name__ == "__main__":
    window = Tk()
    window.attributes('-topmost', 1)
    window.withdraw()
    showinfo(title="Info", message="Welcome To SocialMediaZen App!!! Leave the app in background...")
    while True:
        main(0, 20, 0)