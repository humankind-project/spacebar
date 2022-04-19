from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

from spacebar.time.utc import UTC
from spacebar.math.linalg import Vector3D
from spacebar.astro.propagators.inertial import TwoBody


def run():

    # This will be used to plot your data
    ax = plt.axes(projection="3d")

    # This is your empty dataset to be populated for your plot
    x = []
    y = []
    z = []

    # This is your initial state and propagator
    epoch = UTC("Mar 06 2022 00:00:00.000")
    position = Vector3D(42164, 0, 700)
    velocity = Vector3D(0, 3.075, 0)
    propagator = TwoBody(epoch, position, velocity)

    # This is your propagation settings.  This will propagate for one day
    TEN_MINUTE_SEGMENTS_IN_DAY = 144
    TEN_MINUTES = 600

    # This is your propagation loop
    for t in range(TEN_MINUTE_SEGMENTS_IN_DAY):

        # We've used underscores here to indicate we only want position
        _, new_position, _ = propagator.get_state_at_epoch(epoch)

        # This increments the epoch by the defined stepsize
        epoch = epoch.plus_seconds(TEN_MINUTES)

        # Here we save each data point
        x.append(new_position.x)
        y.append(new_position.y)
        z.append(new_position.z)

    # Now we plot the orbit
    ax.plot(x, y, z, "maroon")

    # Now we plot an origin to represent Earth
    ax.scatter([0], [0], [0], "blue")

    # Finally we show the plot
    plt.show()


if __name__ == "__main__":
    run()
