from abc import ABC, abstractmethod
from time import sleep
from random import uniform


class Action:

    def __init__(self, **kwargs):
        self.title       = kwargs.pop('title', None)
        self.skill       = kwargs.pop('skill', None)
        self.preset      = kwargs.pop('preset', None)
        self.hotbar_key  = kwargs.pop('hotbar_key', None)

        self._input      = kwargs.pop('rs_input', None)
        self._settings   = kwargs.pop('settings', None)
        self._should_run = False


        print(f'<-- {self.title} Action object instantiated. -->')

    @abstractmethod
    def execute(self):
        pass

    def range_sleep(self, mini=0.53, maxi=0.9):
        sleep(uniform(mini, maxi))


class Herblore(Action):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self._bank_x , self._bank_y = self._settings.get('POSITIONS', 'bank', True)

    def execute(self):
        print(f'Starting {self.title} module for the {self.skill} skill.')
        super().range_sleep(1, 2)
        self._input.click(int(self._bank_x), int(self._bank_y))
        super().range_sleep(1, 2)
        self._input.tap_key(self.preset)
        super().range_sleep(1, 2)
        self._input.tap_key(self.hotbar_key)
        super().range_sleep()
        self._input.tap_space()
        super().range_sleep(18, 21)

