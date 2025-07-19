import pygame
import random
from utils import CELL_SIZE, GRID_SIZE, RED, GOLD, PURPLE, WHITE, ease_in_out, FOOD_ANIMATION_DURATION

class Food:
    def __init__(self):
        self.position = (0, 0)
        self.animation_timer = 0
        self.animation_duration = FOOD_ANIMATION_DURATION
        self.is_special = False
        self.special_timer = 0
        self.special_duration = 300  # Default 30 seconds at 10 FPS
        self.randomize_position([])

    def randomize_position(self, snake_body):
        while True:
            x = random.randint(0, GRID_SIZE - 1)
            y = random.randint(0, GRID_SIZE - 1)
            if (x, y) not in snake_body:
                self.position = (x, y)
                self.animation_timer = 0  # Reset animation when food moves
                break

    def spawn_special_food(self, snake_body, duration=None):
        """Spawn a special food item with optional custom duration"""
        self.is_special = True
        self.special_timer = duration if duration is not None else self.special_duration
        self.randomize_position(snake_body)

    def set_special_duration(self, duration):
        """Set the default special food duration"""
        self.special_duration = duration

    def update(self):
        """Update animation timer and special food timer"""
        self.animation_timer = (self.animation_timer + 1) % self.animation_duration
        
        # Update special food timer
        if self.is_special:
            self.special_timer -= 1
            if self.special_timer <= 0:
                self.is_special = False

    def render(self, surface):
        x, y = self.position
        rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        
        # Calculate animation scale
        animation_progress = self.animation_timer / self.animation_duration
        base_scale = 0.8 + 0.4 * ease_in_out(animation_progress)
        
        # Special food is larger and has different animation
        if self.is_special:
            # Special food is 1.5x larger and has pulsing effect
            scale = base_scale * 1.5
            color = GOLD if self.special_timer > 60 else PURPLE  # Flash when about to disappear
        else:
            scale = base_scale
            color = RED
        
        # Draw animated colored rectangle
        scaled_rect = pygame.Rect(
            rect.centerx - int(CELL_SIZE * scale / 2),
            rect.centery - int(CELL_SIZE * scale / 2),
            int(CELL_SIZE * scale),
            int(CELL_SIZE * scale)
        )
        pygame.draw.rect(surface, color, scaled_rect)
        pygame.draw.rect(surface, (0, 0, 0), scaled_rect, 2)
        
        # Add sparkle effect for special food
        if self.is_special:
            self.draw_sparkles(surface, rect.center, scale)

    def draw_sparkles(self, surface, center, scale):
        """Draw sparkle effect around special food"""
        sparkle_size = int(CELL_SIZE * scale * 0.3)
        sparkle_color = WHITE if self.special_timer > 60 else PURPLE
        
        # Draw 4 sparkles around the food
        sparkle_positions = [
            (center[0] - sparkle_size, center[1] - sparkle_size),
            (center[0] + sparkle_size, center[1] - sparkle_size),
            (center[0] - sparkle_size, center[1] + sparkle_size),
            (center[0] + sparkle_size, center[1] + sparkle_size)
        ]
        
        for pos in sparkle_positions:
            pygame.draw.circle(surface, sparkle_color, pos, 2) 