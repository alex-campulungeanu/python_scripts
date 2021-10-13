from datetime import datetime
import os

# from PIL import ImageGrab
import keyboard
import pyautogui
# from pynput import keyboard

SHOT_DIR = 'capturate'
PRINT_SCRIPT_KEY = 'print screen'
STOP_SCRIPT_KEY = 'esc'
CUR_DIR = os.path.dirname(os.path.realpath(__file__))


def get_now():
    return datetime.now().strftime("%Y_%m_%d %H:%M:%S")
    

def capture_the_sht():
    img_name = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    img_storage = os.path.join(CUR_DIR, SHOT_DIR)
    img_path = os.path.join(img_storage, f'{img_name}.png')
    print(f'[+] CAPTURE IMAGE {img_path}')
    my_shot = pyautogui.screenshot()
    my_shot.save(img_path)
    return img_path
    
def write_log(text='write line default'):
    with open(os.path.join(CUR_DIR, 'log.txt'), 'a+') as file:
        file.write(f"[+] {get_now()} {text} \n")

if __name__ == '__main__':
    print('[+] START listening !')
    while True:
        try:
            if keyboard.is_pressed(PRINT_SCRIPT_KEY):
            #    image = ImageGrab.grab()
            #    image.save("screenshot.png")
                img = capture_the_sht()
                write_log(img)
            elif keyboard.is_pressed(STOP_SCRIPT_KEY):
                break
            else:
                pass
        except Exception as e:
            print(f'Something went wronkg {e}')
            break
