from imaging.scanner import Chat
from settings.settings import Settings
from rsinput.input import RSInput
from commands.command import EmoteCommand, AdditionCommand
from time import sleep

settings = Settings('config.ini')
chat = Chat(settings)
rs_input = RSInput()

commands = {
    'dance': EmoteCommand(value='dance', summary='Fuck you', rs_input=rs_input, settings=settings),
    'jig': EmoteCommand(value='jig', summary='Jig you', rs_input=rs_input, settings=settings),
    'celebrate': EmoteCommand(value='celebrate', summary='Celebrate :3', rs_input=rs_input, settings=settings),
    'salute': EmoteCommand(value='salute', summary='I salute you', rs_input=rs_input, settings=settings),
    'panic': EmoteCommand(value='panic', summary='Oh no :(', rs_input=rs_input, settings=settings),
    'add': AdditionCommand(value='2+2', summary='I can do math :3', rs_input=rs_input, settings=settings)
}

def run(cmd):
    print(cmd)
    commands[cmd].execute()


# TODO: Finish command handler
if __name__ == '__main__':

    while 1:
        last_msg = chat.read_chatbox().lower()

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
        
