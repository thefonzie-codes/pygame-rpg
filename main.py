import pygame
import sys
from entities.ghost import Ghost
from entities.player import Player
from system.camera import Camera
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, COLORS, GRID_SIZE, PIXEL_SIZE, FPS

def main():
    # Initialize pygame
    pygame.init()

    # Set up the display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('RPG Game')


    # Use a tick counter to control the animation
    tick = 0
    clock = pygame.time.Clock()
    running = True

    ghost = Ghost(64, 64, PIXEL_SIZE, tick, GRID_SIZE) 
    
    player = Player(32, 32, PIXEL_SIZE, tick, GRID_SIZE)

    camera = Camera(SCREEN_WIDTH, SCREEN_HEIGHT, GRID_SIZE)

    # Main game loop
    while running:
        clock.tick(FPS)
        # Resets the tick counter if it reaches the FPS
        if tick >= FPS:
            tick = 0
        else:
            tick += 1
            
        ghost.tick = tick
        player.tick = tick
        
        screen.fill(COLORS['black'])  # Clear screen
        
        # Get keyboard input
        keys = pygame.key.get_pressed()
        player.move(keys)
                
        ghost.move()  # Move the ghost

        # Update camera to follow player
        camera.update(player)

        ghost_pos = camera.apply(ghost)
        player_pos = camera.apply(player)

        draw_entity(screen, ghost, ghost_pos, COLORS)
        draw_entity(screen, player, player_pos, COLORS)

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
            else:
                continue

            pygame.draw.rect(screen, color, 
                ((draw_x + x) * entity.pixel_size, 
                 (draw_y + y) * entity.pixel_size, 
                 entity.pixel_size, entity.pixel_size))

if __name__ == '__main__':
    main()
