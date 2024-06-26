#!/usr/bin/python3
"""
test for User class
"""
from models.user import User
import unittest
from datetime import datetime
from time import sleep


class test_for_User(unittest.TestCase):
    """
    test for unittest.TestCase
    """
    def test_for_id_type(self):
        """
        id type
        """
        self.assertEqual(str, type(User().id))

    def test_for_created_at_type(self):
        """
        created_at type
        """
        self.assertEqual(datetime, type(User().created_at))

    def test_for_updated_at_type(self):
        """
        updated_at type
        """
        self.assertEqual(datetime, type(User().updated_at))

    def test_for_two_obj_id(self):
        """
        uniq id
        """
        s = User()
        d = User()
        self.assertNotEqual(s.id, d.id)

    def test_for_str_test(self):
        """
        test for what str return
        """
        s = User()
        s.id = "hazem"
        d = datetime.today()
        s.created_at = s.updated_at = d
        self.assertIn("[User] (hazem)", s.__str__())
        self.assertIn("'id': 'hazem'", s.__str__())
        self.assertIn("'created_at': " + repr(d), s.__str__())
        self.assertIn("'updated_at': " + repr(d), s.__str__())

    def test_for_to_time(self):
        """
        testing for created_at and updated_at
        """
        s = User()
        sleep(1)
        d = User()
        self.assertGreater(d.created_at, s.created_at)
        self.assertGreater(d.updated_at, s.updated_at)

    def test_for_User(self):
        """
        test for the class
        """
        d = datetime.today()
        s = User(id="zoome", created_at=d.isoformat(),
                 updated_at=d.isoformat())
        self.assertEqual(s.id, "zoome")
        self.assertEqual(s.created_at, d)
        self.assertEqual(s.updated_at, d)

    def test_time_after_save(self):
        """
        updated_at
        """
        s = User()
        sleep(1)
        d = s.updated_at
        s.save()
        self.assertGreater(s.updated_at, d)

    def test_type_of_to_dict(self):
        """
        type of to_dict
        """
        s = User()
        self.assertEqual(dict, type(s.to_dict()))

    def test_to_dict(self):
        """
        to_dict function
        """
        s = User()
        s.name = "hazem"
        s.my_number = 20
        self.assertIn("id", s.to_dict())
        self.assertIn("created_at", s.to_dict())
        self.assertIn("updated_at", s.to_dict())
        self.assertIn("__class__", s.to_dict())
        self.assertIn("name", s.to_dict())
        self.assertIn("my_number", s.to_dict())

    def test_for_str_time(self):
        """
        convert created_at and updated_at
        """
        s = User()
        d = s.to_dict()
        self.assertEqual(str, type(d["created_at"]))
        self.assertEqual(str, type(d["updated_at"]))

    def test_for__dict__(self):
        """
        testing __dict__
        """
        s = User()
        self.assertNotEqual(s.to_dict(), s.__dict__)

    def test_for_email_type(self):
        """
        type of email
        """
        self.assertEqual(str, type(User.email))

    def test_for_pw_type(self):
        """
        password type
        """
        self.assertEqual(str, type(User.password))

    def test_for_first_name_type(self):
        """
        fn type
        """
        self.assertEqual(str, type(User.first_name))

    def test_for_last_name_type(self):
        """
        ln type
        """
        self.assertEqual(str, type(User.last_name))

    def test_for_defaul(self):
        """
        check for varible
        """
        s = User()
        self.assertEqual(s.email, "")
        self.assertEqual(s.password, "")
        self.assertEqual(s.first_name, "")
        self.assertEqual(s.last_name, "")


if __name__ == "__main__":
    unittest.main()
