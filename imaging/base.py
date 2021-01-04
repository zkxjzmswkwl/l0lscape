import cv2
import numpy as np
from mss import mss
import pyautogui


class Imaging:

    @staticmethod
    def preprocess(snapshot):
        # We need this to dilate and erode the snapshot
        kernel = np.ones((1, 1), np.uint8)

        snapshot = cv2.resize(snapshot, None, fx=1.6, fy=1.6, interpolation=cv2.INTER_CUBIC) 
        snapshot = cv2.cvtColor(snapshot, cv2.COLOR_BGR2GRAY)
        snapshot = cv2.dilate(snapshot, kernel, iterations=1)
        snapshot = cv2.erode(snapshot, kernel, iterations=1)
        snapshot = cv2.threshold(cv2.medianBlur(snapshot, 3), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
#        cv2.imshow('debug', snapshot);cv2.waitKey(0)
        return snapshot

    @staticmethod
    def screenshot(**kwargs):
        """Takes a snapshot of screen region and applies preprocessing.

        Keyword arguments:

        top    -- int
        left   -- int
        width  -- int
        height -- int
        """

        snapshot = np.asarray(mss().grab(kwargs))
        snapshot = Imaging.preprocess(snapshot)
        return snapshot
        

class Capture:

    def run(self):
        while True:
            cv2.imshow('L0lscape', Imaging.screenshot(top=0, left=0, width=3840, height=2160)) 
            if cv2.waitKey(1) == ord('q'):
                cv2.destroyAllWindows()
                break
