import keyboard, time, subprocess
import pandas as pd
from datetime import datetime
import pyautogui

hashes = "#" * 95

print('\n\n', hashes)

print('Welcome to Automatic Zoom Bot, lazy people!! ^_^')
print(">>If you've reached here I'm assuming you've read the README.md and have the settings configured")
print(">>Please check all the configurations before proceeding as it may cause this program to crash otherwise")
print(">>Please keep this program running in the background at all times (if you want to run it everyday)")
print("Requirements : ( python version > 3.0 ) and ( all packages installed )")
print('You can exit this program using ( Ctrl+c ) at any time')

print('\n', hashes)


df = pd.read_csv('meetingschedule.csv')
df_new = pd.DataFrame()

while(True):
    
    timestr = datetime.now().strftime("%H:%M")
    
    if timestr in df.Time.values:
        df_new = df[df['Time'].astype(str).str.contains(timestr)]
        
        subprocess.Popen("C:\\Users\\ABHAY VERMA\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe")
        time.sleep(10)
       
        pyautogui.mouseUp(button='left', x=763, y=420)
        pyautogui.click()
        time.sleep(5)
        
        keyboard.write(df_new.iloc[0,1])

        
        position = pyautogui.locateOnScreen("buttons\\turn_off_vid_button.png")
        pyautogui.moveTo(position)
        pyautogui.click()
        time.sleep(5)

        
        position = pyautogui.locateOnScreen("buttons\\join_button_2.png")
        pyautogui.moveTo(position)
        pyautogui.click()
        time.sleep(7)

        
        keyboard.write(str(int(df_new.iloc[0,2])))
        time.sleep(5)

        
        position = pyautogui.locateOnScreen("buttons\\join_meeting.png")
        pyautogui.moveTo(position)
        pyautogui.click()

        
        time.sleep(60)



