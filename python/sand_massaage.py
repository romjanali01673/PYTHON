# pyautogui are not support integer!

import pyautogui
import time
time.sleep(5 )
i = 0
#n = int (inpaut("inter  a number :"))
while i <= 5:
    pyautogui.typewrite("romajn") 
    pyautogui.press("enter")

    time.sleep(2)
    i+=1
