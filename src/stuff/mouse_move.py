import sys
import pyautogui
import time
import random
import win32api

saved_pos = win32api.GetCursorPos()

while True:
    mouse_location = [100, 200, 300, 400]
    rand_pos = random.choice(mouse_location)
    pyautogui.moveTo(rand_pos, rand_pos, duration=1)
    time.sleep(2)
    current_pos = win32api.GetCursorPos()
    if saved_pos != current_pos:
        sys.exit("The use is now in control,  with great power comes great responsability !!")