#!/usr/bin/python3
"""Command interpreter to execute the hbnb console"""
import cmd
import shlex
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Hbnb console"""

    prompt = "(hbnb) "
    allowed_classes = {"BaseModel": BaseModel}

    def emptyline(self):
        """Method to cancel last command repetition"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        print('Thank you for using Turtle')
        return True

    def do_EOF(self, arg):
        """Quit command to exit the program\n"""
        print('Thank you for using Turtle')
        return True

    def do_create(self, line):
        """Creates a new instance of BaseModel.
        """
        command = self.parseline(line)[0]
        if command is None:
            print('** class name missing **')
        elif command not in self.allowed_classes:
            print("** class doesn't exist **")
        else:
            new_obj = eval(command)()
            new_obj.save()
            print(new_obj.id)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
