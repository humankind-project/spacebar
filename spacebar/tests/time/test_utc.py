import unittest

from spacebar.time.utc import UTC


class TestVector3D(unittest.TestCase):

    EPOCH_AS_STRING = "Mar 04 2022 04:42:42.000"

    def test_utc(self):
        """
        Test to UTC object creation and timestamp conversion
        """
        utc = UTC(self.EPOCH_AS_STRING)
        self.assertAlmostEqual(1646368962, utc.timestamp, 7)

    def test_plus_seconds(self):
        """
        Test the ability to time to a UTC object
        """
        utc = UTC(self.EPOCH_AS_STRING)
        utc2 = utc.plus_seconds(34)
        self.assertAlmostEqual(1646368996, utc2.timestamp, 7)
        self.assertEqual("Mar 04 2022 04:43:16.000000", utc2.to_string())
