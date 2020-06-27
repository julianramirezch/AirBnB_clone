#!/usr/bin/python3
import cmd, sys

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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
