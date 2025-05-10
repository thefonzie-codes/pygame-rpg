import pygame
import sys
import argparse
from entities.ghost import Ghost
from entities.player import Player
from helpers.music import play_music
from helpers.fonts import load_font
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

    # Music"
    play_music("audio/Trilogy - Telecasted.mp3")

    # Screen
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    screen_width, screen_height = screen.get_size()

    pygame.display.set_caption('RPG Game')

    ## Font rendering
    pixel_font = load_font('fonts/damage/Jersey10-Regular.ttf', 100)
    title = pixel_font.render('PYGAME RPG', True, COLORS['white'])
    title_rect = title.get_rect()

    # FPS and Game
    tick = 0
    clock = pygame.time.Clock()
    running = True

    # Camera
    camera = Camera(VIEWPORT.x, VIEWPORT.y)
    camera.set_screen_size(screen_width, screen_height)

    # Map
    base_floor = BaseFloor()
    level_map = Map(MAX_MAP_WIDTH, MAX_MAP_HEIGHT, PIXEL_SIZE, base_floor)

    # Entities
    ghost = Ghost(tick) 
    player = Player(tick)
    
    # Create a surface for the game viewport
    game_surface = pygame.Surface((VIEWPORT.x, VIEWPORT.y))

    while running:

        clock.tick(FPS)
        if tick >= FPS:
            tick = 0
        else:
            tick += 1
            
        ghost.tick = tick
        player.tick = tick
        
        # Fill the main screen with light gray (for the frame)
        screen.fill(COLORS['black'])
        screen.blit(title, (
            screen_width // 2 - title_rect.w // 2,
            (screen_height // 2 - VIEWPORT.y // 2) // 2 - title_rect.h // 2
            ))

        # Get the position to center the game surface on screen
        frame_pos = camera.get_frame_position()

        # Draw the game surface onto the main screen at the centered position
        screen.blit(game_surface, (frame_pos.x, frame_pos.y))

        frame_thickness = 4
        frame = pygame.Rect(
            frame_pos.x - frame_thickness,
            frame_pos.y - frame_thickness,
            VIEWPORT.x + (frame_thickness * 2), 
            VIEWPORT.y + (frame_thickness * 2),
        )
        pygame.draw.rect(screen, COLORS['lightgrey'], frame, frame_thickness)
        
        # Fill the game surface with black
        game_surface.fill(COLORS['black'])

        keys = pygame.key.get_pressed()
        player.move(keys, level_map)
                
        ghost.move(level_map)
        camera.update(player)

        # Draw to the game surface instead of directly to the screen
        level_map.draw(game_surface, camera)

        ghost_pos = camera.apply(ghost)
        player_pos = camera.apply(player)

        draw_entity(game_surface, ghost, ghost_pos, COLORS)
        player.draw(game_surface, player_pos)

        # Debug information
        if debug_mode and tick % 10 == 0:  # Only print every 10 ticks to avoid console spam
            print("\n--- DEBUG INFO ---")
            print(f"Camera: pos=({camera.offset.x}, {camera.offset.y}), size=({camera.size.x}, {camera.size.y})")
            print(f"Frame position: ({frame_pos.x}, {frame_pos.y})")
            print(f"Screen size: ({screen_width}, {screen_height})")
            print(f"Player: pos=({player.position.x}, {player.position.y}), size=({player.size.x}, {player.size.y})")
            print(f"Ghost: pos=({ghost.position.x}, {ghost.position.y}), size=({ghost.size.x}, {ghost.size.y})")
            print(f"Map: viewport=({camera.offset.x}-{camera.offset.x + camera.size.x // PIXEL_SIZE}, "
                f"{camera.offset.y}-{camera.offset.y + camera.size.y // PIXEL_SIZE}), "
                f"size=({level_map.size.x}, {level_map.size.y})")
            print("-----------------") 

        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.flip()  # Update the display

def draw_entity(screen, entity, position, colors, pixel_size = 4):
    model = entity.models[0] if entity.tick < 12 else entity.models[1]

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
                ((position.x + x) * pixel_size, 
                 (position.y + y) * pixel_size, 
                 pixel_size, pixel_size))

if __name__ == '__main__':
    main()
