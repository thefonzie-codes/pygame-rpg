import pygame
import sys
import argparse
from entities.ghost import Ghost
from entities.player import Player
from system.camera import Camera
from constants import *
from system.map import Map
from textures.base_floor import BaseFloor

def main():
    parser = argparse.ArgumentParser(description='RPG Game')
    parser.add_argument('--debug', action='store_true', help='Enable debug mode')
    args = parser.parse_args()
    
    debug_mode = args.debug
    
    pygame.init()

    screen = pygame.display.set_mode((VIEWPORT_WIDTH, VIEWPORT_HEIGHT))
    pygame.display.set_caption('RPG Game')

    tick = 0
    clock = pygame.time.Clock()
    running = True

    ghost = Ghost(64, 64, PIXEL_SIZE, tick, GRID_SIZE) 

    camera = Camera(VIEWPORT_WIDTH, VIEWPORT_HEIGHT)

    base_floor = BaseFloor()
    level_map = Map(MAX_MAP_WIDTH, MAX_MAP_HEIGHT, PIXEL_SIZE, base_floor)

    player = Player(32, 32, PIXEL_SIZE, tick, level_map)

    while running:

        clock.tick(FPS)
        if tick >= FPS:
            tick = 0
        else:
            tick += 1
            
        ghost.tick = tick
        player.tick = tick
        
        screen.fill(COLORS['black'])

        keys = pygame.key.get_pressed()
        player.move(keys)
                
        ghost.move()
        camera.update(player)

        level_map.draw(screen, camera)

        ghost_pos = camera.apply(ghost)
        player_pos = camera.apply(player)

        draw_entity(screen, ghost, ghost_pos, COLORS)
        draw_entity(screen, player, player_pos, COLORS)

        # Debug information
        if debug_mode and tick % 10 == 0:  # Only print every 10 ticks to avoid console spam
            print("\n--- DEBUG INFO ---")
            print(f"Camera: pos=({camera.offset_x}, {camera.offset_y}), size=({camera.width}, {camera.height})")
            print(f"Player: pos=({player.x}, {player.y}), size=({player.width}, {player.height})")
            print(f"Ghost: pos=({ghost.x}, {ghost.y}), size=({ghost.width}, {ghost.height})")
            print(f"Map: viewport=({camera.offset_x}-{camera.offset_x + camera.width // PIXEL_SIZE}, "
                  f"{camera.offset_y}-{camera.offset_y + camera.height // PIXEL_SIZE}), "
                  f"size=({level_map.width}, {level_map.height})")
            print("-----------------")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.flip()  # Update the display


def draw_entity(screen, entity, position, colors):
    model = entity.models[0] if entity.tick < 12 else entity.models[1]
    draw_x, draw_y = position

    for y, row in enumerate(model):
        for x, pixel in enumerate(row):
            if pixel == 'W':
                color = colors['white']
            elif pixel == 'B':
                color = colors['black']
            elif pixel == 'R':
                color = colors['red']
            elif pixel == 'G':
                color = colors['grey']
            elif pixel == 'D':
                color = colors['darkgrey']
            else:
                continue

            pygame.draw.rect(screen, color, 
                ((draw_x + x) * entity.pixel_size, 
                 (draw_y + y) * entity.pixel_size, 
                 entity.pixel_size, entity.pixel_size))

if __name__ == '__main__':
    main()
