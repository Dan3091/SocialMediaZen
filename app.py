import win32gui
import time
import datetime

# Create a function that acts as a countdown:
def timer(h, m, s):
    total_sec = h * 3600 + m * 60 + s
    while total_sec > 0:
        time_left_countdown = datetime.timedelta(seconds=total_sec)
        print(time_left_countdown)
        time.sleep(1)
        total_sec -= 1
    print("The timer = 0 seconds")

timer(00, 00, 10)