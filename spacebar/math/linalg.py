from audioop import mul
from math import sqrt

class Vector3D:

    def __init__(self, x:float, y:float, z:float) -> None:
        """
        Class used to represent three-dimensional vectors and perform basic 
        linear algebra.  This class will most often be used to represent a 
        position or velocity
        """

        self.x = x
        self.y = y
        self.z = z

    def plus(self, vec_to_add:"Vector3D") -> "Vector3D":
        """
        Method used to add the elements of the calling vector to the argument
        vector
        """

        return Vector3D(
            self.x + vec_to_add.x, 
            self.y + vec_to_add.y,
            self.z + vec_to_add.z
        )

    def minus(self, vec_to_subtract:"Vector3D") -> "Vector3D":
        """
        Method used to subtract the elements of the argument vector from the
        elements of the calling vector
        """

        return Vector3D(
            self.x - vec_to_subtract.x, 
            self.y - vec_to_subtract.y,
            self.z - vec_to_subtract.z
        )

    def dot(self, vec_to_dot:"Vector3D") -> "Vector3D":
        """
        Method used to get the dot product of the calling vector and the 
        argument vector
        """

        return self.x*vec_to_dot.x + self.y*vec_to_dot.y + self.z*vec_to_dot.z

    def cross(self, vec_to_cross:"Vector3D") -> "Vector3D":
        """
        Method used to get the cross product of the calling vector and the
        argument vector.  Order matters here, the format is self.cross(vec)
        is equivalent to self X vec
        """

        return Vector3D(
            self.y*vec_to_cross.z - self.z*vec_to_cross.y,
            self.z*vec_to_cross.x - self.x*vec_to_cross.z,
            self.x*vec_to_cross.y - self.y*vec_to_cross.x
        )

    def normalize(self) -> "Vector3D":
        """
        Method used to get the unit vector for the calling vector
        """
        mag = self.magnitude()
        return Vector3D(self.x/mag, self.y/mag, self.z/mag)
        

    def magnitude(self) -> float:
        """
        Method used to get the length of the calling vector
        """
        return sqrt(self.x**2 + self.y**2 + self.z**2)

    def scale(self, multiple:float) -> "Vector3D":
        """
        Method used to scale each element by the specified multiple
        """
        return Vector3D(self.x*multiple, self.y*multiple, self.z*multiple)