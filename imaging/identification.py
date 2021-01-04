from abc import abstractmethod
from .base import Imaging
import cv2
import pytesseract
import numpy as np
import pyscreenshot as screen
from time import sleep
from random import uniform

# README: This entire file is a mess right now and is a conceptual WIP.


class Identification:

    def __init__(self, **kwargs):
        self.id_count  = 0
        self.current_count = 1
        self._monster  = kwargs.pop('monster', None)
        self._image_count = kwargs.pop('image_count', None)
        self._settings = kwargs.pop('settings', None)
        self._input = kwargs.pop('rs_input', None)

    def match_image(self, img, threshold=0.69):
        sub_img = cv2.imread(f'resources/{self._monster}.png')

        sub_img = Imaging.preprocess(sub_img)
        img = Imaging.preprocess(img)

        w, h = sub_img.shape[:-1]

        res = cv2.matchTemplate(img, sub_img, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= threshold)

        for pt in zip(*loc[::-1]):
            cv2.rectangle(img, pt, (pt[0] + 5 + w, pt[1] + h), (255, 255, 0), 2)

        return loc

    @staticmethod
    def find_color(self, img, upper, lower):
        """Returns stacked column of x,y coordinates
        of hsv range

        img -- np.array
        """

        img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        lower = np.array([100, 130, 200], np.uint8)
        upper = np.array([110, 140, 255], np.uint8)

        mask = cv2.inRange(img_hsv, lower, upper)

        cv2.imshow('debug', mask);cv2.waitKey(0)

        return np.column_stack(np.where(mask < 50))[0].tolist()

    @abstractmethod
    def execute(self, region):
        pass


class Rabbit(Identification):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        x1, y1, x2, y2 = self._settings.get('POSITIONS', 'rabbit_region', True)
        self._region = [0, 0, 3840, 2160]

    def execute(self):
        snapshot = np.asarray(screen.grab(bbox=self._region))
      #  rabbit_pos = super().match_image(snapshot)
        rabbit_pos = super().find_color(snapshot)
        print(rabbit_pos)

        if rabbit_pos:
            self._input.click(int(rabbit_pos[0]), int(rabbit_pos[1]))
            sleep(uniform(1, 1.5))


