import subprocess
import pyautogui
import time
import pandas as pd
from datetime import datetime

#temporary login creds: 
#id: 95200673544
#pwd: 7377384

def sign_in(meetingid, pwd):
    #initiates the zoom app 
    subprocess.call("C:\\Users\\canyo\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe")
    #print("hello")
    #time.sleep(10) #gives adequate time for program to start next step
    while True:
        joinbutton = pyautogui.locateOnScreen('joinbutton.png')
        if joinbutton != None:
            pyautogui.click(joinbutton)
            print("Found and clicked the Join Button on Zoom")
            break
        else: 
            print("Could not locate join button on Zoom")
            time.sleep(2)
            #delays for 2 seconds before repeating
    while True:
        field = pyautogui.locateOnScreen('field.png')
        if field != None:
            pyautogui.click(field)
            print("Found the enter field into location on Zoom")
            pyautogui.typewrite(id)
            
            break
        else: 
            print("Could not locate field info on Zoom")
            time.sleep(2)
            #delays for 2 seconds before repeating
sign_in(95200673544, 7377384)