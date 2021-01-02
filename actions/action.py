

class Action:

    def __init__(self, **kwargs):
        self.title = kwargs.pop('title', None)
        self.skill = kwargs.pop('skill', None)

        self._input = kwargs.pop('rs_input', None)
        self._settings = kwargs.pop('settings', None)

    @abstractmethod
    def execute(self):
        pass


class Heblore(Action):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def execute(self):
        pass
