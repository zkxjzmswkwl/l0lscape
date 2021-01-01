import configparser


class Emote:

    def __init__(self, settings, rs_input):
        self._settings = settings
        self._input = rs_input

    def perform(self, emote_name):
        """Performs an emote

        emote_name -- str
        """

        x, y = self._settings.get('POSITIONS', emote_name, True)
        self._input.click(int(x), int(y))
