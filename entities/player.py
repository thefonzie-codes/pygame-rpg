import pygame

class Player:
    def __init__(self, x, y, pixel_size, tick, grid_size):
        self.x = x
        self.y = y
        self.pixel_size = pixel_size
        self.tick = tick
        self.grid_size = grid_size
        self.width = 8
        self.height = 11
        self.models = [[
            " WWWWWW ",
            "WBBBBBBW",
            "WBBBBBBW",
            "WBWBBWBW",
            "RBBBBBBR",
            "RRRRRRRR",
            "RRBWWBRR",
            "RRRRRRRR",
            " RRRRRR ",
            "   RRR  ",
            "    RRR ",
        ],
        [
            " WWWWWW ",
            "WBBBBBBW",
            "WBBBBBBW",
            "WBWBBWBW",
            "RBBBBBBR",
            "RRRRRRRR",
            "RRBWWBRR",
            "RRRRRRRR",
            " RRRRRR ",
            "  RRR   ",
            " RRR    ",
        ]]
        # Add 'red' to colors in main.py

    def move(self, keys):
        # Move based on keyboard input
        if keys[pygame.K_w]:  # Up
            self.y -= 1
        if keys[pygame.K_s]:  # Down
            self.y += 1
        if keys[pygame.K_a]:  # Left
            self.x -= 1
        if keys[pygame.K_d]:  # Right
            self.x += 1

        # Keep within bounds
        self.x = max(0, min(self.x, self.grid_size - self.width))
        self.y = max(0, min(self.y, self.grid_size - self.height))
