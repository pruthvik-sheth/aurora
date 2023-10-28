import math

class Vector:

    def __init__(self, x = 0.0, y = 0.0, z = 0.0) -> None:
        self.x = x
        self.y = y
        self.z = z

    # Dunder method
    def __str__(self) -> str:
        return f"Vector({self.x}, {self.y}, {self.z})"

    def dot_product(self, vector):
        return (self.x * vector.x) + (self.y * vector.y) + (self.z * vector.z)
    
    def magnitude(self):
        return math.sqrt(self.dot_product(vector = self))
    
    def normalize(self):
        return self / self.magnitude()
    
    def __add__(self, vector):
        return Vector(self.x + vector.x, self.y + vector.y, self.z + vector.z)
    
    def __sub__(self, vector):
        return Vector(self.x - vector.x, self.y - vector.y, self.z - vector.z)
    
    def __mul__(self, scalar):
        # Scalar(input) should not be a vector
        assert not isinstance(scalar, Vector)
        return Vector(self.x * scalar, self.y * scalar, self.z * scalar)
    
    # This method is for python. Because when there are two diff datatypes 
    # It will run this method that exists in one of the two data types
    def __rmul__(self, scalar):
        return self.__mul__(scalar)
    
    # In python3 truediv is used instead of div because it is rectified
    def __truediv__(self, scalar):
        assert not isinstance(scalar, Vector)
        return Vector(self.x / scalar, self.y / scalar, self.z / scalar)