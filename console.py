#!/usr/bin/python3

""" Command Line Interpreter """

import cmd
import json
import re
import sys

from models import *
from models import storage


class HBNBCommand(cmd.Cmd):

    prompt = '(hbnb) '

    def do_EOF(self, *args):
        """ EOF - End of File. Command to exit the program """

        print()
        return True

    def do_quit(Self, *args):
        """ Quit command to exit the program """
        
        quit()
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
