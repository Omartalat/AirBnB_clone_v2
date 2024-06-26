#!/usr/bin/python3
"""
Defines unittests for console.py.
"""
import os
import unittest
from unittest.mock import patch
from io import StringIO
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel


class TestHBNBCommand_prompting(unittest.TestCase):
    """Unittests for prompting of the HBNB command interpreter"""

    def test_prompt_start(self):
        """Test that the prompt is set to '(hbnb) '"""
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_empty_line(self):
        """Test behavior when an empty line is entered"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", output.getvalue().strip())


class TestHBNBCommand_help(unittest.TestCase):
    """Unittests for help cmd of the HBNB command interpreter"""

    def test_help_EOF(self):
        """Test help output for the 'EOF' command"""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("help EOF")
            self.assertEqual("EOF command to exit the program",
                             output.getvalue().strip())

    def test_help_all(self):
        """Test help output for the 'all' command"""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("help all")
            self.assertEqual("print All", output.getvalue().strip())

    def test_help_count(self):
        """Test help output for the 'count' command"""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("help count")
            self.assertEqual("Count instances of class",
                             output.getvalue().strip())

    def test_help_create(self):
        """Test help output for the 'create' command"""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("help create")
            self.assertEqual("create new instance", output.getvalue().strip())

    def test_help_destroy(self):
        """Test help output for the 'destroy' command"""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("help destroy")
            self.assertEqual("destroy", output.getvalue().strip())

    def test_help_help(self):
        """Test help output for the 'help' command"""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("help help")
            self.assertEqual(
                'List available commands with "help" or \
detailed help with "help cmd".', output.getvalue().strip())

    def test_help_quit(self):
        """Test help output for the 'quit' command"""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("help quit")
            self.assertEqual("Quit command to exit the program",
                             output.getvalue().strip())

    def test_help_show(self):
        """Test help output for the 'show' command"""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("help show")
            self.assertEqual("show obj", output.getvalue().strip())

    def test_help_update(self):
        """Test help output for the 'update' command"""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("help update")
            self.assertEqual("Update", output.getvalue().strip())


class TestHBNBCommand_count(unittest.TestCase):
    """Unittests for count cmd of the HBNB command interpreter"""

    def setUp(self):
        """Set up the environment for testing count command"""
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """Tear down the environment after testing count command"""
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_count_invalid_class_name(self):
        """Test count command with an invalid class name"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("MyModel.count()"))
            self.assertEqual("0",
                             output.getvalue().strip())

    def test_count_valid_class_name(self):
        """Test count command with valid class names"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.count()"))
            self.assertEqual("1", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("User.count()"))
            self.assertEqual("1", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("State.count()"))
            self.assertEqual("1", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Place.count()"))
            self.assertEqual("1", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("City.count()"))
            self.assertEqual("1", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Amenity.count()"))
            self.assertEqual("1", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Review.count()"))
            self.assertEqual("1", output.getvalue().strip())


class TestHBNBCommand_quit(unittest.TestCase):
    """Unittests for count cmd of the HBNB command interpreter"""

    def test_quit(self):
        """Test the quit command"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("quit"))


