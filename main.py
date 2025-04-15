import pygame
import sys
from entities.ghost import Ghost
from entities.player import Player
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, COLORS, GRID_SIZE, PIXEL_SIZE, FPS

def main():
    # Initialize pygame
    pygame.init()

    # Set up the display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Moving Ghost')

    # Add red color for the player
    COLORS['red'] = (255, 0, 0)

    # Use a tick counter to control the animation
    tick = 0
    clock = pygame.time.Clock()
    running = True

    # Initialize a Ghost
    ghost = Ghost(64, 64, PIXEL_SIZE, tick, GRID_SIZE) 
    
    # Initialize a Player
    player = Player(32, 32, PIXEL_SIZE, tick, GRID_SIZE)

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
        
        ghost.draw(screen, COLORS)  # Draw the ghost
        player.draw(screen, COLORS)  # Draw the player
        
        ghost.move()  # Move the ghost

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.flip()  # Update the display

if __name__ == '__main__':
    main()