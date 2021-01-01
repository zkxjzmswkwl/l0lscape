import cv2
import numpy as np
import pyscreenshot as screen


class Imaging:

    @staticmethod
    def screenshot(bbox=(0,0,0,0)):
        """Takes a snapshot of screen region and applies preprocessing.

        Keyword argument:
        bbox -- bounding box (default 0,0,0,0)
        """

        # Take snapshot of region (defined as `bbox`) and cast it to a numpy array.
        snapshot = np.asarray(screen.grab(bbox=bbox))

        # Apply preprocessing
        snapshot = cv2.resize(snapshot, None, fx=3, fy=3, interpolation=cv2.INTER_CUBIC) 
        snapshot = cv2.cvtColor(snapshot, cv2.COLOR_BGR2HSV)

        return snapshot
        
