import typing

from copy import deepcopy
from math import cos, sin, sqrt

from spacebar.astro.bodies import Earth
from spacebar.time.utc import UTC
from spacebar.math.linalg import Vector3D
from spacebar.astro.orbit.elements import ClassicalElements

class TwoBody:

    def __init__(self, epoch:UTC, pos:Vector3D, vel:Vector3D) -> None:
        """Class used to model basic propagation
        
        Note:
            Units are in kilometers and kilometers per second

        Args:
            epoch:      time of initial state validity
            pos:        ECI position of the satellite at epoch
            vel:        ECI velocity of the satellite at epoch
            
        Returns:
            None
            
        """
        self.epoch0 = deepcopy(epoch)
        self.position0 = deepcopy(pos)
        self.velocity0 = deepcopy(vel)

    def get_state_at_epoch(
        self, next_epoch:UTC
    ) -> typing.Tuple[UTC, Vector3D, Vector3D]:
        """get future state of model
        
        Args:
            next_epoch:     desired time of next state
            
        Returns:
            new epoch, position, and velocity 
            """

        #Get the time difference in seconds
        t = next_epoch.timestamp - self.epoch0.timestamp

        #Save the COEs of the given state vector
        coes = ClassicalElements.from_position_and_velocity(
            self.position0, 
            self.velocity0
        )

        #Get mean anomaly after delta t (Equation 2.37)
        ma = coes.mean_anomaly + coes.get_mean_motion()*t

        #Get P and Q vectors
        p = coes.get_perigee_vector()
        q = coes.get_semi_latis_rectum_vector()

        #Solve eccentric anomaly
        e = coes.eccentricity
        en = ClassicalElements.equation_to_eccentric_anomaly(ma, e)

        #Solve position using equation 2.43
        a = coes.semi_major_axis
        pScaled = p.scale(a*(cos(en) - e))
        qScaled = q.scale(a*sqrt(1-e*e)*sin(en))
        pos = pScaled.plus(qScaled)

        #Solve velocity using equation 2.44
        pScaled = p.scale(-sin(en))
        qScaled = q.scale(sqrt(1-e*e)*cos(en))
        multiple = sqrt(Earth.mu*a)/self.position0.magnitude()
        vel = pScaled.plus(qScaled).scale(multiple)

        return next_epoch, pos, vel
