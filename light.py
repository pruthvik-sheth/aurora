from color import Color

class Light:
    
    def __init__(self, position, color = Color.from_hex("#FFFFFF")) -> None:
        self.position = position
        self.color = color