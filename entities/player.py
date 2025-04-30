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
        self.moving = False
        self.last_direction = 'right'
        self.animation_tick_start = 0
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

    def move(self, keys):
        if keys[pygame.K_a]:
            self.moving = True
            self.x -= 1
            self.last_direction = 'left'
            self.animation_tick_start = self.tick
        if keys[pygame.K_d]:
            self.moving = True
            self.x += 1
            self.last_direction = 'right'
            self.animation_tick_start = self.tick
        if keys[pygame.K_w]:
            self.moving = True
            self.y -= 1
            self.animation_tick_start = self.tick
            # self.last_direction = 'up' # Adding this into the ideal response to make it easier to implement later
        if keys[pygame.K_s]:
            self.moving = True
            self.y += 1
            self.animation_tick_start = self.tick
            # self.last_direction = 'down' # Adding this into the ideal response to make it easier to implement later

        if self.moving and self.tick == 24:
            self.moving = False
            self.animation_tick_start = 0

        self.x = max(0, min(self.x, self.level_map.width - self.width))
        self.y = max(0, min(self.y, self.level_map.height - self.height))

    def draw(self, screen, position):
        model = self.models[0]
        draw_x, draw_y = position
        if self.moving == False:
            if self.last_direction == 'right':
                model = self.models[1]
            elif self.last_direction == 'left':
                model = self.models[3]

        if self.moving == True:
            if self.last_direction == 'right':
                model = self.models[1] if self.animation_tick_start + self.tick < 12 else self.models[0]
            else:  # left
                model = self.models[3] if self.animation_tick_start + self.tick < 12 else self.models[2]
            
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
