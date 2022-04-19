class Earth:
    """Class used to represent Earth.

    Values are defined using EGM96 geopotential model.  Constant naming
    convention is intentionally not used since the values defined here may be
    updated in the future by introducing other geopotential models

    Attributes:
        mu:                 gravitational constant times body mass
        equatorial_radius:  measure from body center to surface along equator
    """

    mu = 3.986004415e5  # km^3/s^2
    equatorial_radius = 6378.1363  # km
