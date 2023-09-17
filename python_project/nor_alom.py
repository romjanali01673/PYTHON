import pyautogui
import time
time.sleep(5)
i = 0
while i <= 100:
    pyautogui.typewrite("pip install pyautogui")
    pyautogui.press("enter")
    #time.sleep()
    i = i+1

  