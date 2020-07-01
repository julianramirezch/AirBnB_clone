#!/usr/bin/python3
"""Console command."""
import cmd
import sys
import json
import sys
import models
import shlex
from models.base_model import BaseModel
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    """Command console class."""

    my_dict = {'BaseModel': BaseModel, 'User': User, 'City': City,
               'Place': Place, 'Amenity': Amenity, 'State': State,
               'Review': Review}

    prompt = '(hbnb) '
    file = None

    def do_EOF(self, line):
        """Quit command to exit the program"""
        return True

    def do_quit(self, argv):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """Pass next line."""
        pass

    def do_create(self, argv):
        """Create object."""
        if not argv:
            print("** class name missing **")
            return
        argv_list = argv.split()
        try:
            new = self.my_dict[argv]()
            print(new.id)
            new.save()
        except Exception:
            print("** class doesn't exist **")
            return

    def do_show(self, argv):
        """Show object."""
        models.storage.reload()
        if not argv:
            print("** class name missing **")
            return
        argv_list = argv.split()
        if argv and len(argv_list) == 2:
            if argv_list[0] in self.my_dict.keys():
                test = False
                for key, value in storage.all().items():
                    if key == argv_list[0] + '.' + argv_list[1]:
                        test = True
                        print(value)
                        break
                if test is not True:
                    print('** no instance found **')
            else:
                print('** class doesn\'t exist **')
        elif argv and len(argv_list) == 1:
            if argv_list[0] in self.my_dict.keys():
                print('** instance id missing **')
            else:
                print('** class doesn\'t exist **')
        elif len(argv_list) < 1:
            print('** class name missing **')

    def do_destroy(self, argv):
        """Destroy object."""
        if not argv:
            print("** class name missing **")
            return
        argv_list = argv.split()
        try:
            y = eval(argv_list[0])
        except Exception:
            print("** class doesn't exist **")
            return
        if len(argv_list) == 1:
            print("** instance id missing **")
            return
        elif len(argv_list) > 1:
            key = argv_list[0] + "." + argv_list[1]
            if key in models.storage.all():
                models.storage.all().pop(key)
                models.storage.save()
            else:
                print("** no instance found **")
                return

    def do_all(self, argv):
        """ Show all."""
        models.storage.reload()
        if len(argv) < 1:
            va_list = []
            for value in models.storage.all().values():
                va_list.append(str(value))
            if not va_list:
                return
            print(va_list)
        else:
            tok = argv.split(" ")
            if tok[0] not in self.my_dict.keys():
                print("** class doesn't exist **")
            elif tok[0] in self.my_dict.keys():
                va_list = []
                for value in models.storage.all().values():
                    if tok[0] in value.__class__.__name__:
                        va_list.append(str(value))
                if not va_list:
                    return
                print(va_list)

    def do_update(self, argv):
        """ Update Instance."""
        models.storage.reload()
        if len(argv) == 0:
            print("** class name missing **")
            return
        else:
            ar_sp = shlex.split(argv)
            if ar_sp[0] not in self.my_dict.keys():
                print("** class doesn't exist **")
                return
            if ar_sp[0] in self.my_dict.keys() and len(ar_sp) < 2:
                print("** instance id missing **")
                return
            temp = ar_sp[0] + '.' + ar_sp[1]
            if temp in models.storage.all():
                new = models.storage.all()[temp].__dict__
                if len(ar_sp) < 3:
                    print("** attribute name missing **")
                elif len(ar_sp) < 4:
                    print("** value missing **")
                else:
                    i = ar_sp[2]
                    try:
                        attr = type(new[i])
                        value = attr(ar_sp[3])
                    except KeyError:
                        value = ar_sp[3]
                    new[i] = value
                    models.storage.save()
            else:
                print("** no instance found **")

    def do_count(self, argv):
        """ Count Instances """
        ins_dic = models.storage.all()
        cls_list = []
        for key, value in ins_dic.items():
            cls_list.append(value.to_dict()['__class__'])
        print(cls_list.count(argv))

    def precmd(self, line):
        """ Return the value that is used as the command"""
        if '.' in line and '(' in line and ')' in line:
            l_split = line.split('.')
            s_split = l_split[1].split('(')
            t_split = s_split[1].split(')')
            f_split = t_split[0].split("\"")
            if len(f_split) == 3:
                line = '{} {} {}'.format(s_split[0], l_split[0], f_split[1])
            else:
                line = '{} {}'.format(s_split[0], l_split[0])
        return line


if __name__ == '__main__':
    HBNBCommand().cmdloop()
