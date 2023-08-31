# Automatic Zoom Bot

## **Overview:**
This Python program automatically joins online Zoom classes based on input from the "meetingschedule.csv" file.

## **Requirements:**

Before using this program, ensure the following:

1. The Zoom app must be installed on your system.
2. You must be logged into your Zoom account.
3. Manually enter the meeting time, Meeting ID, and passcode into the "meetingschedule.csv" file for the day.
4. Check your Zoom app settings (e.g., join audio on joining classes).
5. Python - Download and install from [python.org](https://www.python.org/downloads/).

## **Usage:**

Follow these steps to use the program:

1. Change the location of your Zoom app at line 29.
2. Change the x and y coordinates at line 32 to match the location of the "Join" button on your Zoom application.
3. Extract the "MousePosition32bit.zip" file and run the application to determine the x and y coordinates of your "Join" button. Enter these coordinates on line 20.
4. Open "meetingschedule.csv" and enter the scheduled time in the correct columns in the following format:

   * Time: hh:mm [24-hour format]
   * Meeting ID: 123456123 (string)
   * Meeting Password: 1234 (string)

5. Ensure all windows are closed and the desktop is clear, as this program relies on image recognition and automatic mouse movement.
6. Run `main.py`.
7. Keep an eye out for errors and failures. Please test the program before regular use.
8. Prevent your computer from entering sleep mode during long intervals between lectures.
9. Edit the `run.bat` file and add the path to your `python.exe` and your `.py` file.
10. If you prefer not to write code, you can use the `zoombot.rar` file, which contains a direct executable version of the program. However, you'll need to edit the `schedule.csv` file according to your class schedule.

## **Modules used:**
1. keyboard
2. time
3. subprocess
4. pyautogui
5. pandas
6. datetime
7. pillow
   
### To install the required modules, use the following commands:

```bash
pip install keyboard time subprocess pyautogui pandas datetime pillow
