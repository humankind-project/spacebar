from math import sqrt


class Vector3D:
    def __init__(self, x: float, y: float, z: float) -> None:
        """three-dimensional vector used for basic linear algebra

        Args:
            x:      The first component of the vector
            y:      The second component of the vector
            z:      The third component of the vector

        Returns:
            None

        """
        self.x = x
        self.y = y
        self.z = z

    def plus(self, vec_to_add: "Vector3D") -> "Vector3D":
        """Performs vector addition

        Args:
            vec_to_add:     The vector which will be added to the calling vector

        Returns:
            AVector representing element addition of self and vec_to_add

        """
        return Vector3D(self.x + vec_to_add.x, self.y + vec_to_add.y, self.z + vec_to_add.z)

    def minus(self, vec_to_subtract: "Vector3D") -> "Vector3D":
        """Performs vector subtraction

        Args:
            vec_to_subtract:    The vector which will be subtracted from self

        Returns:
            Vector representing element difference of self and vec_to_subtract

        """
        return Vector3D(
            self.x - vec_to_subtract.x,
            self.y - vec_to_subtract.y,
            self.z - vec_to_subtract.z,
        )

    def dot(self, vec_to_dot: "Vector3D") -> float:
        """Performs dot product

        Args:
            vec_to_dot:     The vector to be used in the product with self

        Returns:
            scalar value representing sum of element multiplication

        """
        return self.x * vec_to_dot.x + self.y * vec_to_dot.y + self.z * vec_to_dot.z

    def cross(self, vec_to_cross: "Vector3D") -> "Vector3D":
        """Performs cross product

        Args:
            vec_to_cross:   The vector to be used in the product with self

        Returns:
            Vector perpendicular to self and vec_to_cross

        """
        return Vector3D(
            self.y * vec_to_cross.z - self.z * vec_to_cross.y,
            self.z * vec_to_cross.x - self.x * vec_to_cross.z,
            self.x * vec_to_cross.y - self.y * vec_to_cross.x,
        )

    def normalize(self) -> "Vector3D":
        """Method used to get the unit vector for the calling vector

        Args:
            None

        Returns:
            Vector parallel to self and of length 1

        """
        mag = self.magnitude()
        return Vector3D(self.x / mag, self.y / mag, self.z / mag)

    def magnitude(self) -> float:
        """Method used to get the length of the calling vector

        Args:
            None

        Returns:
            Square root of the sum of squared components

        """
        return sqrt(self.x**2 + self.y**2 + self.z**2)

    def scale(self, multiple: float) -> "Vector3D":
        """Method used to scale each element by the specified multiple

        Args:
            multiple:   value to be multiplied across elements

        Returns:
            Vector parallel to self with a scaled magnitude
        """
        return Vector3D(self.x * multiple, self.y * multiple, self.z * multiple)
