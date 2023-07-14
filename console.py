#!/usr/bin/python3
"""This is the entry point for the command line"""

import cmd
from models import storage


class HBNBCommand(cmd.Cmd):
    """This is the entry point (class for the command line  interpreter)"""
    prompt = '(hbnb) '

    def do_quit(self, line):
        """Quit the command"""
        return True

    def do_EOF(self, line):
        """The EOF implementation"""
        print()

    def checkInput(self, line):
        if line == "" or line is None:
            print("** class name missing **")
            return False, None, None
        else:
            words = line.split(' ')
            if words[0] not in storage.avClasses():
                print("** class doesn't exist **")
                return False, None, None
            elif len(words) < 2:
                print("** instance id missing **")
                return False, None, None
            else:
                key = "{}.{}".format(words[0], words[1])
                if key not in storage.all():
                    print("** no instance found **")
                    return False, None, None
                else:
                    return True, words[0], words[1]

    def do_create(self, line):
        """The create implementation"""

        if line == "" or line is None:
            print("** class name missing **")
        elif line not in storage.avClasses():
            print("** class doesn't exist **")
        else:
            newClass = storage.avClasses()[line]()
            newClass.save()
            print(newClass.id)

    def do_show(self, line):
        """The show method"""

        success, model, id = self.checkInput(line)
        if success:
            print(storage.all()["{}.{}".format(model, id)])

    def do_destroy(self, line):
        """The destroy method"""

        success, model, id = self.checkInput(line)

        if success:
            del storage.all()["{}.{}".format(model, id)]
            storage.save()

    def do_all(self, line):
        """Print all objects in the database"""
        if len(line) == 0:
            print([str(v) for k, v in storage.all().items()])
        else:
            if line.split(" ")[0] in storage.avClasses():
                print([str(v) for k, v in storage.all().items() if k.split(".")[0] == line.split(" ")[0]])
            else:
                print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
