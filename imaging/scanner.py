import pytesseract as ocr
import cv2
from imaging.base import Imaging as imaging


class Chat:

    def __init__(self, settings):
        self._settings = settings

    def image_chatbox(self):
        """Returns preprocessed image of chatbox"""

        x1, y1, x2, y2 = self._settings.get('POSITIONS', 'chat', True)
        return imaging.screenshot((int(x1), int(y1), int(x2), int(y2)))

    def read_chatbox(self, img=None):
        """Scans chatbox image and returns string for last message

        img -- numpy array (default=None)
        """

        if img is None:
            img = self.image_chatbox()

        return ocr.image_to_string(img, lang='eng')
