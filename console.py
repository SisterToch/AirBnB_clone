#!/usr/bin/python3

import cmd
from models.base_model import BaseModel
from models import storage

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
            print ("** class name is missing **")
            return
        try:
            latest_inst = eval(arg)()
            latest_inst.save()
            print(latest_inst.id)
        except NameError:
            print("** class doesnt exist **")

    def do_destroy(self, arg):
        destroyed = arg.split(" ")
        if not arg:
            print("** class name missing **")
            return
        elif destroyed[0] not in globals():
            print("** class doesnt exist **")
        elif len(destroyed) < 2:
            print("** instance id is missing **")
        else:
            objs = storage.all()
            objectkey = f"{destroyed[0]}.{destroyed[1]}"
        if objectkey in objs:
            del objs[objectkey]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        destroyed = destroyed.split()
        objs = storage.all()
        if not arg:
            print([str(obj) for obj in objs.values()])
        elif destroyed[0] not in globals():
            print("** class doesnt exist **")
        else:
            print([str(obj) for key, obj in objs.items() if key.startswith(objs[0])])



if __name__ == '__main__':
    HBNBCommand().cmdloop()
