from genericpath import exists
import pygame
from direction import Direction
from snakepart import Snakepart
from head import Head

class Snake():

    def __init__(self, color, size, position):
        self.head = Head(color, size, position)
        self.parts = []
    
    def move(self, screenWidth, screenHeight):
        self.head.move()
        self.head.checkOutOfBounds(screenWidth, screenHeight)
        newPos = self.head.lastPos
        for part in self.parts:
            part.lastPos = part.pos
            part.move(newPos)
            part.checkOutOfBounds(screenWidth, screenHeight)
            newPos = part.lastPos

    def createNewPart(self):
        part = Snakepart(self.head.color, self.head.size, (0,0))
        self.parts.append(part)

    def bitSelf(self):
        for part in self.parts: 
            if part.pos.x == self.head.pos.x and part.pos.y == self.head.pos.y:
                return True
        return False