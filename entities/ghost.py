import random

class Ghost:
    def __init__(self, x, y, pixel_size, tick, grid_size):
        self.x = x
        self.y = y
        self.pixel_size = pixel_size
        self.direction = random.choice([(1, 0), (0, 1), (-1, 0), (0, -1)])  # Random initial direction
        self.tick = tick
        self.grid_size = grid_size
        self.width = 8 
        self.height = 11
        self.models = [[
            " WWWWWW ",
            "WBBBBBBW",
            "WBBBBBBW",
            "WBWBBWBW",
            "GBBBBBBG",
            "GGGGGGGG",
            "GGBWWBGG",
            "GGGGGGGG",
            " GGGGGG ",
            "   GGG  ",
            "    GG  ",
        ],
        [
            " WWWWWW ",
            "WBBBBBBW",
            "WBBBBBBW",
            "WBWBBWBW",
            "GBBBBBBG",
            "GGGGGGGG",
            "GGBWWBGG",
            "GGGGGGGG",
            " GGGGGG ",
            "  GGG   ",
            "  GG    ",
        ]]

    def move(self):
        if random.randint(0, 100) < 10:  # Change direction randomly
            self.direction = random.choice([(1, 0), (0, 1), (-1, 0), (0, -1)])
            
        self.x += self.direction[0]
        self.y += self.direction[1]

        self.x = max(0, min(self.x, self.grid_size - self.width)) 
        self.y = max(0, min(self.y, self.grid_size - self.height))
