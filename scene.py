

class Scene:

    def __init__(self, camera, objects, lights, width, height) -> None:
        self.camera = camera
        self.objects = objects
        self.lights = lights
        self.width = width
        self.height = height