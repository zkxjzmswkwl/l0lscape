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
                sleep(uniform(0.02, 0.035))
                self._keyboard.release(char)

            sleep(0.2)
            self._keyboard.press(Key.space)
            self._keyboard.release(Key.space)

        self._keyboard.press(Key.enter)
        self._keyboard.release(Key.enter)

    def click(self, x, y):
        self._mouse.position = (x, y)
        sleep(0.1)
        self._mouse.press(Button.left)
        self._mouse.release(Button.left)



