#!/usr/bin/python3
"""
entry point of the command interpreter
"""
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import json
import shlex


class HBNBCommand(cmd.Cmd):
    """ Command interpreter """
    prompt = "(hbnb) "
    cls_list = ['BaseModel', 'User', 'State', 'City', 'Amenity',
                'Place', 'Review']
    cmd_list = ['create', 'show', 'destroy', 'all', 'update', 'count']

    def precmd(self, arg):
        """ modifies the parsed argument """
        if '.' in arg and '(' in arg and ')' in arg:
            c = arg.split('.')
            cmd = c[1].split('(')
            args = cmd[1].split(')')
            if c[0] in HBNBCommand.cls_list and cmd[0] in HBNBCommand.cmd_list:
                arg = cmd[0] + ' ' + c[0] + ' ' + args[0]
        return (arg)

    def do_count(self, class_name):
        """ retrieve the number of instances of a class """
        count = 0
        all_objs = storage.all()
        for key, value in all_objs.items():
            c = key.split('.')
            if c[0] == class_name:
                count += 1
        print(count)

    def help_help(self):
        """ prints help command description """
        print("Gives description of a command given")

    def emptyline(self):
        """ executes nothing when emptyline is given """
        pass

    def do_create(self, model):
        """ Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id """
        if not model:
            print("** class name missing **")
        elif model not in HBNBCommand.cls_list:
            print("** class doesn't exist **")
        else:
            d = {'BaseModel': BaseModel, 'User': User, 'City': City,
                 'Amenity': Amenity, 'Place': Place, 'Review': Review,
                 'State': State}
            mymodel = d[model]()
            print(mymodel.id)
            mymodel.save()

    def do_show(self, arg):
        """ Prints the string representation of an instance based on the class
        name and id """
        if not arg:
            print("** class name missing **")
            return
        args = arg.split(' ')

        if args[0] not in HBNBCommand.cls_list:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            for key, value in all_objs.items():
                obj_name = value.__class__.__name__
                obj_id = value.id
                if obj_name == args[0] and obj_id == args[1].strip('"'):
                    print(value)
                    return
            print("** no instance found **")

    def do_destroy(self, arg):
        """  Deletes an instance based on the class name and id
        (save the change into the JSON file) """
        if not arg:
            print("** class name missing **")
            return
        args = arg.split(' ')

        if args[0] not in HBNBCommand.cls_list:
            print("** class doesn't exist **")

        elif len(args) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            for key, value in all_objs.items():
                obj_name = value.__class__.__name__
                obj_id = value.id
                if obj_name == args[0] and obj_id == args[1].strip('"'):
                    del value
                    del storage._FileStorage__objects[key]
                    storage.save()
                    return
            print("** no instance found **")

    def do_all(self, arg):
        """ Prints all string representation of all instances based or not on
        the class name """

        args = arg.split(' ')

        if args[0] not in HBNBCommand.cls_list:
            print("** class doesn't exist **")
        else:
            all_objs = storage.all()
            instance_list = []
            for key, value in all_objs.items():
                obj_name = value.__class__.__name__
                if obj_name == args[0]:
                    instance_list.append(value.__str__())
            print(instance_list)

    def do_update(self, arg):
        """ Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file) """

        if not arg:
            print("** class name missing **")
            return
        ar = ""
        for argv in arg.split(','):
            ar += argv

        args = shlex.split(ar)

        if args[0] not in HBNBCommand.cls_list:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            for key, value in all_objs.items():
                obj_name = value.__class__.__name__
                obj_id = value.id
                if obj_name == args[0] and obj_id == args[1].strip('"'):
                    if len(args) == 2:
                        print("** attribute name missing **")
                    elif len(args) == 3:
                        print("** value missing **")
                    else:
                        setattr(value, args[2], args[3])
                        storage.save()
                    return
            print("** no instance found **")

    def do_quit(self, line):
        """ Quit command to exit the program """
        return True

    def do_EOF(self, line):
        """ EOF command to exit the program """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
