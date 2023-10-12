#!/usr/bin/python3

import cmd

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """exits program"""
        return True

    def do_EOF(self, arg):
        """end of file"""
        print()
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
