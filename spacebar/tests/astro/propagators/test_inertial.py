import unittest
import unittest.mock as mk

import matplotlib.pyplot as plt
from spacebar.time.utc import UTC
from spacebar.astro.propagators.inertial import TwoBody
from spacebar.math.linalg import Vector3D


class TestTwoBody(unittest.TestCase):

    START_EPOCH = UTC("Mar 04 2022 04:42:42.000")
    END_EPOCH = UTC("Mar 05 2022 04:42:42.000")
    START_POSITION = Vector3D(42164, 0, 0)
    START_VELOCITY = Vector3D(0, 3.075, 0)
    END_POSITION = Vector3D(42164, 0, 0)

    @mk.patch("matplotlib.pyplot.show")
    def test_get_state_at_epoch(self, mock_show):
        """
        Test to TwoBody propagation
        """
        tb = TwoBody(self.START_EPOCH, self.START_POSITION, self.START_VELOCITY)
        x = []
        y = []
        for t in range(144):
            pep = self.START_EPOCH.plus_seconds(t * 600)
            _, pos, _ = tb.get_state_at_epoch(pep)
            x.append(pos.x)
            y.append(pos.y)

        plt.plot(x, y)
        plt.show()
