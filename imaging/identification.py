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

    def match_image(self, img):
        if self.current_count > self._image_count:
            self.current_count = 1

        img = Imaging.preprocess(img)

        monster_img = cv2.imread(f'resources/{self._monster}-{self.current_count}.png')
        print(f'{self._monster}-{self.current_count}.png')
        monster_img = Imaging.preprocess(monster_img)
        w, h = monster_img.shape[:-1]
        #w, h = monster_img.shape

        res = cv2.matchTemplate(img, monster_img, cv2.TM_CCOEFF_NORMED)
        threshold = 0.82
        loc = np.where(res >= threshold)

        self.current_count += 1

        locs = []
        for _,pt in enumerate(zip(*loc[::-1])):
            cv2.rectangle(img, pt, (pt[0] + 5 + w, pt[1] + h), (0, 255, 0), 2)
            if _ == 0:
                locs.append(pt[0])
                locs.append(pt[1])
        if len(locs) > 0:
            cv2.imshow('Rabbit', img)
            cv2.waitKey(0)
#        return loc[:-2]
        return locs

        return None

    def find_color(self, img):
        img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        lower = np.array([100, 130, 200], np.uint8)
        upper = np.array([110, 140, 255], np.uint8)

        mask = cv2.inRange(img_hsv, lower, upper)
        cv2.imshow('aaa', mask);cv2.waitKey(0)
        i = np.column_stack(np.where(mask < 50))[0].tolist()

#        return i

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


