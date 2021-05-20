import subprocess
import pyautogui
import time
import pandas as pd
from datetime import datetime

#temporary login creds: 
#id: 4815396307
#pwd: 123456

def sign_in(id, pwd):
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
            pyautogui.click(pyautogui.locateOnScreen('joinbutton2.png'))
            break
        else: 
            print("Could not locate field info on Zoom")
            time.sleep(2)
            #delays for 2 seconds before repeating
    while True:
        field2 = pyautogui.locateOnScreen('field2.png')
        if field2 != None:
            pyautogui.click(field2)
            print("Found the enter password location on Zoom")
            pyautogui.typewrite(pwd) #enters password
            pyautogui.click(pyautogui.locateOnScreen('joinmeeting.png')) #joins meeting
            break
        else: 
            print("Could not locate password field on Zoom")
            time.sleep(2)
            #delays for 2 seconds before repeating


#ONLY MODIFY THIS FOLLOWING SECTION FOR PERSONAL USE!!!!!
#
#
#
#
#
#
#
#
#
#
#

while True:
    now = datetime.now()

    current_time = (now.strftime("%m-%d-%y %H:%M")) #times should be filled in this format: month, day, year --- hour:min
    #example imput: 05-20-21 22:16

    if current_time == "05-20-21 15:40": #MODIFY THIS FOR PERSONAL USE
        sign_in(4815396307, 123456) #REPLACE THESE TWO WITH ID AND PWD
        break
    else:
        print("It's not the right time")
        time.sleep(10)

#AFTER FILLING IN EVERYTHING RUN THE CODE ACCRORDING TO README
#
#
#
#
#
#
#



