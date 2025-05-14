import pygame
import os
from constants import COLORS
from helpers.fonts import load_font

class Player:
    def __init__(self, tick, x = 32 , y = 32):
        self.__max_hp__ = 100
        self.__current_hp__ = 100
        self.position = pygame.math.Vector2(x, y)  # Replace x, y with Vector2
        self.tick = tick
        self.size = pygame.math.Vector2(8, 13)
        self.moving = False
        self.last_direction = 'right'
        self.animation_tick_start = 0
        self.models = self.load_sprites('assets/sprites/Player')

    def load_sprites(self, dir):
        print("\n Loading sprites... \n")
        sprites = []
        for file in os.listdir(dir):
            print(f"{file}")
            if file.endswith('.png'):
                try:
                    sprite_path = os.path.join(dir, file)
                    print(f"{sprite_path}")
                    sprite = pygame.transform.scale(pygame.image.load(sprite_path).convert_alpha(), (120, 120))
                    sprites.append(sprite)
                    print(sprites)
                except FileNotFoundError:
                    print(f"Sprite missing for {file}")
                except pygame.error as e:
                    print(f"Error loading sprite for {file}: {e}")
        return sprites

    def update_health(self, hp_change):
        ## keys will just be for testing
        self.__current_hp__ += hp_change        ## keys will just be for testing

        if hp_change < 0:
            print(f"DAMAGE TAKEN, CURRENT HP: {self.__current_hp__}")
            return

        print(f"PLAYER HEALED:  CURRENT HP: {self.__current_hp__}")
        print(self.__current_hp__)

    def display_damage(self, damage):
        self.update_health(damage)
        damage_animation_tick_start = self.tick
        animation_frame = 0
        tick_end = damage_animation_tick_start + 24
        pixel_font = load_font('fonts/damage/Jersey10-Regular.ttf', 100)
        damage = pixel_font.render('PYGAME RPG', True, COLORS['red'])
        dmg_text_rect = damage.get_rect()
        while animation_frame < tick_end:
            print(animation_frame)
            print(damage)

    def display_healing(self, healing):
        pass

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

    def draw(self, game_surface, position, pixel_size=4):
        model = self.models[0]
        if self.moving == False:
            if self.last_direction == 'left':
               model = pygame.transform.flip(model, True, False)

        if self.moving == True:
            model = self.models[0] if self.animation_tick_start + self.tick < 12 else self.models[1]
            if self.last_direction == 'left':
                model = pygame.transform.flip(model, True, False)
                # model = self.models[2] if self.animation_tick_start + self.tick < 12 else self.models[3]

        game_surface.blit(model, (
            (position.x) * pixel_size, 
            (position.y) * pixel_size))
