import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test cases for Square class"""

    def test_attributes(self):
        """Test attributes of Square class"""
        s1 = Square(10)
        self.assertEqual(s1.width, 10)
        self.assertEqual(s1.height, 10)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)

        s2 = Square(5, 7, 8)
        self.assertEqual(s2.width, 5)
        self.assertEqual(s2.height, 5)
        self.assertEqual(s2.x, 7)
        self.assertEqual(s2.y, 8)

    def test_validation(self):
        """Test validation of Square class"""
        with self.assertRaises(TypeError):
            s = Square("10")

        with self.assertRaises(ValueError):
            s = Square(-10)

        with self.assertRaises(TypeError):
            s = Square(10, "0")

        with self.assertRaises(ValueError):
            s = Square(10, -1)

        with self.assertRaises(TypeError):
            s = Square(10, 0, "0")

        with self.assertRaises(ValueError):
            s = Square(10, 0, -1)

    def test_size_property(self):
        """Test size property of Square class"""
        s1 = Square(10)
        self.assertEqual(s1.size, 10)

        s2 = Square(5)
        s2.size = 6
        self.assertEqual(s2.width, 6)
        self.assertEqual(s2.height, 6)

    def test_update_method(self):
        """Test update method of Square class"""
        s1 = Square(5)
        s1.update(89)
        self.assertEqual(s1.id, 89)

        s2 = Square(5)
        s2.update(89, 2)
        self.assertEqual(s2.id, 89)
        self.assertEqual(s2.size, 2)

        s3 = Square(5)
        s3.update(89, 2, 3)
        self.assertEqual(s3.id, 89)
        self.assertEqual(s3.size, 2)
        self.assertEqual(s3.x, 3)

        s4 = Square(5)
        s4.update(89, 2, 3, 4)
        self.assertEqual(s4.id, 89)
        self.assertEqual(s4.size, 2)
        self.assertEqual(s4.x, 3)
        self.assertEqual(s4.y, 4)

    def test_to_dictionary_method(self):
        """Test to_dictionary method of Square class"""
        s1 = Square(10, 2, 1, 9)
        d1 = {"id": 9, "size": 10, "x": 2, "y": 1}
        d2 = s1.to_dictionary()
        self.assertDictEqual(d1, d2)


if __name__ == "__main__":
    unittest.main()
