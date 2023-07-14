#!/usr/bin/python3
"""Defines unittests for models/base_model.py
"""


import unittest
from datetime import datetime
from time import sleep
import os
from models.base_model import BaseModel
import models

class TestBaseModel(unittest.TestCase):
    """
    defines unittest for the BaseModel.py models
    """

    def setUp(self):
        """
        sets up the test methods
        """
        pass

    def tearDown(self):
        """
        tears down the test methods
        """
        pass

    def test_bm_instantiates(self):
        """
        tests instance of BaseModel
        """
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_1_IsInstance(self):
        """
        tests the object is instance of the BaseModel
        """
        b1 = BaseModel()
        self.assertIsInstance(b1, BaseModel)
        self.assertTrue(issubclass(type(b1), BaseModel))
        
    def test_2_id(self):
        """
        tests the id if:
            id attribute type
            is a unique id through comparison
        """
        b1 = BaseModel()
        b2 = BaseModel()

        self.assertTrue(hasattr(b1, "id"))
        self.assertNotEqual(b1.id, b2.id)

    def test_id_is_public(self):
        """
        checks id is public
        """
        self.assertEqual(str, type(BaseModel().id))

    def test_IdType(self):
        """
        Test the id attribute type
        """
        b1 = BaseModel()
        self.assertEqual(type(b1.id), str)

    def test_uniq_id(self):
        """
        Tests for unique user ids
        """
        b = [BaseModel().id for i in range(1000)]
        self.assertEqual(len(set(b)), len(b))

    def test_Created_at(self):
        """
        Checks `created_at` attribute existence
        """
        b1 = BaseModel()
        self.assertTrue(hasattr(b1, "created_at"))

    def test_created_at_is_public_datetime(self):
        """
        checks datetime publicity for created_at
        """
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_Created_atInstance(self):
        """
        Checks the created_at attribute's type
        """
        b1 = BaseModel()
        self.assertIsInstance(b1.created_at, datetime)

    def test_two_models_different_created_at(self):
        """
        tests models created if they are different
        """
        b1 = BaseModel()
        sleep(0.07)
        b2 = BaseModel()
        self.assertLess(b1.created_at, b2.created_at)

    def test_Updated_at(self):
        """
        Checks `updated_at` attribute existence
        """
        b1 = BaseModel()
        self.assertTrue(hasattr(b1, "updated_at"))

    def test_updated_at_is_public_datetime(self):
        """
        checks datetime publicity for updated_at
        """
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_Updated_atInstance(self):
        """
        Check the updated_at attribute type
        """
        b1 = BaseModel()
        self.assertIsInstance(b1.updated_at, datetime)

    def test_two_models_different_updated_at(self):
        """
        tests tow modules updated_at
        """
        b1 = BaseModel()
        sleep(0.07)
        b2 = BaseModel()
        self.assertLess(b1.updated_at, b2.updated_at)

    def test_str(self):
        """
        test that the str method output
        """
        b = BaseModel()
        string = "[BaseModel] ({}) {}".format(b.id, b.__dict__)
        self.assertEqual(string, str(b))

    def test_all_str(self):
        """
        tests all __str__ method
        """
        d_t = datetime.today()
        d_r = repr(d_t)
        b = BaseModel()
        b.id = "645312"
        b.created_at = b.updated_at = d_t
        b_s = b.__str__()
        self.assertIn("[BaseModel] (645312)", b_s)
        self.assertIn("'id': '645312'", b_s)
        self.assertIn("'created_at': " + d_r, b_s)
        self.assertIn("'updated_at': " + d_r, b_s)

    def test_str_return(self):
        """
        tests the return value of __str__ method
        """
        b = BaseModel()
        bm = "[{}] ({}) {}".format("BaseModel", b.id, str(b.__dict__))
        self.assertEqual(str(b), bm)

    def test_args_Unused(self):
        """
        tests args unused
        """
        b = BaseModel(None)
        self.assertNotIn(None, b.__dict__.values())

    def test_None_kwargs(self):
        """
        tests TypeError
        """
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_kwargs(self):
        """
        tests key word args
        """
        d = datetime.today()
        d_iso = d.isoformat()
        b = BaseModel(id="367", created_at=d_iso, updated_at=d_iso)
        self.assertEqual(b.id, "367")
        self.assertEqual(b.created_at, d)
        self.assertEqual(b.updated_at, d)

    def test_with_args_and_kwargs(self):
        """
        tests args and kwargs
        """
        d = datetime.today()
        d_iso = d.isoformat()
        b = BaseModel("11", id="367", created_at=d_iso, updated_at=d_iso)
        self.assertEqual(b.id, "367")
        self.assertEqual(b.created_at, d)
        self.assertEqual(b.updated_at, d)

