#! python3
# lookingbusy.py - Moves the mouse every 10 seconds to trick the
# computer that you are busy working

import time
import pyautogui

print('Print Ctrl-C to End')

try:
    while True:
        pyautogui.moveRel(-100,0)
        pyautogui.moveRel(100,0)
        time.sleep(10)
except KeyboardInterrupt:
    print('Ended')