class TestHBNBCommand_EOF(unittest.TestCase):
    """Unittests for Ctrl + d of the HBNB command interpreter"""

    def test_EOF(self):
        """Test the behavior of Ctrl + d"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("EOF"))


class TestHBNBCommand_create(unittest.TestCase):
    """Unittests for create cmd of the HBNB command interpreter"""

    def setUp(self):
        """Set up the environment for testing create command"""
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """Tear down the environment after testing create command"""
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_create_missing_class(self):
        """Test create command with missing class name"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create"))
            self.assertEqual("** class name missing **",
                             output.getvalue().strip())

    def test_create_invalid_class_name(self):
        """Test create command with invalid class name"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create MyModel"))
            self.assertEqual("** class doesn't exist **",
                             output.getvalue().strip())

    def test_create_class_user(self):
        """Test create command with 'User' class"""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create User")
            key_name = "User.{}".format(output.getvalue().strip())
            self.assertIn(key_name, storage.all().keys())

    def test_create_class_BaseModel(self):
        """Test create command with 'BaseModel' class"""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create BaseModel")
            key_name = "BaseModel.{}".format(output.getvalue().strip())
            self.assertIn(key_name, storage.all().keys())

    def test_create_class_Place(self):
        """Test create command with 'Place' class"""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            key_name = "Place.{}".format(output.getvalue().strip())
            self.assertIn(key_name, storage.all().keys())

    def test_create_class_State(self):
        """Test create command with 'State' class"""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create State")
            key_name = "State.{}".format(output.getvalue().strip())
            self.assertIn(key_name, storage.all().keys())

    def test_create_class_City(self):
        """Test create command with 'City' class"""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create City")
            key_name = "City.{}".format(output.getvalue().strip())
            self.assertIn(key_name, storage.all().keys())

    def test_create_class_Review(self):
        """Test create command with 'Review' class"""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Review")
            key_name = "Review.{}".format(output.getvalue().strip())
            self.assertIn(key_name, storage.all().keys())

    def test_create_class_Amenity(self):
        """Test create command with 'Amenity' class"""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Amenity")
            key_name = "Amenity.{}".format(output.getvalue().strip())
            self.assertIn(key_name, storage.all().keys())


class TestHBNBCommand_show(unittest.TestCase):
    """Unittests for show cmd of the HBNB command interpreter"""

    def setUp(self):
        """Set up the environment for testing show command"""
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """Tear down the environment after testing show command"""
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_show_missing_class(self):
        """Test show command with missing class name"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show"))
            self.assertEqual("** class name missing **",
                             output.getvalue().strip())

    def test_show_invalid_class_name(self):
        """Test show command with invalid class name"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show MyModel"))
            self.assertEqual("** class doesn't exist **",
                             output.getvalue().strip())

    def test_show_missing_class_id(self):
        """Test show command with missing class ID"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd('User.show()'))
            self.assertEqual("** instance id missing **",
                             output.getvalue().strip())

    def test_show_invalid_class_id(self):
        """Test show command with invalid class ID"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd('User.show("1")'))
            self.assertEqual("** no instance found **",
                             output.getvalue().strip())

    def test_show_class_user(self):
        """Test show command with class User"""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create User")
            cls_id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("all User")
            user_dict = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd('User.show("{}")'.format(cls_id))
            self.assertIn(output.getvalue().strip(), user_dict)

    def test_show_class_BaseModel(self):
        """Test show command with class BaseModel"""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create BaseModel")
            cls_id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("all BaseModel")
            user_dict = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd('BaseModel.show("{}")'.format(cls_id))
            self.assertIn(output.getvalue().strip(), user_dict)

    def test_show_class_Place(self):
        """Test show command with class Place"""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            cls_id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("all Place")
            user_dict = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd('Place.show("{}")'.format(cls_id))
            self.assertIn(output.getvalue().strip(), user_dict)

    def test_show_class_State(self):
        """Test show command with class State"""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create State")
            cls_id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("all State")
            user_dict = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd('State.show("{}")'.format(cls_id))
            self.assertIn(output.getvalue().strip(), user_dict)

    def test_show_class_City(self):
        """Test show command with class City"""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create City")
            cls_id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("all City")
            user_dict = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd('City.show("{}")'.format(cls_id))
            self.assertIn(output.getvalue().strip(), user_dict)

    def test_show_class_Amenity(self):
        """Test show command with class Amenity"""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Amenity")
            cls_id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("all Amenity")
            user_dict = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd('Amenity.show("{}")'.format(cls_id))
            self.assertIn(output.getvalue().strip(), user_dict)

    def test_show_class_Review(self):
        """Test show command with class Review"""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Review")
            cls_id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("all Review")
            user_dict = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd('Review.show("{}")'.format(cls_id))
            self.assertIn(output.getvalue().strip(), user_dict)


class TestHBNBCommand_all(unittest.TestCase):
    """Unittests for all cmd of the HBNB command interpreter"""

    def setUp(self):
        """set up test"""
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """tear down test"""
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_all_no_classes(self):
        """test no classes"""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("all User")
            self.assertEqual('[]', output.getvalue().strip())

    def test_all_invalid_classes(self):
        """test all classes"""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("all MyModel")
            self.assertEqual("** class doesn't exist **",
                             output.getvalue().strip())

    def test_all_classes_available(self):
        """test all classes"""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create User")
            HBNBCommand().onecmd("create BaseModel")
            HBNBCommand().onecmd("create Place")
            HBNBCommand().onecmd("create State")
            HBNBCommand().onecmd("create City")
            HBNBCommand().onecmd("create Amenity")
            HBNBCommand().onecmd("create Review")
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("all")
            self.assertIn("User", output.getvalue().strip())
            self.assertIn("BaseModel", output.getvalue().strip())
            self.assertIn("Place", output.getvalue().strip())
            self.assertIn("State", output.getvalue().strip())
            self.assertIn("City", output.getvalue().strip())
            self.assertIn("Amenity", output.getvalue().strip())
            self.assertIn("Review", output.getvalue().strip())

    def test_all_single_object_dot_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertFalse(HBNBCommand().onecmd("create Review"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.all()"))
            self.assertIn("BaseModel", output.getvalue().strip())
            self.assertNotIn("User", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("User.all()"))
            self.assertIn("User", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("State.all()"))
            self.assertIn("State", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("City.all()"))
            self.assertIn("City", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Amenity.all()"))
            self.assertIn("Amenity", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Place.all()"))
            self.assertIn("Place", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Review.all()"))
            self.assertIn("Review", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())


class TestHBNBCommand_destroy(unittest.TestCase):
    """Unittests for destroy cmd of the HBNB command interpreter"""

    def setUp(self):
        """Set up the environment for testing destroy command"""
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """Tear down the environment after testing destroy command"""
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_destroy_missing_class(self):
        """Test destroy command with missing class name"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy"))
            self.assertIn("** class name missing **",
                          output.getvalue().strip())

    def test_destroy_invalid_class(self):
        """Test destroy command with invalid class name"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy Omartalat"))
            self.assertIn("** class doesn't exist **",
                          output.getvalue().strip())

    def test_destroy_missing_id_1(self):
        """Test destroy command with missing instance ID"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy User"))
            self.assertIn("** instance id missing **",
                          output.getvalue().strip())

    def test_destroy_invalid_id_2(self):
        """Test destroy command with invalid instance ID"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd('User.destroy("1")'))
            self.assertIn("** no instance found **", output.getvalue().strip())

    def test_destroy_invalid_id_3(self):
        """Test destroy command with invalid instance ID"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd('BaseModel.destroy("1")'))
            self.assertIn("** no instance found **", output.getvalue().strip())

    def test_destroy_invalid_id_4(self):
        """Test destroy command with invalid instance ID"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd('Place.destroy("1")'))
            self.assertIn("** no instance found **", output.getvalue().strip())

    def test_destroy_invalid_id_5(self):
        """Test destroy command with invalid instance ID"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd('State.destroy("1")'))
            self.assertIn("** no instance found **", output.getvalue().strip())

    def test_destroy_invalid_id_6(self):
        """Test destroy command with invalid instance ID"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd('City.destroy("1")'))
            self.assertIn("** no instance found **", output.getvalue().strip())

    def test_destroy_invalid_id_7(self):
        """Test destroy command with invalid instance ID"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd('Amenity.destroy("1")'))
            self.assertIn("** no instance found **", output.getvalue().strip())

    def test_destroy_invalid_id_8(self):
        """Test destroy command with invalid instance ID"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd('Review.destroy("1")'))
            self.assertIn("** no instance found **", output.getvalue().strip())

    def test_destroy_user(self):
        """Test destroy command with 'User' class"""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd('create User')
            cls_id = output.getvalue().strip
            key_name = "User.{}".format(cls_id)
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd('User.destroy("{}")'.format(cls_id))
            self.assertNotIn(key_name, storage.all().keys())

    def test_destroy_BaseModel(self):
        """Test destroy command with 'BaseModel' class"""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd('create BaseModel')
            cls_id = output.getvalue().strip
            key_name = "BaseModel.{}".format(cls_id)
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd('BaseModel.destroy("{}")'.format(cls_id))
            self.assertNotIn(key_name, storage.all().keys())

    def test_destroy_Place(self):
        """Test destroy command with 'Place' class"""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd('create Place')
            cls_id = output.getvalue().strip
            key_name = "Place.{}".format(cls_id)
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd('Place.destroy("{}")'.format(cls_id))
            self.assertNotIn(key_name, storage.all().keys())

    def test_destroy_State(self):
        """Test destroy command with 'State' class"""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd('State User')
            cls_id = output.getvalue().strip
            key_name = "State.{}".format(cls_id)
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd('State.destroy("{}")'.format(cls_id))
            self.assertNotIn(key_name, storage.all().keys())

    def test_destroy_City(self):
        """Test destroy command with 'City' class"""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd('create City')
            cls_id = output.getvalue().strip
            key_name = "City.{}".format(cls_id)
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd('City.destroy("{}")'.format(cls_id))
            self.assertNotIn(key_name, storage.all().keys())

    def test_destroy_Amenity(self):
        """Test destroy command with 'Amenity' class"""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd('create Amenity')
            cls_id = output.getvalue().strip
            key_name = "Amenity.{}".format(cls_id)
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd('Amenity.destroy("{}")'.format(cls_id))
            self.assertNotIn(key_name, storage.all().keys())

    def test_destroy_Review(self):
        """Test destroy command with 'Review' class"""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd('create Review')
            cls_id = output.getvalue().strip
            key_name = "Review.{}".format(cls_id)
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd('Review.destroy("{}")'.format(cls_id))
            self.assertNotIn(key_name, storage.all().keys())


class TestHBNBCommand_update(unittest.TestCase):
    """Unittests for update cmd of the HBNB command interpreter"""

    def setUp(self):
        """Set up the environment for testing destroy command"""
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """Tear down the environment after testing destroy command"""
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_update_missing_class(self):
        """Test update command with missing class name"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update"))
            self.assertIn("** class name missing **",
                          output.getvalue().strip())

    def test_update_invalid_class(self):
        """Test update command with invalid class name"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update hazemali1"))
            self.assertIn("** class doesn't exist **",
                          output.getvalue().strip())

    def test_update_missing_id(self):
        """Test update command with missing instance ID"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update User"))
            self.assertIn("** instance id missing **",
                          output.getvalue().strip())

    def test_update_invalid_id(self):
        """Test update command with invalid instance ID"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd('User.update("1")'))
            self.assertIn("** no instance found **",
                          output.getvalue().strip())

    def test_update_missing_attr(self):
        """Test update command with missing attribute"""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create User")
            cls_id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(
                'User.update("{}")'.format(cls_id)))
            self.assertIn("** attribute name missing **",
                          output.getvalue().strip())

    def test_update_missing_attr(self):
        """Test update command with missing attribute"""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create User")
            cls_id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(
                'User.update("{}" , "name")'.format(cls_id)))
            self.assertIn("** value missing **",
                          output.getvalue().strip())

    def test_update_class_User(self):
        """Test update command with missing attribute"""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create User")
            cls_id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd('User.update("{}" , \
"name", "Omar")'.format(cls_id))
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd('User.show("{}")'.format(cls_id))
            inst = output.getvalue().strip()
            self.assertIn("'name': 'Omar'", inst)

    def test_update_class_BaseModel(self):
        """Test update command with missing attribute"""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create BaseModel")
            cls_id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd('BaseModel.update("{}" , \
"name", "Omar")'.format(cls_id))
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd('BaseModel.show("{}")'.format(cls_id))
            inst = output.getvalue().strip()
            self.assertIn("'name': 'Omar'", inst)

    def test_update_class_Place(self):
        """Test update command with missing attribute"""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
            cls_id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd('Place.update("{}" , \
"name", "Omar")'.format(cls_id))
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd('Place.show("{}")'.format(cls_id))
            inst = output.getvalue().strip()
            self.assertIn("'name': 'Omar'", inst)

    def test_update_class_State(self):
        """Test update command with missing attribute"""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create State")
            cls_id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd('State.update("{}" , \
"name", "Omar")'.format(cls_id))
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd('State.show("{}")'.format(cls_id))
            inst = output.getvalue().strip()
            self.assertIn("'name': 'Omar'", inst)

    def test_update_class_City(self):
        """Test update command with missing attribute"""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create City")
            cls_id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd('City.update("{}" , \
"name", "Omar")'.format(cls_id))
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd('City.show("{}")'.format(cls_id))
            inst = output.getvalue().strip()
            self.assertIn("'name': 'Omar'", inst)

    def test_update_class_Amenity(self):
        """Test update command with missing attribute"""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Amenity")
            cls_id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd('Amenity.update("{}" , \
"name", "Omar")'.format(cls_id))
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd('Amenity.show("{}")'.format(cls_id))
            inst = output.getvalue().strip()
            self.assertIn("'name': 'Omar'", inst)

    def test_update_class_Review(self):
        """Test update command with missing attribute"""
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Review")
            cls_id = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd('Review.update("{}" , \
"name", "Omar")'.format(cls_id))
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd('Review.show("{}")'.format(cls_id))
            inst = output.getvalue().strip()
            self.assertIn("'name': 'Omar'", inst)\


    def test_update_invalid_id_space(self):
        """Test update command with missing attribute"""
        correct = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update BaseModel 1"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update User 1"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update State 1"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update City 1"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update Amenity 1"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update Place 1"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update Review 1"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_update_missing_id_space(self):
        """Test update command with missing attribute"""
        correct = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update BaseModel"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update User"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update State"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update City"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update Amenity"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update Place"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("update Review"))
            self.assertEqual(correct, output.getvalue().strip())


if __name__ == "__main__":
    unittest.main()
