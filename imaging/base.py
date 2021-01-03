import cv2
import numpy as np
import pyscreenshot as screen


class Imaging:

    @staticmethod
    def preprocess(snapshot):
        # We need this to dilate and erode the snapshot
        kernel = np.ones((1, 1), np.uint8)

        snapshot = cv2.resize(snapshot, None, fx=1.6, fy=1.6, interpolation=cv2.INTER_CUBIC) 
        snapshot = cv2.cvtColor(snapshot, cv2.COLOR_BGR2GRAY)
        snapshot = cv2.dilate(snapshot, kernel, iterations=1)
        snapshot = cv2.erode(snapshot, kernel, iterations=1)
        snapshot = cv2.medianBlur(snapshot, 3)
        snapshot = cv2.threshold(cv2.medianBlur(snapshot, 3), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
#        cv2.imshow('debug', snapshot);cv2.waitKey(0)
        return snapshot

    @staticmethod
    def screenshot(bbox=(0,0,0,0)):
        """Takes a snapshot of screen region and applies preprocessing.

        Keyword argument:
        bbox -- bounding box (default 0,0,0,0)
        """

        # Take snapshot of region (defined as `bbox`) and cast it to a numpy array.
        snapshot = np.asarray(screen.grab(bbox=bbox))
        
        snapshot = Imaging.preprocess(snapshot)

        return snapshot
        
