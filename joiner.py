import subprocess
import pyautogui
import time
import pandas as pd
from datetime import datetime

def sign_in(meetingid, pwd):
    #initiates the zoom app 
    subprocess.call(["/usr/bin/open", '/Users/canyo/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/zoom.us.app'])

    time.sleep(10) #gives adequate time for program to start next step
