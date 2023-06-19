import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test cases for Base class"""

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


if __name__ == '__main__':
    unittest.main()
