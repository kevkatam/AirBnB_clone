#!/usr/bin/python3
"""
entry point of the command interpreter
"""
import cmd
"""from models.base_model import BaseModel
from models import storage"""
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ Command interpreter """
    prompt = "(hbnb) "
    class_list = ['BaseModel', 'User', 'State', 'City', 'Amenity',
                  'Place', 'Review']
    command_list = ['create', 'show', 'destroy', 'all', 'update']

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
        elif model not in HBNBCommand.class_list:
            print("** class doesn't exist **")
        else:
            dct = {'BaseModel': BaseModel}
            mymodel = dct[model]()
            print(mymodel.id)
            mymodel.save()

    def do_show(self, arg):
        """ Prints the string representation of an instance based on the class
        name and id """
        if not arg:
            print("** class name missing **")
            return
        args = arg.split(' ')

        if args[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
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

        if args[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")

        elif len(args) == 1:
            print("** instance id missing **")
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

        instance_list = []
        if args[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")
            all_objs = storage.all()
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

        args = arg.split(' ')

        if args[0] not in HBNBCommand.class_list:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            all_objs = storage.all()
            for key, value in all_onjs.items():
                obj_name = value.__class__.name__
                obj_id = value.id
                if obj_name == args[0] and obj_id == args[1].strip('"'):
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
