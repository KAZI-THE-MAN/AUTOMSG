import pyautogui
import time
numberofmsg=10
while True:
    pyautogui.typewrite("I LIKE YOU")
    time.sleep(.600)
    pyautogui.typewrite("\n")
    time.sleep(2)

    numberofmsg = numberofmsg -1
    if numberofmsg == 0:
        break
