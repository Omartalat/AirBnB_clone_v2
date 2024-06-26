#!/usr/bin/python3
"""
test for BaseModel class
"""
from models.amenity import Amenity
import unittest
from datetime import datetime
from time import sleep


class test_for_BaseModel(unittest.TestCase):
    """
    test for unittest.TestCase
    """
    def test_for_id_type(self):
        """
        id type
        """
        self.assertEqual(str, type(Amenity().id))

    def test_for_created_at_type(self):
        """
        created_at type
        """
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_for_updated_at_type(self):
        """
        updated_at type
        """
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_for_two_obj_id(self):
        """
        uniq id
        """
        s = Amenity()
        d = Amenity()
        self.assertNotEqual(s.id, d.id)

    def test_for_str_test(self):
        """
        test for what str return
        """
        s = Amenity()
        s.id = "hazem"
        d = datetime.today()
        s.created_at = s.updated_at = d
        self.assertIn("[Amenity] (hazem)", s.__str__())
        self.assertIn("'id': 'hazem'", s.__str__())
        self.assertIn("'created_at': " + repr(d), s.__str__())
        self.assertIn("'updated_at': " + repr(d), s.__str__())

    def test_for_to_time(self):
        """
        testing for created_at and updated_at
        """
        s = Amenity()
        sleep(1)
        d = Amenity()
        self.assertGreater(d.created_at, s.created_at)
        self.assertGreater(d.updated_at, s.updated_at)

    def test_for_base_model(self):
        """
        test for the class
        """
        d = datetime.today()
        s = Amenity(id="zoome", created_at=d.isoformat(),
                    updated_at=d.isoformat())
        self.assertEqual(s.id, "zoome")
        self.assertEqual(s.created_at, d)
        self.assertEqual(s.updated_at, d)

    def test_time_after_save(self):
        """
        updated_at
        """
        s = Amenity()
        sleep(1)
        d = s.updated_at
        s.save()
        self.assertGreater(s.updated_at, d)

    def test_type_of_to_dict(self):
        """
        type of to_dict
        """
        s = Amenity()
        self.assertEqual(dict, type(s.to_dict()))

    def test_to_dict(self):
        """
        to_dict function
        """
        s = Amenity()
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
        s = Amenity()
        d = s.to_dict()
        self.assertEqual(str, type(d["created_at"]))
        self.assertEqual(str, type(d["updated_at"]))

    def test_for__dict__(self):
        """
        testing __dict__
        """
        s = Amenity()
        self.assertNotEqual(s.to_dict(), s.__dict__)

    def test_for_name_type(self):
        """
        name type
        """
        self.assertEqual(str, type(Amenity.name))

    def test_for_name_in_dict(self):
        """
        name in dict
        """
        s = Amenity()
        self.assertIn("name", dir(Amenity()))
        self.assertNotIn("name", s.__dict__)

    def test_for_default(self):
        """
        varible
        """
        s = Amenity()
        self.assertEqual(s.name, "")


if __name__ == "__main__":
    unittest.main()
