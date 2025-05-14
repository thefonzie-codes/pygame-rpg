import random
import pygame.math
from constants import COLORS

class Ghost:
    def __init__(self, x=64, y=64):
        self.position = pygame.math.Vector2(x, y)  # Replace separate x, y with Vector2
        self.movement = pygame.math.Vector2(random.choice([(1, 0), (0, 1), (-1, 0), (0, -1)]))  # Vector2 direction
        self.size = pygame.math.Vector2(8, 11)
        self.animation_time_start = pygame.time.get_ticks() / 1000.0
        self.animation_duration = 0.5  # Duration of animation cycle in seconds
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

    def update(self, map, dt, speed=25):  # Speed in pixels per second
        if random.randint(0, 100) < 2:  # Change direction randomly
            self.movement = pygame.math.Vector2(random.choice([(1, 0), (0, 1), (-1, 0), (0, -1)])) * speed * dt

        self.position += self.movement  # Vector addition for movement

        # Clamp position within grid bounds
        self.position = pygame.math.Vector2(
            max(0, min(self.position.x, map.size.x - self.size.x)), 
            max(0, min(self.position.y, map.size.y - self.size.y))
            )

    def draw(self, screen, position, pixel_size=4):
        current_time = pygame.time.get_ticks() / 1000.0
        elapsed = current_time - self.animation_time_start
        model = self.models[0 if elapsed < self.animation_duration / 2 else 1]
        if elapsed >= self.animation_duration:
            self.animation_time_start = current_time  # Reset animation cycle

        for y, row in enumerate(model):
            for x, pixel in enumerate(row):
                if pixel == 'W':
                    color = COLORS['white']
                elif pixel == 'B':
                    color = COLORS['black']
                elif pixel == 'R':
                    color = COLORS['red']
                elif pixel == 'G':
                    color = COLORS['grey']
                elif pixel == 'D':
                    color = COLORS['darkgrey']
                else:
                    continue

                pygame.draw.rect(screen, color, 
                    ((position.x + x) * pixel_size, 
                    (position.y + y) * pixel_size, 
                    pixel_size, pixel_size))