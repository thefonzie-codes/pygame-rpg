import random
import pygame.math

class Ghost:
    def __init__(self, x, y, pixel_size, tick, grid_size):
        self.position = pygame.math.Vector2(x, y)  # Replace separate x, y with Vector2
        self.direction = pygame.math.Vector2(random.choice([(1, 0), (0, 1), (-1, 0), (0, -1)]))  # Vector2 direction
        self.size = pygame.math.Vector2(8, 11)
        self.pixel_size = pixel_size
        self.tick = tick
        self.grid_size = grid_size
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
            self.direction = pygame.math.Vector2(random.choice([(1, 0), (0, 1), (-1, 0), (0, -1)]))

        self.position += self.direction  # Vector addition for movement

        # Clamp position within grid bounds
        self.position.x = max(0, min(self.position.x, self.grid_size - self.size.x))
        self.position.y = max(0, min(self.position.y, self.grid_size - self.size.y))
