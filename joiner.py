import subprocess
import pyautogui
import time
import pandas as pd
from datetime import datetime

def sign_in(meetingid, pwd):
    #initiates the zoom app 
    subprocess.call("C:\\Users\\canyo\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe")
    #print("hello")
    #time.sleep(10) #gives adequate time for program to start next step
    while True:
        joinbutton = pyautogui.locateOnScreen('joinbutton.png')
        if joinbutton != None:
            pyautogui.click(joinbutton)
            print("Clicked the Join Button on Zoom")
        else: 
            print("Could not locate join button on Zoom")

sign_in(95200673544, 7377384)