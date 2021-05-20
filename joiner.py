import subprocess
import pyautogui
import time
import pandas as pd
from datetime import datetime

def sign_in(meetingid, pwd):
    #initiates the zoom app 
    subprocess.call(["/usr/bin/open", '/Applications/zoom.us.app'])

sign_in()