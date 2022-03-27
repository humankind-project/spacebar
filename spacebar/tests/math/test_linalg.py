import unittest
from math import sqrt

from spacebar.math.linalg import Vector3D

class TestVector3D(unittest.TestCase):

    VECTOR_1 = Vector3D(4, 2, 42)
    VECTOR_2 = Vector3D(4, 42, 2)

    def test_plus(self):
        """
        Test to verify vector addition
        """
        answer = self.VECTOR_1.plus(self.VECTOR_2)
        self.assertAlmostEqual(8, answer.x)
        self.assertAlmostEqual(44, answer.y)
        self.assertAlmostEqual(44, answer.z)

    def test_minus(self):
        """
        Test to verify vector subtraction
        """
        answer = self.VECTOR_1.minus(self.VECTOR_2)
        self.assertAlmostEqual(0, answer.x)
        self.assertAlmostEqual(-40, answer.y)
        self.assertAlmostEqual(40, answer.z)

    def test_dot(self):
        """
        Test to verify vector dot product
        """
        answer = self.VECTOR_1.dot(self.VECTOR_2)
        self.assertAlmostEqual(184, answer)

    def test_cross(self):
        """
        Test to verify vector cross product
        """
        answer = self.VECTOR_1.cross(self.VECTOR_2)
        self.assertAlmostEqual(-1760, answer.x)
        self.assertAlmostEqual(160, answer.y)
        self.assertAlmostEqual(160, answer.z)

    def test_magnitude(self):
        """
        Test to verify the vector magnitude
        """
        self.assertAlmostEqual(2*sqrt(446), self.VECTOR_1.magnitude())

    def test_normalize(self):
        """
        Test to verify the unit vector
        """
        u = self.VECTOR_1.normalize()
        self.assertAlmostEqual(2/sqrt(446), u.x)
        self.assertAlmostEqual(1/sqrt(446), u.y)
        self.assertAlmostEqual(21/sqrt(446), u.z)

    def test_scale(self):
        """
        Test to verify the ability to scale a vector
        """
        v = self.VECTOR_1.scale(2)
        self.assertAlmostEqual(8, v.x)
        self.assertAlmostEqual(4, v.y)
        self.assertAlmostEqual(84, v.z)