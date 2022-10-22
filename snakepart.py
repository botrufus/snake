import pygame
from direction import Direction
from entity import Entity

class Snakepart(Entity):
    def __init__(self, color, size, position):
        super().__init__(color, size, position)
        self.lastPos = position

    def move(self, pos):
        self.lastPos = self.pos
        self.pos = pos

    def checkOutOfBounds(self, width, height):
        if self.pos.x >= width:
            self.pos.x = 0
        elif self.pos.y >= height:
            self.pos.y = 0
        elif self.pos.x < 0:
            self.pos.x = width - 20
        elif self.pos.y < 0:
            self.pos.y = height - 20