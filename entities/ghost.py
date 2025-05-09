import random
import pygame.math

class Ghost:
    def __init__(self, x, y, tick):
        self.position = pygame.math.Vector2(x, y)  # Replace separate x, y with Vector2
        self.movement = pygame.math.Vector2(random.choice([(1, 0), (0, 1), (-1, 0), (0, -1)]))  # Vector2 direction
        self.size = pygame.math.Vector2(8, 11)
        self.tick = tick
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

    def move(self, map):
        if random.randint(0, 100) < 10:  # Change direction randomly
            self.movement = pygame.math.Vector2(random.choice([(1, 0), (0, 1), (-1, 0), (0, -1)]))

        self.position += self.movement  # Vector addition for movement

        # Clamp position within grid bounds
        self.position = pygame.math.Vector2(
            max(0, min(self.position.x, map.size.x - self.size.x)), 
            max(0, min(self.position.y, map.size.y - self.size.y))
            )
