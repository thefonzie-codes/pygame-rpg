import pygame

def load_font():
    try:
        pixel_font = pygame.font.Font('fonts/damage/Jersey10-Regular.ttf, 36')
        return pixel_font
    except FileNotFoundError:
        print(f"Error: Font not found, using default.")
        return pygame.font.SysFont('Arial', 36)