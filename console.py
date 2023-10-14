#!/usr/bin/python3

import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """exits program"""
        return True

    def do_EOF(self, arg):
        """end of file"""
        print()
        return True

    def do_create(self, arg):
        """instance of basemodel, saves it"""
        if not arg:
            print("** class name is missing **")
            return
        try:
            latest_inst = eval(arg)()
            latest_inst.save()
            print(latest_inst.id)
        except NameError:
            print("** class doesnt exist **")

    def do_show(self, arg):
        """string representation printout"""
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
        key = Argz[0] + '.' + Argz[1]
        objects = storage.all()
        if key in objects:
            print(objects[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        lists = arg.split(" ")
        if not lists:
            print("** class name missing **")
            return
        elif lists[0] not in globals():
            print("** class doesnt exist **")
        elif len(lists) < 2:
            print("** instance id is missing **")
        else:
            objs = storage.all()
            objectkey = f"{lists[0]}.{lists[1]}"
        if objectkey in objs:
            del objs[objectkey]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        lists = arg.split()
        objs = storage.all()
        if not arg:
            print([str(obj) for obj in objs.values()])
        elif lists[0] not in globals():
            print("** class doesnt exist **")
        else:
            print([str(obj) for key, obj in objs.items() if key.startswith(lists[0])])

    def do_update(self, arg):
        """updates based on class name & id for each instance"""
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
            objectkey = f"{update[0]}.{update[1]}"
            obj = objs.get(objectkey, None)
            if obj is None:
                print("** no instance found **")
            else:
                setattr(obj, args[2], args[3])
                obj.save()

    def emptyline(self):
        "overwrite to repeat last cmd"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
