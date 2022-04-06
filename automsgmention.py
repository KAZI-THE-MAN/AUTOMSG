import pyautogui
import time
from random import randint
numberofmsg=10

def name():
    name_list= ["  Baby","  Janu","  Shuna","  Lifeline","  Cutyeyes"]
    rand_name =name_list[randint(0,len(name_list)-1)]
    return rand_name

while True:
    pyautogui.typewrite(f"I LIKE YOU{name()}")
    time.sleep(.600)
    pyautogui.typewrite("\n")
    time.sleep(2)
    numberofmsg = numberofmsg - 1
    if numberofmsg == 0:
        break
