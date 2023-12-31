#!/usr/bin/python3
"""
It is the main
"""
import cmd
import sys
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Subclass of Cmd to create a simple command line interpreter for
    the AirBnB_clone project.
    """
    myClasses = {"BaseModel": BaseModel, "User": User, "Amenity": Amenity,
                 "City": City, "Place": Place,
                 "Review": Review, "State": State}
    prompt = '(hbnb) '

    def do_quit(self, args):
        """Enter Quit command to exit the program"""
        raise SystemExit

    def do_EOF(self, args):
        """Enter Quit program at End Of File (or ctrl+D)"""
        return True

    def emptyline(self):
        """This Overrides empty line default behavior"""
        pass

    def postloop(self):
        """This prints a newline after EOF"""
        print()

    def do_create(self, arg):
        """ This Creates a new instance of a Model"""
        if arg and arg in HBNBCommand.myClasses.keys():
            myStore = HBNBCommand.myClasses[arg]()
            myStore.save()
            print(myStore.id)
        elif not arg:
            print("** class name missing **")
        else:
            print("** class doesn't exist **")

    def do_show(self, args):
        "This Displays an object based on its class and id"""
        print(type(args))
        if args:
            args = [x.strip() for x in args.split()]
            print(args)
        if len(args) == 2:
            if args[0] in HBNBCommand.myClasses.keys():
                result = "{}.{}".format(args[0], args[1])
                if result in storage.all().keys():
                    print(storage.all()[result])
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            print("** class name missing **")

    def do_destroy(self, *args):
        """This Deletes an instance based on its class and id"""
        if len(args) == 2:
            if args[0] in HBNBCommand.myClasses:
                result = "{}.{}".format(args[0], args[1])
                if result in storage.all().keys():
                    del storage.all()[result]
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")
        elif len(args) == 1 and args[0]:
            print("** instance id missing **")
        else:
            print("** class name missing **")

    def do_all(self, name=""):
        """This Prints all instances bases on a class name"""
        if name:
            if name in HBNBCommand.myClasses.keys():
                for key, value in (storage.all()).items():
                    if name in key:
                        print(value)
            else:
                print("** class doesn't exist **")
        else:
            for value in storage.all().values():
                print(value)

    def update(self, *args):
        """This Updates object attribute"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
