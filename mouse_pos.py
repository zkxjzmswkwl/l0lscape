from pynput.mouse import Button, Listener
from time import sleep
from configparser import ConfigParser

# Helper script to display current mouse x,y/save it to config

config = ConfigParser()
config.read('config.ini')

times_pressed = 0
x1 = y1 = x2 = y2 = None

def on_click(x, y, button, pressed):
    global times_pressed, config, x1, y1, x2, y2
    if button == Button.button9 and pressed:

#        if times_pressed == 0:
#            x1 = x
#            y1 = y
#            times_pressed += 1
#            return
#
#        if times_pressed == 1:
#            x2 = x
#            y2 = y
#
#            config['POSITIONS']['chat'] = f'{x1}-{y1}-{x2}-{y2}'
        config['POSITIONS']['bank'] = f'{x}-{y}'
        with open('config.ini', 'w') as conf_file:
            config.write(conf_file)

def on_scroll(x, y, dx, dy):
    pass

def on_move(x, y):
#    print(x, y)
    pass

mouse_listener = Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll)
mouse_listener.start()



while 1:
    sleep(0.05)
