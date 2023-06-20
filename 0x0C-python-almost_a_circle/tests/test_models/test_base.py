import unittest
import os
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """Test cases for Base class"""

    def setUp(self):
        """Reset __nb_objects before each test"""
        Base._Base__nb_objects = 0

    def test_id(self):
        """Test id attribute"""
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base(12)
        self.assertEqual(b3.id, 12)

        b4 = Base()
        self.assertEqual(b4.id, 3)

    def test_to_json_string(self):
        """Test to_json_string method"""
        d1 = {'id': 1, 'width': 10, 'height': 2, 'x': 1, 'y': 9}
        d2 = {'id': 2, 'width': 5, 'height': 5, 'x': 7, 'y': 8}
        json_str = Base.to_json_string([d1, d2])
        expect_str = ('[{"id": 1, "width": 10, "height": 2, "x": 1, "y": 9}, '
                      '{"id": 2, "width": 5, "height": 5, "x": 7, "y": 8}]')
        self.assertEqual(json_str, expect_str)

    def test_save_to_file(self):
        """Test save_to_file method"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), '[{"id": 1, "width": 10, '
                                       '"height": 7, "x": 2, "y": 8}, '
                                       '{"id": 2, "width": 2, '
                                       '"height": 4, "x": 0, "y": 0}]')


if __name__ == '__main__':
    unittest.main()
