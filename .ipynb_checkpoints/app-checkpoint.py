import pygame
successes, failures = pygame.init()
print("{0} successes and {1} failures".format(successes, failures))
screen = pygame.display.set_mode((720, 480)) # Notice the tuple! It's not 2 arguments.
clock = pygame.time.Clock()
FPS = 60