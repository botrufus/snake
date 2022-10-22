import pygame

class Entity:
    def __init__(self, color, size, position):
        self.color = color
        self.size = size
        self.surface = pygame.Surface(size)
        self.surface.fill(color)
        self.pos = self.surface.get_rect(topleft = position)