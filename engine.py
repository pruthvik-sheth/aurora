from image import Image
from ray import Ray
from vector import Vector
from color import Color

class RenderEngine:

    def render(self, scene):
        width = scene.width
        height = scene.height
        camera = scene.camera
        aspect_ratio = float(width) / height
        img = Image(width, height)

        def raster_to_ndc(x, y):
            ndc_x = (x + 0.5) / width
            ndc_y = (y + 0.5) / height
            return ndc_x, ndc_y
        
        def ndc_to_screen(ndc_x, ndc_y):
            scr_x = ((2 * ndc_x) - 1) * aspect_ratio
            scr_y = 1 - (2 * ndc_y)
            return scr_x, scr_y

        for pix_y in range(height):
            for pix_x in range(width):
                ndc_x, ndc_y = raster_to_ndc(pix_x, pix_y)
                scr_x, scr_y = ndc_to_screen(ndc_x, ndc_y)

                ray = Ray(camera, Vector(scr_x, scr_y, 1) - camera)
                img.set_pixel(pix_x, pix_y, self.ray_trace(ray, scene))

        return img
    
    def ray_trace(self, ray, scene):
        color = Color(0, 0, 0)

        dist_hit, object_hit = self.find_nearest(ray, scene)
        if object_hit is None:
            return color
        # Using parametric equation to find a point
        hit_pos = ray.origin + (ray.direction * dist_hit)
        obj_hit_normal = object_hit.normal_at_point(hit_pos)

        color += self.color_at(object_hit, hit_pos, obj_hit_normal, scene)
        return color

    def find_nearest(self, ray, scene):
        dist_min = None
        obj_hit = None

        for obj in scene.objects:
            dist = obj.intersects(ray)
            if dist is not None and (obj_hit is None or dist < dist_min):
                dist_min = dist
                obj_hit = obj
        return dist_min, obj_hit
    
    def color_at(self, obj_hit, hit_pos, obj_hit_normal, scene):
        # return obj_hit.material
        # return (hit_pos.normalize() * 0.5) + Vector(0.5, 0.5, 0.5)
        material = obj_hit.material
        obj_color = obj_hit.material.color
        color = material.ambient * Color.from_hex("#000000")
        # obj_color = material.color_at ???

        for light in scene.lights:
            hit_to_light = Ray(hit_pos, (light.position - hit_pos))
            # color += obj_color * material.diffuse * max(obj_hit_normal.dot_product(hit_to_light.direction), 0)
            color += obj_color * material.diffuse * max(obj_hit_normal.dot_product(light.position), 0)

        return color