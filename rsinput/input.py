from pynput.keyboard import Key, Listener 
from pynput.keyboard import Controller as KeyboardController
from pynput.mouse import Controller as MouseController
from pynput.mouse import Button
from time import sleep
from random import uniform


class RSInput:

    def __init__(self):
        self._keyboard = KeyboardController()
        self._mouse = MouseController()

    def write(self, msg):
        self._keyboard.press(Key.enter)
        sleep(uniform(0.02, 0.08))
        self._keyboard.release(Key.enter)
       
        for word in msg:
            for char in word:
                self._keyboard.press(char)
                sleep(uniform(0.02, 0.025))
                self._keyboard.release(char)

            sleep(0.05)
            self._keyboard.press(Key.space)
            self._keyboard.release(Key.space)

        self._keyboard.press(Key.enter)
        self._keyboard.release(Key.enter)

    def click(self, x, y):
        self._mouse.position = (x, y)
        sleep(uniform(0.08, 0.152))
        self._mouse.press(Button.left)
        sleep(uniform(0.04, 0.118))
        self._mouse.release(Button.left)

    def tap_key(self, key):
        self._keyboard.press(key)
        sleep(uniform(0.08, 0.152))
        self._keyboard.release(key)

    def tap_space(self):
        self._keyboard.press(Key.space)
        sleep(uniform(0.08, 0.152))
        self._keyboard.release(Key.space)
