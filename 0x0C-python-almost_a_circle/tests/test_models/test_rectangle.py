import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for Rectangle class"""

    def test_attributes(self):
        """Test attributes of Rectangle class"""
        r1 = Rectangle(10, 20)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 20)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

        r2 = Rectangle(5, 6, 7, 8)
        self.assertEqual(r2.width, 5)
        self.assertEqual(r2.height, 6)
        self.assertEqual(r2.x, 7)
        self.assertEqual(r2.y, 8)

    def test_validation(self):
        """Test validation of Rectangle class"""
        with self.assertRaises(TypeError):
            r = Rectangle("10", 20)

        with self.assertRaises(ValueError):
            r = Rectangle(-10, 20)

        with self.assertRaises(TypeError):
            r = Rectangle(10, "20")

        with self.assertRaises(ValueError):
            r = Rectangle(10, -20)

        with self.assertRaises(TypeError):
            r = Rectangle(10, 20, "0")

        with self.assertRaises(ValueError):
            r = Rectangle(10, 20, -1)

        with self.assertRaises(TypeError):
            r = Rectangle(10, 20, 0, "0")

        with self.assertRaises(ValueError):
            r = Rectangle(10, 20, 0, -1)

    def test_update(self):
        """Test update method of Rectangle class"""
        r1 = Rectangle(10, 20)
        r1.update(12)
        self.assertEqual(r1.id, 12)

        r2 = Rectangle(5, 6)
        r2.update(7, 8)
        self.assertEqual(r2.id, 7)
        self.assertEqual(r2.width, 8)

        r3 = Rectangle(5, 6)
        r3.update(id=9)
        self.assertEqual(r3.id, 9)

        r4 = Rectangle(5, 6)
        r4.update(width=10, height=11)
        self.assertEqual(r4.width, 10)
        self.assertEqual(r4.height, 11)

        r5 = Rectangle(5, 6)
        r5.update(12, 13, x=14)
        self.assertEqual(r5.id, 12)
        self.assertEqual(r5.width, 13)
        self.assertEqual(r5.x, 14)


if __name__ == '__main__':
    unittest.main()
