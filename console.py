#!/usr/bin/python3
"""This is the entry point for the command line"""

import cmd

class HBNBCommand(cmd.Cmd):
    """This is the entry point (class for the command line  interpreter)"""
    prompt = '(hbnb) '

    def do_quit(self,line):
        """Quit the command"""
        return True

    def do_EOF(self,line):
        """The EOF implementation"""
        print()


if __name__ == '__main__':
    HBNBCommand().cmdloop()