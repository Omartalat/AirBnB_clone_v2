#!/usr/bin/python3
"""
commands
"""
import json
import re
import cmd
from models import storage
from models.engine.file_storage import class_dict
import uuid
from datetime import datetime


class HBNBCommand(cmd.Cmd):
    """
    HBNB comands
    """
    prompt = "(hbnb) "

    def default(self, arg):
        """Default
        """
        params_pattern = r"""^"([^"]+)"(?:,\s*(?:"([^"]+)"|
        (\{[^}]+\}))(?:,\s*(?:("?[^"]+"?)))?)?"""
        m_dict_pattern = r'"[^"]+"\s*,\s*{[^}]+}'
        s_dict_pattern = r',\s+(?={)'
        s_str_pattern = r',\s*'
        cmd_arg = re.match(r"^([A-Za-z]+)\.([a-z]+)\(([^(]*)\)", arg)
        if not cmd_arg:
            print("*** Unknown syntax: {}".format(arg))
            return
        cmd_arg = re.split(r"^([A-Za-z]+)\.([a-z]+)\(([^(]*)\)", arg)
        cls_name, cmd_method, method_param = cmd_arg[1], cmd_arg[2], cmd_arg[3]
        method_param_str = "".join(method_param)
        params = re.match(params_pattern, method_param_str)
        cmd_str = "".join([cls_name])
        if params:
            cmd_str = cmd_str + " " + method_param_str
        if cmd_method == 'all':
            return self.do_all(cmd_str)

        elif cmd_method == 'count':
            return self.do_count(cmd_str)

        elif cmd_method == 'show':
            return self.do_show(cmd_str.replace('"', ""))

        elif cmd_method == 'destroy':
            return self.do_destroy(cmd_str.replace('"', ""))

        elif cmd_method == 'update':
            if re.match(m_dict_pattern, method_param):
                cmd_s_d = re.split(s_dict_pattern, method_param)
                cls_id = cmd_s_d[0].replace('"', "")
                cls_dict = json.loads(cmd_s_d[1].replace("'", '"'))
                for k, v in cls_dict.items():
                    cmd_full = cls_name + " " + cls_id + " " + k + " " + str(v)
                    self.do_update(cmd_full)
            else:
                cmd_s_d = re.split(s_str_pattern, method_param)
                cls_id = cmd_s_d[0].replace('"', "")
                cmd_full = ""
                if cls_name:
                    cmd_full = cls_name + " "
                if cls_id:
                    cmd_full += cls_id + " "
                if len(cmd_s_d) > 1:
                    cmd_full += cmd_s_d[1] + " "
                if len(cmd_s_d) > 2:
                    cmd_full += cmd_s_d[2] + " "
                self.do_update(cmd_full)
        else:
            print("*** Unknown syntax: {}".format(arg))

    def do_count(self, arg):
        """Count instances of class"""
        q = arg.split()
        c = 0
        for v in storage.all().values():
            if q[0] == v.__class__.__name__:
                c += 1
        print(c)

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print("")
        return True

    def emptyline(self):
        """empty line"""
        pass

    def do_create(self, arg):
        """Create a new instance with given parameters"""
        if not arg:
            print("** class name missing **")
        else:
            q = arg.split()
            class_name = q[0]
            if class_name not in class_dict:
                print("** class doesn't exist **")
            else:
                params = {}
                for param in q[1:]:
                    if '=' in param:
                        key, value = param.split('=')
                        if value.startswith('"') and value.endswith('"'):
                            value = value[1:-1].replace('_', ' ')
                        elif '.' in value:
                            try:
                                value = float(value)
                            except ValueError:
                                continue
                        else:
                            try:
                                value = int(value)
                            except ValueError:
                                continue
                        params[key] = value

                if 'id' not in params:
                    params['id'] = str(uuid.uuid4())
                if 'created_at' not in params:
                    params['created_at'] = str(datetime.now())
                if 'updated_at' not in params:
                    params['updated_at'] = str(datetime.now())

                s = class_dict[class_name](**params)
                s.save()
                print(s.id)

    def do_show(self, arg):
        """show obj"""
        q = arg.split()
        date_base = storage.all()
        b = 1
        if not arg:
            print("** class name missing **")
        elif q[0] not in class_dict.keys():
            print("** class doesn't exist **")
        elif len(q) == 1:
            print("** instance id missing **")
        else:
            for k, v in date_base.items():
                if v.id == q[1] and v.__class__.__name__ == q[0]:
                    b = 2
                    print(v)
            if b == 1:
                print("** no instance found **")

    def do_destroy(self, arg):
        """destroy"""
        q = arg.split()
        date_base = storage.all()
        b = 1
        if not arg:
            print("** class name missing **")
        elif q[0] not in class_dict.keys():
            print("** class doesn't exist **")
        elif len(q) == 1:
            print("** instance id missing **")
        else:
            for k, v in date_base.items():
                if v.id == q[1] and v.__class__.__name__ == q[0]:
                    b = 2
                    del date_base[k]
                    storage.save()
                    break
            if b == 1:
                print("** no instance found **")

    def do_all(self, arg):
        """print All"""
        q = arg.split()
        date_base = storage.all()
        if arg and q[0] not in class_dict.keys():
            print("** class doesn't exist **")
        elif arg and q[0] in class_dict.keys():
            z = []
            for v in date_base.values():
                if v.__class__.__name__ == q[0]:
                    z.append(str(v))
            print(z)
        else:
            z = []
            for v in date_base.values():
                z.append(str(v))
            print(z)

    def do_update(self, arg):
        """Update"""
        q = arg.replace('"', ' ').replace("'", ' ').split()
        date_base = storage.all()
        b = 1
        if not arg:
            print("** class name missing **")
            return
        if q[0] not in class_dict.keys():
            print("** class doesn't exist **")
            return
        if len(q) == 1:
            print("** instance id missing **")
            return
        if len(q) > 1:
            for k, v in date_base.items():
                if v.id == q[1]:
                    b = 2
            if b == 1:
                print("** no instance found **")
                return
        if len(q) == 2:
            print("** attribute name missing **")
            return
        if len(q) == 3:
            print("** value missing **")
            return
        if len(q) > 3:
            p = 1
            v = str(q[3])
            if q[3].isdigit():
                v = int(q[3])
                p = 2
            if p == 1:
                try:
                    v = float(q[3])
                except ValueError:
                    pass
            for k in date_base.values():
                if k.id == q[1]:
                    k.__dict__[q[2]] = v
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
