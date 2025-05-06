import pygame

class Camera:

    def __init__(self, width, height):
        self.size = pygame.math.Vector2(width, height)
        self.offset = pygame.math.Vector2(0, 0) 

    def update(self, target):
        target_center = pygame.math.Vector2(target.position.x + target.size.x // 2, target.position.y + target.size.y // 2)
        self.offset = target_center - (self.size // (2 * target.pixel_size))

    def apply(self, entity):
        return pygame.math.Vector2(entity.position.x - self.offset.x, entity.position.y - self.offset.y)  # Return tuple for drawing
