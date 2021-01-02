from imaging.scanner import Chat
from settings.settings import Settings
from rsinput.input import RSInput
from commands.command import EmoteCommand, AdditionCommand, StaticCommand
from actions.action import Herblore
from time import sleep

settings = Settings('config.ini')
chat = Chat(settings)
rs_input = RSInput()

commands = {
    'dance': EmoteCommand(value='dance', summary='Dances his heart out.', rs_input=rs_input, settings=settings),
    'jig': EmoteCommand(value='jig', summary='Does a jig :)', rs_input=rs_input, settings=settings),
    'celebrate': EmoteCommand(value='celebrate', summary='Celebrate :3', rs_input=rs_input, settings=settings),
    'salute': EmoteCommand(value='salute', summary='I salute you.', rs_input=rs_input, settings=settings),
    'panic': EmoteCommand(value='panic', summary='Oh no :(', rs_input=rs_input, settings=settings),
    'add': AdditionCommand(value='2+2', summary='I can do math :3', rs_input=rs_input, settings=settings),
    'about': StaticCommand(
        value='l0lscape. Try writing "command help".', 
        summary='About command.',
        rs_input=rs_input,
        settings=settings),
    'help': StaticCommand(
        value='My instructions must start with "command". dance celebrate jig salute & panic.',
        summary='Help command.',
        rs_input=rs_input,
        settings=settings)
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

def run(cmd, obj_type=commands):
    obj_type[cmd].execute()

# TODO: Finish command handler
if __name__ == '__main__':
    tmp = None

    while 1:
        run('herblore', actions)

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

            if 'add' in cmd:
                cmd = cmd.split('add ')[1].strip()
                commands['add'].value = cmd
                run('add')
                sleep(1)
                
        sleep(0.1)
