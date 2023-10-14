import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        self.file_path = "file.json"
        self.storage = FileStorage()

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all_method_returns_dict(self):
        self.assertIsInstance(self.storage.all(), dict)

    def test_new_method_adds_object(self):
        my_model = BaseModel()
        self.storage.new(my_model)
        key = "{}.{}".format(my_model.__class__.__name__, my_model.id)
        self.assertIn(key, self.storage.all())

    def test_save_method_saves_to_file(self):
        my_model = BaseModel()
        self.storage.new(my_model)
        self.storage.save()
        self.assertTrue(os.path.exists(self.file_path))

    def test_reload_method_loads_from_file(self):
        my_model = BaseModel()
        self.storage.new(my_model)
        self.storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        key = "{}.{}".format(my_model.__class__.__name__, my_model.id)
        self.assertIn(key, new_storage.all())


if __name__ == '__main__':
    unittest.main()

