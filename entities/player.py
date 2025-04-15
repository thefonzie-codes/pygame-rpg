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
            "    RR  ",
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
            "  RR    ",
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

    def draw(self, screen, colors):
        model = self.models[0] if self.tick < 12 else self.models[1]
        for y, row in enumerate(model):
            for x, pixel in enumerate(row):   
                if pixel == 'W':
                    color = colors['white']
                elif pixel == 'B':
                    color = colors['black']
                elif pixel == 'R':
                    color = colors['red']  # Using red for player
                else:
                    continue

                pygame.draw.rect(screen, color, ((self.x + x) * self.pixel_size, (self.y + y) * self.pixel_size, self.pixel_size, self.pixel_size)) 