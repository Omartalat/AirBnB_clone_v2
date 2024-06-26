#!/usr/bin/python3
"""
test for Place class
"""
from models.place import Place
import unittest
from datetime import datetime
from time import sleep


class test_for_Place(unittest.TestCase):
    """
    test for unittest.TestCase
    """
    def test_for_id_type(self):
        """
        id type
        """
        self.assertEqual(str, type(Place().id))

    def test_for_created_at_type(self):
        """
        created_at type
        """
        self.assertEqual(datetime, type(Place().created_at))

    def test_for_updated_at_type(self):
        """
        updated_at type
        """
        self.assertEqual(datetime, type(Place().updated_at))

    def test_for_two_obj_id(self):
        """
        uniq id
        """
        s = Place()
        d = Place()
        self.assertNotEqual(s.id, d.id)

    def test_for_str_test(self):
        """
        test for what str return
        """
        s = Place()
        s.id = "hazem"
        d = datetime.today()
        s.created_at = s.updated_at = d
        self.assertIn("[Place] (hazem)", s.__str__())
        self.assertIn("'id': 'hazem'", s.__str__())
        self.assertIn("'created_at': " + repr(d), s.__str__())
        self.assertIn("'updated_at': " + repr(d), s.__str__())

    def test_for_to_time(self):
        """
        testing for created_at and updated_at
        """
        s = Place()
        sleep(1)
        d = Place()
        self.assertGreater(d.created_at, s.created_at)
        self.assertGreater(d.updated_at, s.updated_at)

    def test_for_base_model(self):
        """
        test for the class
        """
        d = datetime.today()
        s = Place(id="zoome", created_at=d.isoformat(),
                  updated_at=d.isoformat())
        self.assertEqual(s.id, "zoome")
        self.assertEqual(s.created_at, d)
        self.assertEqual(s.updated_at, d)

    def test_time_after_save(self):
        """
        updated_at
        """
        s = Place()
        sleep(1)
        d = s.updated_at
        s.save()
        self.assertGreater(s.updated_at, d)

    def test_type_of_to_dict(self):
        """
        type of to_dict
        """
        s = Place()
        self.assertEqual(dict, type(s.to_dict()))

    def test_to_dict(self):
        """
        to_dict function
        """
        s = Place()
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
        s = Place()
        d = s.to_dict()
        self.assertEqual(str, type(d["created_at"]))
        self.assertEqual(str, type(d["updated_at"]))

    def test_for__dict__(self):
        """
        testing __dict__
        """
        s = Place()
        self.assertNotEqual(s.to_dict(), s.__dict__)

    def test_for_city_id_type(self):
        """
        city_id type
        """
        self.assertEqual(str, type(Place.city_id))

    def test_for_user_id_type(self):
        """
        user_id type
        """
        self.assertEqual(str, type(Place.user_id))

    def test_for_name_type(self):
        """
        name type
        """
        self.assertEqual(str, type(Place.name))

    def test_for_description_type(self):
        """
        description type
        """
        self.assertEqual(str, type(Place.description))

    def test_for_number_rooms_type(self):
        """
        number_rooms type
        """
        self.assertEqual(int, type(Place.number_rooms))

    def test_for_number_bathrooms_type(self):
        """
        number_bathrooms type
        """
        self.assertEqual(int, type(Place.number_bathrooms))

    def test_for_max_guest_type(self):
        """
        max_guest type
        """
        self.assertEqual(int, type(Place.max_guest))

    def test_for_price_by_night_type(self):
        """
        price_by_night type
        """
        self.assertEqual(int, type(Place.price_by_night))

    def test_for_latitude_type(self):
        """
        latitude type
        """
        self.assertEqual(float, type(Place.latitude))

    def test_for_latitude_type(self):
        """
        latitude type
        """
        self.assertEqual(float, type(Place.latitude))

    def test_for_amenity_ids_type(self):
        """
        amenity_ids type
        """
        self.assertEqual(list, type(Place.amenity_ids))

    def test_for_city_id_in_dict(self):
        """
        city_id in dict
        """
        s = Place()
        self.assertIn("city_id", dir(s))
        self.assertNotIn("city_id", s.__dict__)

    def test_for_user_id_in_dict(self):
        """
        user_id in dict
        """
        s = Place()
        self.assertIn("user_id", dir(s))
        self.assertNotIn("user_id", s.__dict__)

    def test_for_name_in_dict(self):
        """
        name in dict
        """
        s = Place()
        self.assertIn("name", dir(s))
        self.assertNotIn("name", s.__dict__)

    def test_for_description_in_dict(self):
        """
        description in dict
        """
        s = Place()
        self.assertIn("description", dir(s))
        self.assertNotIn("description", s.__dict__)

    def test_for_number_rooms_in_dict(self):
        """
        number_rooms in dict
        """
        s = Place()
        self.assertIn("number_rooms", dir(s))
        self.assertNotIn("number_rooms", s.__dict__)

    def test_for_number_bathrooms_in_dict(self):
        """
        number_bathrooms in dict
        """
        s = Place()
        self.assertIn("number_bathrooms", dir(s))
        self.assertNotIn("number_bathrooms", s.__dict__)

    def test_for_max_guest_in_dict(self):
        """
        max_guest in dict
        """
        s = Place()
        self.assertIn("max_guest", dir(s))
        self.assertNotIn("max_guest", s.__dict__)

    def test_for_price_by_night_in_dict(self):
        """
        price_by_night in dict
        """
        s = Place()
        self.assertIn("price_by_night", dir(s))
        self.assertNotIn("price_by_night", s.__dict__)

    def test_for_latitude_in_dict(self):
        """
        latitude in dict
        """
        s = Place()
        self.assertIn("latitude", dir(s))
        self.assertNotIn("latitude", s.__dict__)

    def test_for_longitude_in_dict(self):
        """
        longitude in dict
        """
        s = Place()
        self.assertIn("longitude", dir(s))
        self.assertNotIn("longitude", s.__dict__)

    def test_for_amenity_ids_in_dict(self):
        """
        amenity_ids in dict
        """
        s = Place()
        self.assertIn("amenity_ids", dir(s))
        self.assertNotIn("amenity_ids", s.__dict__)

    def test_for_default(self):
        """
        varible
        """
        s = Place()
        self.assertEqual(s.city_id, "")
        self.assertEqual(s.user_id, "")
        self.assertEqual(s.name, "")
        self.assertEqual(s.description, "")
        self.assertEqual(s.number_rooms, 0)
        self.assertEqual(s.number_bathrooms, 0)
        self.assertEqual(s.max_guest, 0)
        self.assertEqual(s.price_by_night, 0)
        self.assertEqual(s.latitude, 0.0)
        self.assertEqual(s.longitude, 0.0)
        self.assertEqual(s.amenity_ids, [])


if __name__ == "__main__":
    unittest.main()
