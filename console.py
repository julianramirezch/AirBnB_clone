#!/usr/bin/python3
"""Console command."""
import cmd
import sys
import json
import sys
import models
from models.base_model import BaseModel
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class c_c:
    """Color class."""

    lightgray = '\033[37m'
    magenta = '\033[35m'
    blue = '\033[94m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    end = '\033[0m'


class HBNBCommand(cmd.Cmd):
    """Command console class."""

    intro = c_c.magenta + 'Welcome to \'hbnb\'. Type help or \
? to list commands.\n' + c_c.end
    prompt = c_c.red + '(hbnh) ' + c_c.end
    file = None

    def do_EOF(self, arg):
        """Quit console."""
        return True

    def do_quit(self, arg):
        """Quit console."""
        return True

    def emptyline(self):
        """Pass next line."""
        pass

    def do_create(self, arg):
        """Create object."""
        if len(arg) == 0:
            print("** class name missing **")
            return
        arg_list = arg.split()
        try:
            inst = eval(arg_list[0])()
            print(inst.id)
            inst.save()
        except Exception:
            print("** class doesn't exist **")
            return

    def do_show(self, arg):
        """Show object."""
        models.storage.reload()
        if len(arg) == 0:
            print("** class name missing **")
            return
        arg_list = arg.split()
        try:
            inst = eval(arg_list[0])
        except Exception:
            print("** class doesn't exist **")
            return
        if len(arg_list) == 1:
            print("** instance id missing **")
            return
        elif len(arg_list) > 1:
            key = arg_list[0] + "." + arg_list[1]
            if key in models.storage.all():
                print(models.storage.all()[key])
            else:
                print("** no instance found **")
                return

    def do_destroy(self, arg):
        """Destroy object."""
        if len(arg) == 0:
            print("** class name missing **")
            return
        arg_list = arg.split()
        try:
            inst = eval(arg_list[0])
        except Exception:
            print("** class doesn't exist **")
            return
        if len(arg_list) == 1:
            print("** instance id missing **")
            return
        elif len(arg_list) > 1:
            key = arg_list[0] + "." + arg_list[1]
            if key in models.storage.all():
                models.storage.all().pop(key)
                models.storage.save()
            else:
                print("** no instance found **")
                return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
