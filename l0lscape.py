from imaging.scanner import Chat
from imaging.identification import Rabbit
from settings.settings import Settings
from rsinput.input import RSInput
from commands.command import EmoteCommand, AdditionCommand, StaticCommand, DivisionCommand, MultiplicationCommand
from actions.action import Herblore
from actions.movement.movement import Move
from time import sleep

settings = Settings('config.ini')
chat = Chat(settings)
rs_input = RSInput()

# TODO: Make base class that each command inherits that contains a reference to rs_input & settings
commands = {
    'dance'    : EmoteCommand(value='dance', summary='Dances his heart out.', rs_input=rs_input, settings=settings),
    'jig'      : EmoteCommand(value='jig', summary='Does a jig :)', rs_input=rs_input, settings=settings),
    'celebrate': EmoteCommand(value='celebrate', summary='Celebrate :3', rs_input=rs_input, settings=settings),
    'salute'   : EmoteCommand(value='salute', summary='I salute you.', rs_input=rs_input, settings=settings),
    'panic'    : EmoteCommand(value='panic', summary='Oh no :(', rs_input=rs_input, settings=settings),
    'add'      : AdditionCommand(value='2+2', summary='I can do math :3', rs_input=rs_input, settings=settings),
    'about'    : StaticCommand(
        value='l0lscape. Try writing "command help".', 
        summary='About command.',
        rs_input=rs_input,
        settings=settings),
    'help'     : StaticCommand(
        value='My instructions must start with "command". dance celebrate jig salute & panic.',
        summary='Help command.',
        rs_input=rs_input,
        settings=settings),
    'hello'    : StaticCommand(
        value='l0l hello :3',
        summary='Says hello',
        rs_input=rs_input,
        settings=settings),
    'divide'   : DivisionCommand(value='4/4', summary='Divides user input', rs_input=rs_input, settings=settings),
    'multiply' : MultiplicationCommand(value='4*4', summary='Multiplies user input', rs_input=rs_input, settings=settings),
    'go=north' : Move(tiles=1, direction='North', rs_input=rs_input, settings=settings),
    'go=south' : Move(tiles=1, direction='South', rs_input=rs_input, settings=settings),
    'go=west'  : Move(tiles=1, direction='West', rs_input=rs_input, settings=settings),
    'go=east'  : Move(tiles=1, direction='East', rs_input=rs_input, settings=settings),
}

actions = {
    'herblore': Herblore(
        title='Potion maker',
        skill='Herblore',
        preset='2',
        hotbar_key='z',
        rs_input=rs_input,
        settings=settings)
}

monsters = {
    'rabbit': Rabbit(
        monster='Rabbit',
        image_count=2,
        settings=settings,
        rs_input=rs_input)
}

def run(cmd, obj_type=commands):
    obj_type[cmd].execute()

# TODO: Finish command handler
if __name__ == '__main__':
    tmp = None

    while 1:
        last_msg = chat.read_chatbox().lower()
        if last_msg != tmp:
            print(last_msg)
            tmp = last_msg

        if 'command' in last_msg:
            print(last_msg)

            cmd = last_msg.split('command ')[1].strip()

            if cmd in commands.keys():
                run(cmd)
                sleep(1)

        if 'math' in last_msg:
            print(last_msg)
            cmd = last_msg.split('math ')[1]
            
            if '*' in cmd:
                commands['multiply'].value = cmd.strip()
                run('multiply')
            elif '+' in cmd:
                commands['add'].value = cmd.strip()
                run('add')
            elif '/' in cmd:
                commands['divide'].value = cmd.strip()
                run('divide')
                
        sleep(0.1)
