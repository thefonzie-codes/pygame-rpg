import pygame

class Map:
    def __init__(self, width, height, pixel_size, floor_texture):
        self.width = width
        self.height = height
        self.pixel_size = pixel_size
        self.floor_texture = floor_texture

    def draw(self, screen, camera):
        start_x = max(0, camera.offset_x)
        start_y = max(0, camera.offset_y)
        end_x = min(self.width, camera.offset_x + (camera.width // self.pixel_size))
        end_y = min(self.height, camera.offset_y + (camera.height // self.pixel_size))

        for x in range(start_x, end_x):
            for y in range(start_y, end_y):

                pattern_x = x % len(self.floor_texture.pattern[0])
                pattern_y = y % len(self.floor_texture.pattern)

                tile = self.floor_texture.pattern[pattern_y][pattern_x]

                screen_x = (x - camera.offset_x) * self.pixel_size
                screen_y = (y - camera.offset_y) * self.pixel_size

                pygame.draw.rect(screen, self.floor_texture.colors[tile], (screen_x, screen_y, self.pixel_size, self.pixel_size))