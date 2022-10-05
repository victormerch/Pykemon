import pygame
pygame.init()

screen = pygame.display.set_mode((720, 480)) # Notice the tuple! It's not 2 arguments.
clock = pygame.time.Clock()
FPS = 60