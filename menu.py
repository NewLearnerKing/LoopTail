import pygame
from utils import WINDOW_SIZE, WHITE, BLACK, BLUE, GRAY, GREEN, RED

class Button:
    def __init__(self, x, y, width, height, text, font_size=24, color=BLUE, hover_color=GREEN):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = pygame.font.SysFont('consolas', font_size)
        self.color = color
        self.hover_color = hover_color
        self.is_hovered = False
        
    def update(self, mouse_pos):
        self.is_hovered = self.rect.collidepoint(mouse_pos)
        
    def render(self, surface):
        color = self.hover_color if self.is_hovered else self.color
        pygame.draw.rect(surface, color, self.rect)
        pygame.draw.rect(surface, WHITE, self.rect, 2)
        
        # Draw text
        text_surface = self.font.render(self.text, True, WHITE)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)
        
    def is_clicked(self, mouse_pos, mouse_clicked):
        return self.rect.collidepoint(mouse_pos) and mouse_clicked

class Slider:
    def __init__(self, x, y, width, height, min_val, max_val, initial_val, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.min_val = min_val
        self.max_val = max_val
        self.value = initial_val
        self.text = text
        self.font = pygame.font.SysFont('consolas', 20)
        self.is_dragging = False
        self.is_hovered = False
        
    def update(self, mouse_pos, mouse_clicked, mouse_down):
        self.is_hovered = self.rect.collidepoint(mouse_pos)
        
        if mouse_clicked and self.is_hovered:
            self.is_dragging = True
        
        if not mouse_down:
            self.is_dragging = False
            
        if self.is_dragging:
            # Calculate value based on mouse position
            rel_x = mouse_pos[0] - self.rect.x
            self.value = self.min_val + (rel_x / self.rect.width) * (self.max_val - self.min_val)
            self.value = max(self.min_val, min(self.max_val, self.value))
    
    def render(self, surface):
        # Draw background
        pygame.draw.rect(surface, GRAY, self.rect)
        pygame.draw.rect(surface, WHITE, self.rect, 2)
        
        # Draw fill
        fill_width = (self.value - self.min_val) / (self.max_val - self.min_val) * self.rect.width
        fill_rect = pygame.Rect(self.rect.x, self.rect.y, fill_width, self.rect.height)
        pygame.draw.rect(surface, GREEN, fill_rect)
        
        # Draw text
        text_surface = self.font.render(f"{self.text}: {int(self.value)}", True, WHITE)
        text_rect = text_surface.get_rect(midleft=(self.rect.x, self.rect.y - 25))
        surface.blit(text_surface, text_rect)

class Menu:
    def __init__(self, surface):
        self.surface = surface
        self.title_font = pygame.font.SysFont('consolas', 48, bold=True)
        self.subtitle_font = pygame.font.SysFont('consolas', 24)
        
        # Calculate button positions
        center_x = WINDOW_SIZE // 2
        button_width = 200
        button_height = 50
        button_spacing = 70
        
        # Create buttons for main menu with new color scheme
        self.main_buttons = {
            'play': Button(center_x - button_width//2, 250, button_width, button_height, "PLAY GAME", color=(100, 200, 100), hover_color=(150, 255, 150)),
            'settings': Button(center_x - button_width//2, 250 + button_spacing, button_width, button_height, "SETTINGS", color=(100, 100, 200), hover_color=(150, 150, 255)),
            'quit': Button(center_x - button_width//2, 250 + button_spacing * 2, button_width, button_height, "QUIT", color=(200, 100, 100), hover_color=(255, 150, 150))
        }
        
        # Create buttons for pause menu with consistent color scheme
        self.pause_buttons = {
            'resume': Button(center_x - button_width//2, 200, button_width, button_height, "RESUME", color=(100, 200, 100), hover_color=(150, 255, 150)),
            'menu': Button(center_x - button_width//2, 200 + button_spacing, button_width, button_height, "MAIN MENU", color=(100, 100, 200), hover_color=(150, 150, 255))
        }
        
        # Create buttons for game over menu with consistent color scheme
        self.game_over_buttons = {
            'restart': Button(center_x - button_width//2, 270, button_width, button_height, "RESTART", color=(100, 200, 100), hover_color=(150, 255, 150)),
            'menu': Button(center_x - button_width//2, 270 + button_spacing, button_width, button_height, "MAIN MENU", color=(100, 100, 200), hover_color=(150, 150, 255))
        }
        
        # Create buttons for settings menu
        self.settings_buttons = {
            'back': Button(center_x - button_width//2, 450, button_width, button_height, "BACK", color=(200, 100, 100), hover_color=(255, 150, 150))
        }
        
        # Create sliders for settings
        slider_x = center_x - 100
        self.sliders = {
            'speed': Slider(slider_x, 200, 200, 20, 5, 20, 10, "Game Speed"),
            'special_food_chance': Slider(slider_x, 280, 200, 20, 5, 25, 10, "Special Food Chance (%)"),
            'special_food_duration': Slider(slider_x, 360, 200, 20, 15, 60, 30, "Special Food Duration (s)")
        }
        
        self.current_state = 'MAIN'
        self.mouse_pos = (0, 0)
        self.mouse_clicked = False
        self.mouse_down = False
        
    def update(self, mouse_pos, mouse_clicked, mouse_down=False):
        """Update menu state and handle interactions"""
        self.mouse_pos = mouse_pos
        self.mouse_clicked = mouse_clicked
        self.mouse_down = mouse_down
        
        # Update all buttons based on current state
        if self.current_state == 'MAIN':
            for button in self.main_buttons.values():
                button.update(mouse_pos)
        elif self.current_state == 'PAUSE':
            for button in self.pause_buttons.values():
                button.update(mouse_pos)
        elif self.current_state == 'GAME_OVER':
            for button in self.game_over_buttons.values():
                button.update(mouse_pos)
        elif self.current_state == 'SETTINGS':
            for button in self.settings_buttons.values():
                button.update(mouse_pos)
            for slider in self.sliders.values():
                slider.update(mouse_pos, mouse_clicked, mouse_down)
        
        # Handle button clicks
        return self.handle_clicks()
    
    def handle_clicks(self):
        """Handle button clicks and return the action to take"""
        if self.current_state == 'MAIN':
            if self.main_buttons['play'].is_clicked(self.mouse_pos, self.mouse_clicked):
                return 'PLAY'
            elif self.main_buttons['settings'].is_clicked(self.mouse_pos, self.mouse_clicked):
                self.current_state = 'SETTINGS'
                return None
            elif self.main_buttons['quit'].is_clicked(self.mouse_pos, self.mouse_clicked):
                return 'QUIT'
                
        elif self.current_state == 'PAUSE':
            if self.pause_buttons['resume'].is_clicked(self.mouse_pos, self.mouse_clicked):
                return 'RESUME'
            elif self.pause_buttons['menu'].is_clicked(self.mouse_pos, self.mouse_clicked):
                self.current_state = 'MAIN'
                return 'MENU'
                
        elif self.current_state == 'GAME_OVER':
            if self.game_over_buttons['restart'].is_clicked(self.mouse_pos, self.mouse_clicked):
                return 'RESTART'
            elif self.game_over_buttons['menu'].is_clicked(self.mouse_pos, self.mouse_clicked):
                self.current_state = 'MAIN'
                return 'MENU'
                
        elif self.current_state == 'SETTINGS':
            if self.settings_buttons['back'].is_clicked(self.mouse_pos, self.mouse_clicked):
                self.current_state = 'MAIN'
                return None
        
        return None
    
    def get_settings(self):
        """Get current settings values"""
        return {
            'speed': int(self.sliders['speed'].value),
            'special_food_chance': int(self.sliders['special_food_chance'].value),
            'special_food_duration': int(self.sliders['special_food_duration'].value)
        }
    
    def set_state(self, state):
        """Set the current menu state"""
        self.current_state = state
    
    def render(self, score=0, high_score=0):
        """Render the menu based on current state"""
        if self.current_state == 'MAIN':
            self.render_main_menu()
        elif self.current_state == 'PAUSE':
            self.render_pause_menu()
        elif self.current_state == 'GAME_OVER':
            self.render_game_over_menu(score, high_score)
        elif self.current_state == 'SETTINGS':
            self.render_settings_menu()
    
    def render_main_menu(self):
        """Render the main menu"""
        # Background
        self.surface.fill(BLACK)
        
        # Title
        title_text = self.title_font.render("SNAKE GAME", True, WHITE)
        title_rect = title_text.get_rect(center=(WINDOW_SIZE//2, 100))
        self.surface.blit(title_text, title_rect)
        
        # Subtitle
        subtitle_text = self.subtitle_font.render("Use arrow keys to move", True, GRAY)
        subtitle_rect = subtitle_text.get_rect(center=(WINDOW_SIZE//2, 160))
        self.surface.blit(subtitle_text, subtitle_rect)
        
        # Render buttons
        for button in self.main_buttons.values():
            button.render(self.surface)
        
        # Instructions
        instr_text = self.subtitle_font.render("Click buttons or use keyboard shortcuts", True, WHITE)
        instr_rect = instr_text.get_rect(center=(WINDOW_SIZE//2, 450))
        self.surface.blit(instr_text, instr_rect)
    
    def render_pause_menu(self):
        """Render the pause menu"""
        # Semi-transparent overlay
        overlay = pygame.Surface((WINDOW_SIZE, WINDOW_SIZE))
        overlay.set_alpha(128)
        overlay.fill(BLACK)
        self.surface.blit(overlay, (0, 0))
        
        # Pause text
        pause_text = self.title_font.render("PAUSED", True, WHITE)
        pause_rect = pause_text.get_rect(center=(WINDOW_SIZE//2, 100))
        self.surface.blit(pause_text, pause_rect)
        
        # Instructions
        instr_text = self.subtitle_font.render("Press ESC to resume or click buttons", True, WHITE)
        instr_rect = instr_text.get_rect(center=(WINDOW_SIZE//2, 150))
        self.surface.blit(instr_text, instr_rect)
        
        # Render buttons
        for button in self.pause_buttons.values():
            button.render(self.surface)
    
    def render_game_over_menu(self, score, high_score):
        """Render the game over menu"""
        # Semi-transparent overlay
        overlay = pygame.Surface((WINDOW_SIZE, WINDOW_SIZE))
        overlay.set_alpha(128)
        overlay.fill(BLACK)
        self.surface.blit(overlay, (0, 0))
        
        # Game over text
        over_text = self.title_font.render("GAME OVER", True, WHITE)
        over_rect = over_text.get_rect(center=(WINDOW_SIZE//2, 80))
        self.surface.blit(over_text, over_rect)
        
        # Score display
        score_text = self.subtitle_font.render(f"Score: {score}", True, WHITE)
        score_rect = score_text.get_rect(center=(WINDOW_SIZE//2, 130))
        self.surface.blit(score_text, score_rect)
        
        high_score_text = self.subtitle_font.render(f"High Score: {high_score}", True, WHITE)
        high_score_rect = high_score_text.get_rect(center=(WINDOW_SIZE//2, 160))
        self.surface.blit(high_score_text, high_score_rect)
        
        # Render buttons
        for button in self.game_over_buttons.values():
            button.render(self.surface)
        
        # Instructions
        instr_text = self.subtitle_font.render("Press SPACE to restart or click buttons", True, WHITE)
        instr_rect = instr_text.get_rect(center=(WINDOW_SIZE//2, 400))
        self.surface.blit(instr_text, instr_rect)
    
    def render_settings_menu(self):
        """Render the settings menu"""
        # Background
        self.surface.fill(BLACK)
        
        # Title
        title_text = self.title_font.render("SETTINGS", True, WHITE)
        title_rect = title_text.get_rect(center=(WINDOW_SIZE//2, 80))
        self.surface.blit(title_text, title_rect)
        
        # Instructions
        instr_text = self.subtitle_font.render("Drag sliders to adjust game settings", True, GRAY)
        instr_rect = instr_text.get_rect(center=(WINDOW_SIZE//2, 120))
        self.surface.blit(instr_text, instr_rect)
        
        # Render sliders
        for slider in self.sliders.values():
            slider.render(self.surface)
        
        # Render back button
        for button in self.settings_buttons.values():
            button.render(self.surface) 