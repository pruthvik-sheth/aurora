import pygame as pg
from color import Color
from vector import Vector
from sphere import Sphere
from scene import Scene
from engine import RenderEngine
from material import Material
from light import Light


def main():
    WIDTH = 500
    HEIGHT = 375 #4:3 ratio

    window = pg.display.set_mode((WIDTH, HEIGHT))
    pg.display.set_caption("Ray Tracer!")

    camera = Vector(0, 0, 2)
    objects = [
        # Sphere(Vector(-1, 0, -2), 0.5, Color.from_hex("#ff0000")),
        Sphere(Vector(0, 0, 0), 1.0, Material(Color.from_hex("#00ffff"), ambient=1.0)),
        # Sphere(Vector(1, 0, -2), 0.5, Color.from_hex("#0000ff"))
    ]
    lights = [Light(position = Vector(1, 1, 1))]
    scene = Scene(camera, objects, lights, WIDTH, HEIGHT)

    engine = RenderEngine()
    img = engine.render(scene)

    # with open("test.ppm", "w") as img_file:
    #     img.write_ppm(img_file)
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        img.paint_image(window, WIDTH, HEIGHT)
        pg.display.update()

        # running = False
    pg.quit()

if __name__ == "__main__":
    main()