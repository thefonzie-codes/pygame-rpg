import pygame
from constants import COLORS

class Player:
    def __init__(self, x, y, pixel_size, tick, level_map):
        self.x = x
        self.y = y
        self.pixel_size = pixel_size
        self.tick = tick
        self.level_map = level_map
        self.width = 8
        self.height = 13
        self.models = [[
                " GGGGGG ",
                "GWWWWWWG",
                "GWBWWWBG",
                "GWWWWWWG",
                " GGGGGG ",
                "GBBBBBBG",
                "GBBBBBBG",
                "GBBBBBBG",
                " GGGGGG ",
                " BB  B   ",
                "BB  DBB ",
                "BBBDDBBB",
                "DDDDDDDD"
            ],
            [
                " GGGGGG ",
                "GWWWWWWG",
                "GWBWWWBG",
                "GWWWWWWG",
                " GGGGGG ",
                "GBBBBBBG",
                "GBBBBBBG",
                "GBBBBBBG",
                " GGGGGG ",
                " BG BB  ",
                " BG BB  ",
                "DBBBGBBD",
                " DDDDDD "
            ],
            [
                " GGGGGG ",
                "GWWWWWWG",
                "GBWWWBWG",
                "GWWWWWWG",
                " GGGGGG ",
                "GBBBBBBG",
                "GBBBBBBG",
                "GBBBBBBG",
                " GGGGGG ",
                "   B  BB ",
                " BBD  BB",
                "BBBDDBBBB",
                "DDDDDDDD"
            ],
            [
                " GGGGGG ",
                "GWWWWWWG",
                "GBWWWBWG",
                "GWWWWWWG",
                " GGGGGG ",
                "GBBBBBBG",
                "GBBBBBBG",
                "GBBBBBBG",
                " GGGGGG ",
                "  BB GB ",
                "  BB GB ",
                "DBBGBBBD",
                " DDDDDD "
            ]
        ]
        self.last_direction = 'right'  # Default to right

    def move(self, keys):
        moving = False
        if keys[pygame.K_a]:
            self.x -= 1
            self.last_direction = 'left'
            moving = True
        if keys[pygame.K_d]:
            self.x += 1
            self.last_direction = 'right'
            moving = True

        self.x = max(0, min(self.x, self.level_map.width - self.width))
        self.y = max(0, min(self.y, self.level_map.height - self.height))

    def draw(self, screen, position):
        if self.last_direction == 'right':
            model = self.models[0] if self.tick < 12 else self.models[1]
        else:  # left
            model = self.models[2] if self.tick < 12 else self.models[3]
        draw_x, draw_y = position

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
                    ((draw_x + x) * self.pixel_size, 
                    (draw_y + y) * self.pixel_size, 
                    self.pixel_size, self.pixel_size))