class TestBaseModel_to_dict(unittest.TestCase):
    """
    Unittest for testing to_dict method of the BaseModel class
    """

    def test_to_dict_present(self):
        """
        checks if the class is present
        """
        b1 = BaseModel()
        dic = b1.to_dict()
        self.assertNotEqual(dic, b1.__dict__)

    def test_to_dict_type(self):
        """
        checks the type dict
        """
        b = BaseModel()
        self.assertTrue(dict, type(b.to_dict()))

    def test_to_dict_correct_keys(self):
        """
        tests for to_dict correct keys
        """
        b = BaseModel()
        self.assertIn("id", b.to_dict())
        self.assertIn("created_at", b.to_dict())
        self.assertIn("updated_at", b.to_dict())
        self.assertIn("__class__", b.to_dict())

    def test_att_ISO_format(self):
        """
	tests the iso formt of datetime attribute
	"""
        b1 = BaseModel()
        dic = b1.to_dict()
        self.assertEqual(type(dic['created_at']), str)
        self.assertEqual(type(dic['updated_at']), str)

    def test_to_dict_contains_attributes(self):
        """
        checks for attributes added
        """
        b = BaseModel()
        b.name = "My First Model"
        b.my_number = 89
        self.assertIn("name", b.to_dict())
        self.assertIn("my_number", b.to_dict())

    def test_to_dict_with_arg(self):
        """
        tests id to_dict has args
        """
        b1 = BaseModel()
        with self.assertRaises(TypeError):
            b1.to_dict(None)

    def test_to_dict_created_at(self):
        """
        checks the to_dict if is created_at
        """
        b = BaseModel()
        bm = b.to_dict()
        self.assertEqual(str, type(bm["created_at"]))

    def test_to_dict_updated_at(self):
        """
        tests to_dict updated_at
        """
        b = BaseModel()
        bm = b.to_dict()
        self.assertEqual(str, type(bm["updated_at"]))

    def test_to_dict(self):
        """
        unittest for to_dict
        """
        dt = datetime.today()
        b = BaseModel()
        b.id = "645312"
        b.created_at = b.updated_at = dt
        todict = {
            "id": "645312",
            "created_at": dt.isoformat(),
            "updated_at": dt.isoformat(),
            "__class__": "BaseModel"
        }
        self.assertDictEqual(b.to_dict(), todict)

    def test_to_dict_dict(self):
        """
        unittest for to_dict
        """
        b = BaseModel()
        self.assertNotEqual(b.to_dict(), b.__dict__)

class TestBaseModel_Save(unittest.TestCase):
    """
    Unittest for testing the save method
    """

    def test_save_present(self):
        """
        Tests the instance save()
        """
        b = BaseModel()
        Update_at = b.updated_at
        b.save()
        self.assertLess(Update_at, b.updated_at)

    def test_save_arg(self):
        """
        raises error
        """
        b = BaseModel()
        with self.assertRaises(TypeError):
            b.save(None)

    def test_one_save(self):
        """
        tests one save method
        """
        b = BaseModel()
        sleep(0.05)
        one_updated_at = b.updated_at
        b.save()
        self.assertLess(one_updated_at, b.updated_at)

    def test_mul_saves(self):
        """
        tests multiple save method
        """
        b = BaseModel()
        one_updated_at = b.updated_at
        b.save()
        two_updated_at = b.updated_at
        self.assertLess(one_updated_at, two_updated_at)
        b.save()
        self.assertLess(two_updated_at, b.updated_at)


if __name__ == '__main__':
    unittest.main()
