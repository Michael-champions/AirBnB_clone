#!/usr/bin/python3

""" Module for testing the HBNBCommand Class """

import unittest
import cmd
import sys


class Console_Airbnb(cmd.Cmd):

    prompt = '(hbnb) '

    def do_quit(self):
        " Call quit or quit() to close the console "

        print("Logging out")
        quit()

    def do_EOF(self):
        " EOF - End of file. A signal used to indicate the end of file data "

        pass


if __name__ == "__main__":
    Console_Airbnb().cmdloop()
