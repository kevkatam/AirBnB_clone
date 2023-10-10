#!/usr/bin/python3
"""
entry point of the command interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """ Command interpreter """
    prompt = "(hbnb) "

    def help_help(self):
        """ prints help command description """
        print("Gives description of a command given")

    def emptyline(self):
        """ executes nothing when emptyline is given """
        pass

    def do_quit(self, line):
        """ Quit command to exit the program """
        return True

    def do_EOF(self, line):
        """ EOF command to exit the program """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
