import unittest

from spacebar.astro.bodies import Earth


class TestEarth(unittest.TestCase):
    """
    Test class to validate Earth model
    """

    def test_mu(self):
        """
        Test to verify the mu value is set according to EGM96 model
        """
        self.assertAlmostEqual(398600.4415, Earth.mu)

    def test_radius(self):
        """
        Test to verify the equatorial radius is set according to EGM96 model
        """
        self.assertAlmostEqual(6378.1363, Earth.equatorial_radius)
