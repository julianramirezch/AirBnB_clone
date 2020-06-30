#!/usr/bin/python3
import cmd
import sys
from airbnb.models import *


class console_colors:
    lightgray = '\033[37m'
    magenta = '\033[35m'
    blue = '\033[94m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    end = '\033[0m'


class HBNBCommand(cmd.Cmd):
    intro = console_colors.magenta + 'Welcome to \'hbnb\'.   Type help or ? to list commands.\n' + console_colors.end
    prompt = console_colors.red + '(hbnh) ' + console_colors.end
    file = None

    def do_help(self, arg):
        if arg == 'quit' or arg == 'EOF':
            print(console_colors.yellow + "Quit command to exit the program" + console_colors.end)
        else:
            print("""Documented commands (type help <topic>):
                ========================================
                EOF  help  quit
                """)

    def do_EOF(self, arg):
        return True

    def do_quit(self, arg):
        return True
    
    def emptyline(self):
        pass

    def do_create(self, arg):
        if len(arg) == 0:
            print("Please enter a further instruction")
            return
        arg_list = arg.split()
        try:
            inst = eval(arg_list[0])()
            print(inst.id)
            inst.save()
        except Exception:
            print("Not found")
            return

    def do_show(self, arg):
        BaseModel.storage.reload()
        if len(arg) == 0:
            print("Enter a name")
            return
        arg_list = arg.split()
        try:
            inst = eval(arg_list[0])
        except Exception:
            print("Nothiing found")
            return
        if len(arg_list) == 1:
            print("Id not found")
            return
        elif len(arg_list) > 1:
            key = arg_list[0] + "." + arg_list[1]
            if key in BaseModel.storage.all():
                print(BaseModel.storage.all()[key])
            else:
                print("Nothing found")
                return

    def do_destroy(self, arg):
        if len(arg) == 0:
            print("Further info required")
            return
        arg_list = arg.split()
        try:
            inst = eval(arg_list[0])
        except Exception:
            print("Nothing found")
            return
        if len(arg_list) == 1:
            print("Id not found")
            return
        elif len(arg_list) > 1:
            key = arg_list[0] + "." + arg_list[1]
            if key in BaseModel.storage.all():
                BaseModel.storage.all().pop(key)
                BaseModel.storage.save()
            else:
                print("Nothing found")
                return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
