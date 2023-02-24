import random

import pygame
import sys

pygame.init()
CELL_SIZE = 10

class Maze():
    def __init__(self):
        pygame.display.set_caption("Maze")

        self.clock = pygame.time.Clock()

        self.screen_res = [700, 500]
        self.screen = pygame.display.set_mode(self.screen_res)

        self.node_sprites = pygame.sprite.Group()
        self.node_list = []

        # w/o time

        self.createGrid()
        while True:
            self.loop()

    def loop(self):
        self.checkKeyPressed()
        self.drawField()
        pygame.display.update()


    def drawField(self):
        self.screen.fill(0)

        self.node_sprites.draw(self.screen)
        self.node_sprites.update()


    def checkKeyPressed(self):
        direction = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    direction = "up"
                elif event.key == pygame.K_DOWN:
                    direction = "down"
                elif event.key == pygame.K_LEFT:
                    direction = "left"
                elif event.key == pygame.K_RIGHT:
                    direction = "right"


    def createGrid(self):
        col_pos = 20
        row_pos = 20
        num = 0

        col_count = 50
        row_count = 50

        color = [random.choice(range(255)), random.choice(range(255)), random.choice(range(255))]

        for y in range(row_count):
            for x in range(col_count):
                Node(self, [col_pos, row_pos], num, color)
                col_pos += CELL_SIZE
                row_pos += CELL_SIZE


class Node(pygame.sprite.Sprite):
    def __init__(self, game, pos, num, color):
        self.game = game

        self.game.node_sprites.add(self)
        self.game.node_list.append(self)

        self.pos = pos
        self.num = num
        self.color = color

        self.solver_on = False

        self.image = pygame.Surface([10, 10])
        self.image.fill(0)
        self.rect = self.image.get_rect(topleft = self.pos)

        self.walls = {
            'up': False,
            'down': False,
            'right': False,
            'left': False
        }
        self.neighbors = {}

Maze()