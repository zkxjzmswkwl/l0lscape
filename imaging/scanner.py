import pytesseract as ocr
import cv2
from imaging.base import Imaging


class Chat:

    def __init__(self, settings):
        self._settings = settings
        self._capture  = cv2.namedWindow('L0Lscape')

    def image_chatbox(self):
        """Returns preprocessed image of chatbox"""

        x1, y1, x2, y2 = self._settings.get('POSITIONS', 'chat', True)
        width = x2 - x1
        height = y2 - y1
        return Imaging.screenshot(top=y1, left=x1, width=width, height=height)

    def read_chatbox(self, img=None):
        """Scans chatbox image and returns string for last message

        img -- numpy array (default=None)
        """

        if img is None:
            img = self.image_chatbox()

        cv2.imshow('L0Lscape', img)
        if cv2.waitKey(1) == ord('q'):
            cv2.destroyAllWindows()

        return ocr.image_to_string(img, lang='eng')
