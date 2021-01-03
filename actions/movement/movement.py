from abc import ABC, abstractmethod
from time import sleep
from random import uniform


class Movement(ABC):

    def __init__(self, **kwargs):
        self.tile_count = kwargs.pop('tiles', None)
        self.direction  = kwargs.pop('direction', None).lower()
        self._input     = kwargs.pop('rs_input', None)
        self._settings  = kwargs.pop('settings', None)

        print(f'<-- {self.direction} Movement object instantiated -->')

    @abstractmethod
    def execute(self):
        pass

    def say(self, msg):
        msg = msg.split(' ')
        self._input.write(msg)


class Move(Movement):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def execute(self):
        compass_x, compass_y = self._settings.get('POSITIONS', 'compass', True)
        tile_x, tile_y = self._settings.get('POSITIONS', f'{self.direction}_tile', True)

        super().say(f'Executing cmd: Move {self.direction} by {self.tile_count} tiles.')
        self._input.click(int(compass_x), int(compass_y))
        sleep(0.5)
        self._input.click(int(tile_x), int(tile_y))

