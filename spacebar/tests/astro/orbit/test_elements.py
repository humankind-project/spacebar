import unittest
from math import degrees
from spacebar.astro.orbit.elements import ClassicalElements
from spacebar.math.linalg import Vector3D


class TestClassicalElements(unittest.TestCase):
    """
    Test class to validate ClassicalElements
    """

    def test_from_position_and_velocity(self):
        """
        Test to validate the calculation of classical elements given position
        and velocity.  This test data can be found on page 49 of Satellite
        Orbits by Oliver Montenbruck and Eberhard Gill
        """
        pos = Vector3D(10000, 40000, -5000)
        vel = Vector3D(-1.5, 1, -0.1)
        coes = ClassicalElements.from_position_and_velocity(pos, vel)
        self.assertAlmostEqual(25015.181, coes.semi_major_axis, 3)
        self.assertAlmostEqual(0.7079772, coes.eccentricity, 7)
        self.assertAlmostEqual(6.971, degrees(coes.inclination), 3)
        self.assertAlmostEqual(173.290, degrees(coes.raan), 3)
        self.assertAlmostEqual(91.553, degrees(coes.arg_of_perigee), 3)
        self.assertAlmostEqual(144.225, degrees(coes.mean_anomaly), 3)
