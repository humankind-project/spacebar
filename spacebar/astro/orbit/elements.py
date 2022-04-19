from math import atan2, cos, pi, sin, sqrt

from spacebar.astro.bodies import Earth
from spacebar.math.linalg import Vector3D


class ClassicalElements:
    def __init__(self, sma: float, inc: float, ecc: float, raan: float, aop: float, ma: float) -> None:
        """Basic constructor when elements are known

        Note:
            All lengths are measured in kilometers, and all angles are measured
            in radians

        Args:
            sma:    semi-major axis of orbit
            inc:    angle between momentum vector and z axis
            ecc:    eccentricity of the orbit
            raan:   right ascension of ascending node
            aop:    argument of perigee
            ma:     mean anomaly

        Attributes:
            semi_major_axis:    the average radius relative to the central body
            inclination:        angle between momentum vector and z axis
            eccentricity:       measure where 0 == circular 1 == parabolic
            raan:               right ascension at which orbit becomes positive
            arg_of_perigee:     angle of raan vector and eccentricity vector
            mean_anomaly:       location angle mapped to circle

        Returns:
            None

        """
        self.semi_major_axis = sma
        self.inclination = inc
        self.eccentricity = ecc
        self.raan = raan
        self.arg_of_perigee = aop
        self.mean_anomaly = ma

    @classmethod
    def from_position_and_velocity(cls, pos: Vector3D, vel: Vector3D) -> "ClassicalElements":
        """Constructor when ECI position and velocity are known.

        This method follows the procedures on pages 28-29 of Satellite Orbits
        by Oliver Monenbruck and Eberhard Gill

        Note:
            Values are in kilometers

        Args:
            pos:    Object containing x, y, and z location of satellite
            vel:    Object containing x, y, and z velocity of satellite

        Returns:
            ClassicalElements representation of input position and velocity

        """
        # Get the momentum vector from cross product of pos and vel (Eq. 2.56)
        h = pos.cross(vel)

        # Unitize the momentum vector (Eq. 2.57)
        w = h.normalize()

        # Get inc and raan (Eq. 2.58)
        inc = atan2(sqrt(w.x**2 + w.y**2), w.z)
        if inc == 0:
            raan = 0  # zero inc would create infinite raans without this
        else:
            raan = atan2(w.x, -w.y)

        # Correct for negative raan
        if raan < 0:
            raan += 2 * pi

        # Solve for semi-latus rectum (Eq. 2.59)
        p = h.magnitude() ** 2 / Earth.mu

        # Solve semi-major axis (Eq. 2.60)
        a = 1 / (2 / pos.magnitude() - vel.magnitude() ** 2 / Earth.mu)

        # Solve mean motion (Eq. 2.61)
        n = sqrt(Earth.mu / a**3)

        # Solve eccentricity (Eq. 2.62)
        e = sqrt(1 - p / a)

        # Solve eccentric anomaly (Eq. 2.64)
        num = pos.dot(vel) / (a**2 * n)
        den = 1 - pos.magnitude() / a
        ea = atan2(num, den)

        # Solve mean anomaly (Eq. 2.65)
        ma = ea - e * sin(ea)

        # Correct for negative mean anomaly
        if ma < 0:
            ma += pi * 2

        # Solve argument of latitude (Eq. 2.66)
        u = atan2(pos.z, -pos.x * w.y + pos.y * w.x)

        # Solve true anomaly (Eq. 2.67)
        ta = atan2(sqrt(1 - e**2) * sin(ea), cos(ea) - e)

        # Correct for negative true anomaly
        if ta < 0:
            ta += pi * 2

        # Solve argument of perigee (Eq. 2.68)
        aop = u - ta

        # Correct for negative argument of perigee
        if aop < 0:
            aop += pi * 2

        return ClassicalElements(a, inc, e, raan, aop, ma)

    def get_mean_motion(self) -> float:
        """get the average orbital rate

        Follows equation 2.35 from Satellite Orbits to calculate the mean
        motion of the orbit

        Args:
            None

        Returns:
            mean orbital rate in radians per second

        """
        return sqrt(Earth.mu / self.semi_major_axis**3)

    def get_perigee_vector(self) -> Vector3D:
        """get vector pointing from central body to satellite perigee

        Follows equation 2.52 from Satellite Orbits

        Args:
            None

        Returns:
            unit vector pointing to perigee

        """
        cw = cos(self.arg_of_perigee)
        cO = cos(self.raan)
        sw = sin(self.arg_of_perigee)
        sO = sin(self.raan)
        ci = cos(self.inclination)

        x = cw * cO - sw * ci * sO
        y = cw * sO + sw * ci * cO
        z = sw * sin(self.inclination)

        return Vector3D(x, y, z).normalize()

    def get_semi_latis_rectum_vector(self) -> Vector3D:
        """get vector pointing to true anomaly of 90 degrees

        Follows equation 2.53 from satellite orbits

        Args:
            None

        Returns:
            unit vector pointing to satellite location equal to a true anomaly
            of 90 degrees

        """
        cw = cos(self.arg_of_perigee)
        cO = cos(self.raan)
        sw = sin(self.arg_of_perigee)
        sO = sin(self.raan)
        ci = cos(self.inclination)

        x = -sw * cO - cw * ci * sO
        y = -sw * sO + cw * ci * cO
        z = cw * sin(self.inclination)

        return Vector3D(x, y, z).normalize()

    @staticmethod
    def equation_to_eccentric_anomaly(mean_anom: float, ecc: float) -> float:
        """Solve eccentric anomaly given eccentricity and mean anomaly

        Follows the method found on page 24 of Satellite Orbits.

        Note:
            All angles are in radians

        Args:
            mean_anom:      mean anomaly of orbit
            ecc:            eccentricity of orbit

        Returns:
            value of eccentric anomaly

        """

        # Seed E sub i with mean anomaly
        ea_0 = mean_anom
        converged = False

        # For high eccentricities, seed E sub i with pi
        if ecc > 0.8:
            ea_0 = pi

        # Iterate until meeting tolerance
        while not converged:

            # Save the numerator and denominator separately to avoid long lines
            num = mean_anom - ea_0 + ecc * sin(ea_0)
            den = 1 - ecc * cos(ea_0)

            # Solve E sub i+1
            ea_n = ea_0 + num / den

            # Check tolerance and reseed E sub i if difference is too large
            if abs(ea_n - ea_0) < 1e-12:
                converged = True
            else:
                ea_0 = ea_n

        # Correct for negative values
        if ea_n < 0:
            ea_n += pi * 2.0

        return ea_n
