from math import sqrt

class Sphere:

    def __init__(self, center, radius, material) -> None:
        self.center = center
        self.radius = radius
        self.material = material
        
    def intersects(self, ray):
        # Based on solving the equations of ray and sphere
        sphere_to_ray = ray.origin - self.center
        a = ray.direction.dot_product(ray.direction)
        b = 2 * ray.direction.dot_product(sphere_to_ray)
        c = sphere_to_ray.dot_product(sphere_to_ray) - (self.radius * self.radius)

        discriminant = (b * b) - (4 * a * c)

        if discriminant >= 0:
            t = (- b - sqrt(discriminant)) / (2 * a)
            if t > 0:
                return t
            
        return None
    
    def normal_at_point(self, surface_point):
        return (surface_point - self.center).normalize()