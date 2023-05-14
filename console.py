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

    def do_show(self, line):
        """
        Prints the string representation of an instance
        based on the class name and id.
        """
        command = self.parseline(line)[0]
        arg = self.parseline(line)[1]
        if command is None:
            print('** class name missing **')
        elif command not in self.allowed_classes:
            print("** class doesn't exist **")
        elif arg == '':
            print('** instance id missing **')
        else:
            inst_data = models.storage.all().get(command + '.' + arg)
            if inst_data is None:
                print('** no instance found **')
            else:
                print(inst_data)

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id.
        """
        command = self.parseline(line)[0]
        arg = self.parseline(line)[1]
        if command is None:
            print('** class name missing **')
        elif command not in self.allowed_classes:
            print("** class doesn't exist **")
        elif arg == '':
            print('** instance id missing **')
        else:
            key = command + '.' + arg
            inst_data = models.storage.all().get(key)
            if inst_data is None:
                print('** no instance found **')
            else:
                del models.storage.all()[key]
                models.storage.save()

    def do_all(self, line):
        """
        Prints all string representation of all instances
        based or not on the class name.
        """
        command = self.parseline(line)[0]
        objs = storage.all()
        if command is None:
            print([str(objs[obj]) for obj in objs])
        elif command in self.allowed_classes:
            keys = objs.keys()
            print([str(objs[key]) for key in keys if key.startswith(command)])
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
