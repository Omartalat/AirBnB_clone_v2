#!/usr/bin/python3
"""
test for Review class
"""
from models.review import Review
import unittest
from datetime import datetime
from time import sleep


class test_for_Review(unittest.TestCase):
    """
    test for unittest.TestCase
    """
    def test_for_id_type(self):
        """
        id type
        """
        self.assertEqual(str, type(Review().id))

    def test_for_created_at_type(self):
        """
        created_at type
        """
        self.assertEqual(datetime, type(Review().created_at))

    def test_for_updated_at_type(self):
        """
        updated_at type
        """
        self.assertEqual(datetime, type(Review().updated_at))

    def test_for_two_obj_id(self):
        """
        uniq id
        """
        s = Review()
        d = Review()
        self.assertNotEqual(s.id, d.id)

    def test_for_str_test(self):
        """
        test for what str return
        """
        s = Review()
        s.id = "hazem"
        d = datetime.today()
        s.created_at = s.updated_at = d
        self.assertIn("[Review] (hazem)", s.__str__())
        self.assertIn("'id': 'hazem'", s.__str__())
        self.assertIn("'created_at': " + repr(d), s.__str__())
        self.assertIn("'updated_at': " + repr(d), s.__str__())

    def test_for_to_time(self):
        """
        testing for created_at and updated_at
        """
        s = Review()
        sleep(1)
        d = Review()
        self.assertGreater(d.created_at, s.created_at)
        self.assertGreater(d.updated_at, s.updated_at)

    def test_for_base_model(self):
        """
        test for the class
        """
        d = datetime.today()
        s = Review(id="zoome", created_at=d.isoformat(),
                   updated_at=d.isoformat())
        self.assertEqual(s.id, "zoome")
        self.assertEqual(s.created_at, d)
        self.assertEqual(s.updated_at, d)

    def test_time_after_save(self):
        """
        updated_at
        """
        s = Review()
        sleep(1)
        d = s.updated_at
        s.save()
        self.assertGreater(s.updated_at, d)

    def test_type_of_to_dict(self):
        """
        type of to_dict
        """
        s = Review()
        self.assertEqual(dict, type(s.to_dict()))

    def test_to_dict(self):
        """
        to_dict function
        """
        s = Review()
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
        s = Review()
        d = s.to_dict()
        self.assertEqual(str, type(d["created_at"]))
        self.assertEqual(str, type(d["updated_at"]))

    def test_for__dict__(self):
        """
        testing __dict__
        """
        s = Review()
        self.assertNotEqual(s.to_dict(), s.__dict__)

    def test_for_place_id_type(self):
        """
        place_id type
        """
        self.assertEqual(str, type(Review.place_id))

    def test_for_user_id_type(self):
        """
        user_id type
        """
        self.assertEqual(str, type(Review.user_id))

    def test_for_text_type(self):
        """
        text type
        """
        self.assertEqual(str, type(Review.text))

    def test_for_place_id_in_dict(self):
        """
        place_id in dict
        """
        s = Review()
        self.assertIn("place_id", dir(s))
        self.assertNotIn("place_id", s.__dict__)

    def test_for_user_id_in_dict(self):
        """
        user_id in dict
        """
        s = Review()
        self.assertIn("user_id", dir(s))
        self.assertNotIn("user_id", s.__dict__)

    def test_for_text_in_dict(self):
        """
        text in dict
        """
        s = Review()
        self.assertIn("text", dir(s))
        self.assertNotIn("text", s.__dict__)

    def test_for_default(self):
        """
        varible
        """
        s = Review()
        self.assertEqual(s.place_id, "")
        self.assertEqual(s.user_id, "")
        self.assertEqual(s.text, "")


if __name__ == "__main__":
    unittest.main()
