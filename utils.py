import pygame
import os

# Game constants
WINDOW_SIZE = 600
GRID_SIZE = 30
CELL_SIZE = WINDOW_SIZE // GRID_SIZE
FPS = 10

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
DARK_GRAY = (40, 40, 40)
YELLOW = (255, 255, 0)
BLUE = (0, 120, 255)
GRAY = (128, 128, 128)
GOLD = (255, 215, 0)  # Special food color
PURPLE = (128, 0, 128)  # Special food hover color

# Animation constants
FOOD_ANIMATION_DURATION = 30

# Special food constants
SPECIAL_FOOD_DURATION = 300  # 30 seconds at 10 FPS
SPECIAL_FOOD_SPAWN_CHANCE = 0.1  # 10% chance every 5 points
SPECIAL_FOOD_GROWTH_BONUS = 3  # Extra segments when eaten

# High score file
HIGH_SCORE_FILE = 'highscore.txt'

def draw_grid(surface):
    for x in range(0, WINDOW_SIZE, CELL_SIZE):
        pygame.draw.line(surface, DARK_GRAY, (x, 0), (x, WINDOW_SIZE))
    for y in range(0, WINDOW_SIZE, CELL_SIZE):
        pygame.draw.line(surface, DARK_GRAY, (0, y), (WINDOW_SIZE, y))

def ease_in_out(t):
    """Easing function for smooth animations"""
    return t * t * (3.0 - 2.0 * t)

def load_high_score():
    if not os.path.exists(HIGH_SCORE_FILE):
        return 0
    with open(HIGH_SCORE_FILE, 'r') as f:
        try:
            return int(f.read())
        except ValueError:
            return 0

def save_high_score(score):
    with open(HIGH_SCORE_FILE, 'w') as f:
        f.write(str(score)) 