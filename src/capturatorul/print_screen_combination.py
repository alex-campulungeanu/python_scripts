from datetime import datetime
import os

import pyautogui
from pynput import keyboard

SHOT_DIR = 'capturate'
STOP_SCRIPT_KEY = keyboard.Key.esc
CUR_DIR = os.path.dirname(os.path.realpath(__file__))
print(CUR_DIR)


def get_now():
    return datetime.now().strftime("%Y_%m_%d %H:%M:%S")
    

def capture_the_sht():
    print('Start printing')
    img_name = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    # print(img_name)
    img_storage = os.path.join(CUR_DIR, SHOT_DIR)
    img_path = os.path.join(img_storage, f'{img_name}.png')
    # my_shot = pyautogui.screenshot()
    # my_shot.save(img_path)
    pyautogui.screenshot(img_path)
    
def write_log():
    with open(os.path.join(CUR_DIR, 'log.txt'), 'a') as file:
        file.write(f"[+] {get_now()} write line \n")

pressed_vks = set()

COMBINATIONS = [
    # {keyboard.KeyCode(vk=162), keyboard.Key.shift, keyboard.KeyCode(vk=65), keyboard.KeyCode(vk=83)}  # shift + a (see below how to get vks)
    {keyboard.Key.shift, keyboard.KeyCode(vk=44)}  # 44 PrintScreenSysRq key, 162 ctrl
]

def execute():
    print ("Capture screen")
    write_log()

def get_vk(key):
    print (f"[+] {get_now()} get_vk: {key}")
    return key.vk if hasattr(key, 'vk') else key.value.vk

def is_combination_pressed(combination):
    """ Check if a combination is satisfied using the keys pressed in pressed_vks """
    return all([get_vk(key) in pressed_vks for key in combination])

def on_press(key):
    """ When a key is pressed """
    print(f'[+] {get_now()} [+] START ON PRESS')
    vk = get_vk(key)  # Get the key's vk
    pressed_vks.add(vk)  # Add it to the set of currently pressed keys

    for combination in COMBINATIONS:  # Loop though each combination
        if is_combination_pressed(combination):  # And check if all keys are pressed
            execute() # If they are all pressed, call your function
            # pressed_vks.clear()
            break  # Don't allow execute to be called more than once per key press

def on_release(key):
    print(f'[+] {get_now()} [+] START ON RELEASE')
    """ When a key is released """
    vk = get_vk(key)  # Get the key's vk
    pressed_vks.remove(vk)  # Remove it from the set of currently pressed keys
    if key == STOP_SCRIPT_KEY:
        print('STOP listener')
        # Stop listener
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()  # Join the listener thread to the current thread so we don't exit before it stops
