import pygame
import random
from snake import Snake
from food import Food
from menu import Menu
from utils import *

class Game:
    def __init__(self, surface):
        self.surface = surface
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('consolas', 24)
        self.big_font = pygame.font.SysFont('consolas', 48, bold=True)
        
        # Initialize menu system
        self.menu = Menu(surface)
        
        # Game state
        self.state = 'MENU'  # MENU, PLAYING, PAUSED, GAME_OVER
        self.reset()
        
        # Mouse tracking
        self.mouse_pos = (0, 0)
        self.mouse_clicked = False
        self.mouse_down = False

    def reset(self):
        self.snake = Snake()
        self.food = Food()
        self.score = 0
        self.high_score = load_high_score()
        
        # Get settings from menu
        settings = self.menu.get_settings()
        self.speed = settings['speed']
        self.special_food_chance = settings['special_food_chance'] / 100.0  # Convert to decimal
        self.special_food_duration = settings['special_food_duration'] * 10  # Convert to frames

    def handle_events(self):
        self.mouse_clicked = False
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                self.handle_keydown(event.key)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    self.mouse_clicked = True
                    self.mouse_down = True
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:  # Left click release
                    self.mouse_down = False
            elif event.type == pygame.MOUSEMOTION:
                self.mouse_pos = event.pos
                
        return True

    def handle_keydown(self, key):
        if self.state == 'PLAYING':
            if key == pygame.K_UP:
                self.snake.set_direction((0, -1))
            elif key == pygame.K_DOWN:
                self.snake.set_direction((0, 1))
            elif key == pygame.K_LEFT:
                self.snake.set_direction((-1, 0))
            elif key == pygame.K_RIGHT:
                self.snake.set_direction((1, 0))
            elif key == pygame.K_ESCAPE:
                self.state = 'PAUSED'
                self.menu.set_state('PAUSE')
        elif self.state == 'PAUSED':
            if key == pygame.K_ESCAPE:
                self.state = 'PLAYING'
        elif self.state == 'GAME_OVER':
            if key == pygame.K_SPACE:
                self.restart_game()
        elif self.state == 'MENU':
            if key == pygame.K_SPACE:
                self.start_new_game()

    def update(self):
        # Update food animation
        self.food.update()
        
        # Handle menu interactions
        if self.state in ['MENU', 'PAUSED', 'GAME_OVER']:
            menu_action = self.menu.update(self.mouse_pos, self.mouse_clicked, self.mouse_down)
            if menu_action == 'QUIT':
                return False
            elif menu_action == 'PLAY':
                self.start_new_game()
            elif menu_action == 'RESUME':
                self.state = 'PLAYING'
            elif menu_action == 'RESTART':
                self.restart_game()
            elif menu_action == 'MENU':
                self.state = 'MENU'
                self.menu.set_state('MAIN')
        
        # Update game logic
        if self.state == 'PLAYING':
            self.update_game()
        
        return True

    def start_new_game(self):
        """Start a completely new game with current settings"""
        self.reset()
        self.state = 'PLAYING'

    def update_game(self):
        self.snake.move()
        
        # Check for self-collision
        if self.snake.collides_with_self():
            self.game_over()
            return
        
        # Check for food collision
        if self.snake.get_head() == self.food.position:
            if self.food.is_special:
                # Special food gives bonus points and growth
                self.snake.grow()
                self.snake.grow()
                self.snake.grow()  # 3 extra segments
                self.score += 5  # 5 points instead of 1
            else:
                # Normal food
                self.snake.grow()
                self.score += 1
            
            # Spawn new food
            self.food.randomize_position(self.snake.body)
            
            # Check if we should spawn special food (only when no special food is active)
            if not self.food.is_special:
                # Check every 3 points instead of 5 for more frequent spawning
                if self.score % 3 == 0:
                    # Use the configured chance from settings
                    if random.random() < self.special_food_chance:
                        self.food.spawn_special_food(self.snake.body, self.special_food_duration)
                        print(f"Special food spawned at score {self.score} with {self.special_food_chance*100:.1f}% chance")
                    else:
                        print(f"Special food check at score {self.score} - failed ({self.special_food_chance*100:.1f}% chance)")
            
            # Increase speed every 5 points (but respect settings)
            if self.score % 5 == 0:
                settings = self.menu.get_settings()
                max_speed = settings['speed'] + 10  # Allow some speed increase
                self.speed = min(self.speed + 2, max_speed)

    def game_over(self):
        self.state = 'GAME_OVER'
        self.menu.set_state('GAME_OVER')
        
        if self.score > self.high_score:
            save_high_score(self.score)
            self.high_score = self.score

    def restart_game(self):
        """Restart the current game with same settings"""
        self.reset()
        self.state = 'PLAYING'

    def render_status_bar(self):
        bar_height = 40
        pygame.draw.rect(self.surface, BLUE, (0, WINDOW_SIZE, WINDOW_SIZE, bar_height))
        
        # Score text
        score_text = self.font.render(f'Score: {self.score}', True, WHITE)
        self.surface.blit(score_text, (10, WINDOW_SIZE + 10))
        
        # High score text
        high_score_text = self.font.render(f'High Score: {self.high_score}', True, WHITE)
        self.surface.blit(high_score_text, (200, WINDOW_SIZE + 10))
        
        # Special food indicator
        if self.food.is_special:
            special_text = self.font.render(f'Special Food: {self.food.special_timer//10}s', True, GOLD)
            self.surface.blit(special_text, (400, WINDOW_SIZE + 10))
        else:
            # Debug info for special food
            next_check = 3 - (self.score % 3)
            if next_check == 3:
                next_check = 0
            debug_text = self.font.render(f'Next check: {next_check} | Chance: {self.special_food_chance*100:.0f}%', True, WHITE)
            self.surface.blit(debug_text, (400, WINDOW_SIZE + 10))

    def render_game(self):
        # Draw background
        self.surface.fill(BLACK)
        
        # Draw grid
        draw_grid(self.surface)
        
        # Draw game objects
        self.food.render(self.surface)
        self.snake.render(self.surface)
        
        # Draw status bar
        self.render_status_bar()

    def render(self):
        if self.state == 'PLAYING':
            self.render_game()
        elif self.state == 'MENU':
            self.menu.render()
        elif self.state == 'PAUSED':
            self.render_game()  # Show game in background
            self.menu.render()
        elif self.state == 'GAME_OVER':
            self.render_game()  # Show game in background
            self.menu.render(self.score, self.high_score)
        
        pygame.display.flip()

    def run(self):
        running = True
        while running:
            self.clock.tick(self.speed)
            if not self.handle_events():
                break
            if not self.update():
                break
            self.render() 