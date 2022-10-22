from turtle import back
import pygame
from snake import Snake
from apple import Apple
from pygame.locals import *
import random

WIDTH = 400
HEIGHT = 400
BLACK = [0,0,0]
WHITE = [255,255,255]

def appleEaten(snake, apple):
    return snake.head.pos.x == apple.pos.x and snake.head.pos.y == apple.pos.y

def rndmPos():
    x = random.randint(0, WIDTH / 20 - 1) * 20
    y = random.randint(0, HEIGHT / 20 - 1) * 20
    return x,y

def generateApple(snake) -> Apple:
    done = False
    while not done:
        done = True
        (x,y) = rndmPos()
        if x == snake.head.pos.x and y == snake.head.pos.y:
            done = False
            continue
        for part in snake.parts:
            if x == part.pos.x and y == part.pos.y:
                done = False
                break

    return Apple([255, 0,0], (20,20), (x, y))

def renderScore(screen, score):
    if pygame.font:
        text = "Score " + str(score)
        font = pygame.font.Font(None, 64)
        text = font.render(text, True, WHITE)
        textpos = text.get_rect(topleft = (10,10))
        background = pygame.Surface((WIDTH, 50))
        background.fill(BLACK)
        screen.blit(background, textpos, textpos)
        screen.blit(text, textpos)


def main():
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT + 50))
    score = 0
    pygame.font.init()

    renderScore(screen, score)

    background = pygame.Surface((WIDTH, HEIGHT))
    background.fill(BLACK)

    playingSurface = pygame.Surface((WIDTH, HEIGHT))
    playingSurface.fill(BLACK)

    snake = Snake(WHITE, (20, 20), (WIDTH / 2, HEIGHT / 2))
    apple = generateApple(snake)
    playingSurface.blit(apple.surface, apple.pos)
    playingSurface.blit(snake.head.surface, snake.head.pos)

    screen.blit(playingSurface, (0, 50))
    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                snake.head.changeDirection(event.key)
                break

        playingSurface.blit(background, snake.head.pos, snake.head.pos)
        for part in snake.parts:
            playingSurface.blit(background, part.pos, part.pos)
        snake.move(WIDTH, HEIGHT)
        playingSurface.blit(snake.head.surface, snake.head.pos)
        for part in snake.parts:
            playingSurface.blit(part.surface, part.pos)
        
        if appleEaten(snake, apple):
            apple = generateApple(snake)
            playingSurface.blit(apple.surface, apple.pos)
            snake.createNewPart()
            score += 1
            renderScore(screen, score)
        
        if snake.bitSelf():
            running = False
        
        screen.blit(playingSurface, (0, 50))
        pygame.display.flip()
        clock.tick(2 + len(snake.parts))


if __name__ == "__main__":
    pygame.init()
    main()
    pygame.quit()
