import pygame
from direction import Direction
from entity import Entity
import copy

class Head(Entity):
    def __init__(self, color, size, position):
        super().__init__(color, size, position)
        self.dir = Direction.NONE
        self.lastPos = position

    def move(self):
        self.lastPos = copy.deepcopy(self.pos)
        if self.dir == Direction.UP:
            self.pos.y -= 1 * self.size[0]
        elif self.dir == Direction.DOWN:
            self.pos.y += 1 * self.size[0]
        elif self.dir == Direction.RIGHT:
            self.pos.x += 1 * self.size[0]
        elif self.dir == Direction.LEFT:
            self.pos.x -= 1 * self.size[0]

    def checkOutOfBounds(self, width, height):
        if self.pos.x >= width:
            self.pos.x = 0
        elif self.pos.y >= height:
            self.pos.y = 0
        elif self.pos.x < 0:
            self.pos.x = width - 20
        elif self.pos.y < 0:
            self.pos.y = height - 20

    def changeDirection(self, key):
        if key == pygame.K_UP and self.dir != Direction.DOWN:
            self.dir = Direction.UP
        elif key == pygame.K_DOWN and self.dir != Direction.UP:
            self.dir = Direction.DOWN
        elif key == pygame.K_RIGHT and self.dir != Direction.LEFT:
            self.dir = Direction.RIGHT
        elif key == pygame.K_LEFT and self.dir != Direction.RIGHT:
            self.dir = Direction.LEFT