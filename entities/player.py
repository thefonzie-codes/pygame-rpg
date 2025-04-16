import pygame

class Player:
    def __init__(self, x, y, pixel_size, tick, grid_size):
        self.x = x
        self.y = y
        self.pixel_size = pixel_size
        self.tick = tick
        self.grid_size = grid_size
        self.width = 8
        self.height = 12
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
        ]]

    def move(self, keys):
        if keys[pygame.K_w]:
            self.y -= 1
        if keys[pygame.K_s]:
            self.y += 1
        if keys[pygame.K_a]:
            self.x -= 1
        if keys[pygame.K_d]:
            self.x += 1

        self.x = max(0, min(self.x, self.grid_size - self.width))
        self.y = max(0, min(self.y, self.grid_size - self.height))
