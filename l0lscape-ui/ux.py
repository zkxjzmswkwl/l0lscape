import dearpygui.core as core
import dearpygui.simple as simple
from logic import listen, load_config, modal, open_url, default

WINDOW = 'L0lScape Configuration'

with simple.window(WINDOW):
    core.set_main_window_title(WINDOW)
    core.set_main_window_size(430, 460)

    core.set_theme('Purple')

    core.set_style_item_spacing(5, 5)
    core.set_style_frame_padding(5, 5)

    core.add_additional_font('resources/monofur.ttf', 18)

    core.add_dummy(width=140)
    core.add_same_line()
    core.add_image('logo', 'resources/l0lscape.png')

    core.add_button('About', callback=modal, width=100)
    core.add_same_line()
    core.add_button('Github', callback=open_url, width=100)
    core.add_same_line()
    core.add_button('Discord', callback=open_url, width=100)
    core.add_same_line()
    core.add_button('Help', callback=open_url, width=100)

    core.add_separator()

    for value in load_config():
        key = value.get('key')

        core.add_text(f'{key}', bullet=True)
        core.add_input_text(f'{key}-input', default_value=value.get('value'), width=205, label='')
        core.add_same_line()
        core.add_button(key + '_listen', label='Listen', callback=listen, width=100)
        core.add_same_line()
        core.add_button(key + '_default', label='Default', callback=default, width=100)
        core.add_separator()

core.start_dearpygui(primary_window=WINDOW)
