import time
from pynput.keyboard import Key, Controller


keyboard = Controller()

while True:
    time.sleep(20)

    keyboard.press(Key.up)
    keyboard.release(Key.up)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)