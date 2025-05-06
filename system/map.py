import pygame

class Map:
    def __init__(self, width, height, pixel_size, floor_texture):
        self.size = pygame.math.Vector2(width, height)
        self.pixel_size = pixel_size
        self.floor_texture = floor_texture

    def draw(self, screen, camera):
        start = pygame.math.Vector2(max(0, camera.offset.x), max(0, camera.offset.y))
        end = pygame.math.Vector2(
            min(self.size.x, camera.offset.x + (camera.size.x // self.pixel_size)), 
            min(self.size.y, camera.offset.y + (camera.size.y // self.pixel_size))
            )

        for x in range(int(start.x), int(end.x)):
            for y in range(int(start.y), int(end.y)):

                # There is no point in converting this to a vector2.
                pattern_x = x % len(self.floor_texture.pattern[0])
                pattern_y = y % len(self.floor_texture.pattern)

                tile = self.floor_texture.pattern[pattern_y][pattern_x]

                screen_position = pygame.math.Vector2((x - camera.offset.x) * self.pixel_size, (y - camera.offset.y) * self.pixel_size)
                pygame.draw.rect(screen, self.floor_texture.colors[tile], (screen_position.x, screen_position.y, self.pixel_size, self.pixel_size))
