import pygame
from utils import CELL_SIZE, GRID_SIZE, GREEN, YELLOW, BLACK

class Snake:
    def __init__(self):
        self.reset()

    def reset(self):
        self.body = [(GRID_SIZE // 2, GRID_SIZE // 2)]
        self.direction = (0, -1)  # Start moving up
        self.grow_pending = 0

    def set_direction(self, dir):
        # Prevent reversing
        if (dir[0] == -self.direction[0] and dir[1] == -self.direction[1]):
            return
        self.direction = dir

    def move(self):
        head_x, head_y = self.body[0]
        dx, dy = self.direction
        
        # Calculate new head position with wall wrapping
        new_head_x = (head_x + dx) % GRID_SIZE
        new_head_y = (head_y + dy) % GRID_SIZE
        new_head = (new_head_x, new_head_y)
        
        self.body.insert(0, new_head)
        if self.grow_pending > 0:
            self.grow_pending -= 1
        else:
            self.body.pop()

    def grow(self):
        self.grow_pending += 1

    def collides_with_self(self):
        return self.body[0] in self.body[1:]

    def collides_with_wall(self):
        # No longer needed since we implement wall wrapping
        return False

    def get_head(self):
        return self.body[0]

    def render(self, surface):
        for i, (x, y) in enumerate(self.body):
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            
            if i == 0:  # Head
                pygame.draw.rect(surface, YELLOW, rect)
                pygame.draw.rect(surface, BLACK, rect, 2)
            else:  # Body
                pygame.draw.rect(surface, GREEN, rect)
                pygame.draw.rect(surface, BLACK, rect, 1) 