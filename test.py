from threading import current_thread
from tkinter import *
import datetime
import time
import winsound

def alam(set_alam_timer):
    while True:
        time.sleep(1)
        #Import the datetime module and display the current date:
        current_time = datetime.datetime.now()
        now = current_time.time.strftime("%H :%M : %S")
        date = current_time.time.strftime("%D :%m : %Y")
        print(" THE SET DATE IS :",date)
        print(now)
        if now == set_alam_timer:
            print("Time to Wake up")
        winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
        break

