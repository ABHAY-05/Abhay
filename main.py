import keyboard, time, subprocess
import pandas as pd
from datetime import datetime
import pyautogui


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



