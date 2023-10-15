#!/usr/bin/python3
"""
this is the command interpreter for the console
it works both in interactive mode and interactive mode
"""
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """this is the cmd class, the beginning of the interpreter"""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """end of file to exit the program"""
        print()
        return True

    def do_create(self, arg):
        """
        instance of basemodel, saves it
        """
        if not arg:
            print("** class name is missing **")
            return
        try:
            args = arg.split(" ")[0]

            if args not in FileStorage.cls_dict:
                print("** class doesn't exist **")
            else:
                new_inst = FileStorage.cls_dict[args]()
                new_inst.save()
                print(new_inst.id)
        except NameError:
            print("** class doesn't exist **")

    def do_help(self, arg):
        """
        lists the commands for the interpreter
        """
        cmd.Cmd.do_help(self, arg)

    def do_show(self, arg):
        """
        prints the string representation printout
        """
        Argz = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if Argz[0] not in globals():
            print("** class doesn't exist **")
            return
        if len(Argz) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(Argz[0], Argz[1])
        objects = storage.all()
        if key in objects:
            print(objects[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        this function provides the command to destroy
        """
        lists = arg.split(" ")
        if not arg:
            print("** class name missing **")
            return
        elif lists[0] not in globals():
            print("** class doesn't exist **")
        elif len(lists) < 2:
            print("** instance id is missing **")
        else:
            objs = storage.all()
            objectkey = "{}.{}".format(lists[0], lists[1])
            if objectkey in objs:
                del objs[objectkey]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        this command works to implement all functions
        """
        lists = arg.split()
        objs = storage.all()
        if not arg:
            print([str(obj) for obj in objs.values()])
        elif lists[0] not in globals():
            print("** class doesn't exist **")
        else:
            print([str(obj) for key, obj in objs.items()
                  if key.startswith(lists[0])])

    def do_update(self, arg):
        """
        updates based on class name & id for each instance
        """
        update = arg.split()
        if not update:
            print("** class name missing **")
        elif update[0] not in globals():
            print("** class doesn't exist **")
        elif len(update) < 2:
            print("** instance id missing **")
        elif len(update) < 3:
            print("** attribute name missing **")
        elif len(update) < 4:
            print("** value missing **")
        else:
            objs = storage.all()
            objectkey = "{}.{}".format(update[0], update[1])
            obj = objs.get(objectkey, None)
            if obj is None:
                print("** no instance found **")
            else:
                setattr(obj, update[2], update[3])
                obj.save()

    def emptyline(self):
        """
        this functin overwrites to repeat last cmd
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
