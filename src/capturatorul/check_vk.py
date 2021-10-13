from pynput import keyboard
import sys

def on_press(key):
    vk = key.vk if hasattr(key, 'vk') else key.value.vk
    print('vk =', vk)
    if key == keyboard.Key.esc:
        # Stop listener
        return False

print('Start')

i = 0
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
    i += 1
    print(i)
    if i == 5:
        sys.exit()