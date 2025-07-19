import pygame
from game import Game
from utils import WINDOW_SIZE

def main():
    pygame.init()
    
    window_height = WINDOW_SIZE + 40  # Extra space for status bar
    surface = pygame.display.set_mode((WINDOW_SIZE, window_height))
    pygame.display.set_caption('Snake Game - Enhanced Edition')
    
    game = Game(surface)
    game.run()
    
    pygame.quit()

if __name__ == '__main__':
    main() 