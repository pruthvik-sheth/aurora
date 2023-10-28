

class Image:

    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        self.pixels = [
            [None for _ in range(width)] for _ in range(height)
        ]

    def set_pixel(self, x, y, color):
        self.pixels[y][x] = color

    def paint_image(self, window, WIDTH, HEIGHT):
        
        def conv_0_to_255(value):
            new_value = round(value * 255) # 0-1 -> 0-255
            clamped_value = max(min(new_value, 255), 0) # Claming the values that are greater than 255 to 255
            return clamped_value
        
        for y, row in enumerate(self.pixels):
            for x, color in enumerate(row):
                window.set_at((x, y), (conv_0_to_255(color.x), conv_0_to_255(color.y), conv_0_to_255(color.z)))

        # img_file.write(f"P3 {self.width} {self.height}\n255\n")
        # for row in self.pixels:
        #     for color in row:
        #         img_file.write(f"{conv_0_to_255(color.x)} {conv_0_to_255(color.y)} {conv_0_to_255(color.z)} ")
        #     img_file.write("\n")