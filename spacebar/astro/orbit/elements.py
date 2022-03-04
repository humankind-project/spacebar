from spacebar.astro.bodies import Earth
from spacebar.math.linalg import Vector3D
from math import atan2, sqrt, pi, sin, cos

class ClassicalElements:
    
    def __init__(
        self, sma:float, inc:float, ecc:float, raan:float, aop:float, ma:float
    ) -> None:
        """
        Basic constructor when elements are known
        """

        self.semi_major_axis = sma
        self.inclination = inc
        self.eccentricity = ecc
        self.raan = raan
        self.arg_of_perigee = aop
        self.mean_anomaly = ma

    @classmethod
    def from_position_and_velocity(
        self, pos:Vector3D, vel:Vector3D
    ) -> "ClassicalElements":
        """
        Constructor when ECI position and velocity are known.

        This method follows the procedures on pages 28-29 of Satellite Orbits
        by Oliver Monenbruck and Eberhard Gill
        """

        #Get the momentum vector from cross product of pos and vel (Eq. 2.56)
        h = pos.cross(vel)

        #Unitize the momentum vector (Eq. 2.57)
        w = h.normalize()

        #Get inc and raan (Eq. 2.58)
        inc = atan2(sqrt(w.x**2 + w.y**2), w.z)
        if inc == 0:
            raan = 0    #zero inc would create infinite raans without this
        else:
            raan = atan2(w.x, -w.y)

        #Correct for negative raan
        if raan < 0:
            raan+=2*pi

        #Solve for semi-latus rectum (Eq. 2.59)
        p = h.magnitude()**2/Earth.mu

        #Solve semi-major axis (Eq. 2.60)
        a = 1/(2/pos.magnitude() - vel.magnitude()**2/Earth.mu)

        #Solve mean motion (Eq. 2.61)
        n = sqrt(Earth.mu/a**3)

        #Solve eccentricity (Eq. 2.62)
        e = sqrt(1 - p/a)

        #Solve eccentric anomaly (Eq. 2.64)
        num = pos.dot(vel)/(a**2*n)
        den = 1 - pos.magnitude()/a
        ea = atan2(num, den)

        #Solve mean anomaly (Eq. 2.65)
        ma = ea - e*sin(ea)

        #Correct for negative mean anomaly
        if ma < 0:
            ma+=pi*2

        #Solve argument of latitude (Eq. 2.66)
        u = atan2(pos.z, -pos.x*w.y + pos.y*w.x)

        #Solve true anomaly (Eq. 2.67)
        ta = atan2(sqrt(1 - e**2)*sin(ea), cos(ea) - e)

        #Correct for negative true anomaly
        if ta < 0:
            ta+=pi*2

        #Solve argument of perigee (Eq. 2.68)
        aop = u - ta

        #Correct for negative argument of perigee
        if aop < 0:
            aop+=pi*2

        return ClassicalElements(a, inc, e, raan, aop, ma)
