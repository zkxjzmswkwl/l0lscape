from abc import ABC, abstractmethod
from actions.emote import Emote
from time import sleep


class Command:

    def __init__(self, **kwargs):
        self.value = kwargs.pop('value', None)
        self.summary = kwargs.pop('summary', None)

        self._input = kwargs.pop('rs_input', None)
        self._settings = kwargs.pop('settings', None)

        self._emote = Emote(self._settings, self._input)

    @abstractmethod
    def execute(self):
        pass

    def say(self, msg):
        msg = msg.split(' ')
        self._input.write(msg)

    def emote(self, name):
        self._emote.perform(name)


class StaticCommand(Command):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def execute(self):
        super().say(self.value)


class EmoteCommand(Command):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def execute(self):
        super().say(f'L0lscape chat bot executing cmd: {self.value}!')
        sleep(0.2)
        super().emote(self.value)


class AdditionCommand(Command):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def execute(self):
        i, j = self.value.split('+')
        print(i, j)
        super().say(f'L0Lscape chat bot: The sum of {i} + {j} is {str(int(i) + int(j))}!')


