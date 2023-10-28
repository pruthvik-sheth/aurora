import unittest
from vector import Vector


class TestVectors(unittest.TestCase):
    def setUp(self) -> None:
        self.v1 = Vector(1.0, -2.0, -2.0)
        self.v2 = Vector(3.0, 6.0, 9.0)

    def test_magnitude(self):
        self.assertEqual(self.v1.magnitude(), 3)

    def test_addition(self):
        sum = self.v1 + self.v2
        self.assertEqual(sum.x, 4.0)
        self.assertEqual(sum.y, 4.0)
        self.assertEqual(sum.z, 7.0)

    def test_substraction(self):
        sub = self.v1 - self.v2
        self.assertEqual(sub.x, -2.0)
        self.assertEqual(sub.y, -8.0)
        self.assertEqual(sub.z, -11.0)

    def test_multiplication(self):
        mul = self.v1 * 2.0
        self.assertEqual(mul.x, 2.0)
        self.assertEqual(mul.y, -4.0)
        self.assertEqual(mul.z, -4.0)

if __name__ == "__main__":
    unittest.main()