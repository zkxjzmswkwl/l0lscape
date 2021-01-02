from pynput.keyboard import Controller as KeyboardController
from pynput.keyboard import Key, Listener
from pynput.mouse import Controller as MouseController
from pynput.mouse import Button, Listener
import configparser

config = configparser.ConfigParser()
config.read('../config.ini')

def load_config():
    to_return = []

    for section in config.sections():
      for key in config[section]:
          to_return.append({'key': key, 'value': config[section][key]})

    return to_return

def listen():
    pass

def modal():
    pass

def open_url():
    pass

def default():
    pass
