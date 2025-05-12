import pygame
import os
from constants import COLORS

class Player:
    def __init__(self, tick, x = 32 , y = 32):
        self.__max_health__ = 100
        self.__current_health__ = 100
        self.position = pygame.math.Vector2(x, y)  # Replace x, y with Vector2
        self.tick = tick
        self.size = pygame.math.Vector2(8, 13)
        self.moving = False
        self.last_direction = 'right'
        self.animation_tick_start = 0
        self.models = self.load_sprites('assets/sprites/Player')
        # self.models = [[
        #         " GGGGGG ",
        #         "GWWWWWWG",
        #         "GWBWWWBG",
        #         "GWWWWWWG",
        #         " GGGGGG ",
        #         "GBBBBBBG",
        #         "GBBBBBBG",
        #         "GBBBBBBG",
        #         " GGGGGG ",
        #         " BG BB  ",
        #         " BG BB  ",
        #         "DBBBGBBD",
        #         " DDDDDD "
        #     ],
        #     [
        #         " GGGGGG ",
        #         "GWWWWWWG",
        #         "GWBWWWBG",
        #         "GWWWWWWG",
        #         " GGGGGG ",
        #         "GBBBBBBG",
        #         "GBBBBBBG",
        #         "GBBBBBBG",
        #         " GGGGGG ",
        #         " BB  B   ",
        #         "BB  DBB ",
        #         "BBBDDBBB",
        #         "DDDDDDDD"
        #     ],
        #     [
        #         " GGGGGG ",
        #         "GWWWWWWG",
        #         "GBWWWBWG",
        #         "GWWWWWWG",
        #         " GGGGGG ",
        #         "GBBBBBBG",
        #         "GBBBBBBG",
        #         "GBBBBBBG",
        #         " GGGGGG ",
        #         "  BB GB ",
        #         "  BB GB ",
        #         "DBBGBBBD",
        #         " DDDDDD "
        #     ],
        #     [
        #         " GGGGGG ",
        #         "GWWWWWWG",
        #         "GBWWWBWG",
        #         "GWWWWWWG",
        #         " GGGGGG ",
        #         "GBBBBBBG",
        #         "GBBBBBBG",
        #         "GBBBBBBG",
        #         " GGGGGG ",
        #         "   B  BB ",
        #         " BBD  BB",
        #         "BBBDDBBBB",
        #         "DDDDDDDD"
        #     ],
        # ]

    def load_sprites(dir):
        sprites = []
        for file in os.listdir(dir):
            if file.endswidth('.png'):
                try:
                    sprite_path = os.path.join(dir, file)
                    sprites = sprites.append(pygame.image.load(sprite_path).convert_alpha())
                    return sprites
                except FileNotFoundError:
                    print(f"Sprite missing for {file}")
                except pygame.error as e:
                    print(f"Error loading sprite for {file}: {e}")

    def move(self, keys, map):
            movement = pygame.math.Vector2(0, 0)  # Initialize movement vector
            if keys[pygame.K_a]:
                self.moving = True
                movement.x -= 1
                self.last_direction = 'left'
                self.animation_tick_start = self.tick
            if keys[pygame.K_d]:
                self.moving = True
                movement.x += 1
                self.last_direction = 'right'
                self.animation_tick_start = self.tick
            if keys[pygame.K_w]:
                self.moving = True
                movement.y -= 1
                self.animation_tick_start = self.tick
            if keys[pygame.K_s]:
                self.moving = True
                movement.y += 1
                self.animation_tick_start = self.tick

            if movement.length() > 0:  # Only update position if there's movement
                self.position += movement

            if self.moving and self.tick == 24:
                self.moving = False
                self.animation_tick_start = 0

            # Clamp position within map bounds
            self.position = pygame.math.Vector2(
                max(0, min(self.position.x, map.size.x - self.size.x)), 
                max(0, min(self.position.y, map.size.y - self.size.y))
                )

    def draw(self, screen, position, pixel_size=4):
        model = self.models[0]
        if self.moving == False:
            if self.last_direction == 'right':
                model = self.models[0]
            elif self.last_direction == 'left':
                model = self.models[1]

        if self.moving == True:
            model = self.models[0] if self.animation_tick_start + self.tick < 12 else self.models[1]
            if self.last_direction == 'left':
                model = self.models[2] if self.animation_tick_start + self.tick < 12 else self.models[3]
                pygame.transform.flip(model)
            
        # for y, row in enumerate(model):
        #     for x, pixel in enumerate(row):
        #         if pixel == 'W':
        #             color = COLORS['white']
        #         elif pixel == 'B':
        #             color = COLORS['black']
        #         elif pixel == 'R':
        #             color = COLORS['red']
        #         elif pixel == 'G':
        #             color = COLORS['grey']
        #         elif pixel == 'D':
        #             color = COLORS['darkgrey']
        #         else:
        #             continue

            pygame.draw.rect(screen, color, 
                ((position.x + x) * pixel_size, 
                (position.y + y) * pixel_size, 
                pixel_size, pixel_size))
