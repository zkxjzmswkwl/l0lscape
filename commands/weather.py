from .command import Command
from bs4 import BeautifulSoup
import requests

WEATHER_URL = 'https://www.wunderground.com/weather/us/'


class Weather(Command):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # This is retarded I just didn't want to register an API key for a weather api.
    def execute(self):
        print('FUCK', self.value)
        r = requests.get(WEATHER_URL + f'{self.value[0]}/{self.value[1].strip()}')
        print(r.url)
        soup = BeautifulSoup(r.text, 'html.parser')
        temp = soup.find('div', {'class': 'current-temp'}).text

        super().say(f'In {self.value[1].replace("_", " ").upper()}, {self.value[0].upper()} it is currently {temp}')

