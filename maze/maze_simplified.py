import time
import pygame
import random


def get_random_position():
    return [random.randrange(0, FIELD_SIZE, CELL_SIZE), random.randrange(0, FIELD_SIZE, CELL_SIZE)]


def draw_field(field, field_map):
    for row_index in range(len(field_map)):
        for cell_index in range(len(field_map[row_index])):
            if field_map[row_index][cell_index] == 1:
                row_px_position = row_index * CELL_SIZE
                col_px_position = cell_index * CELL_SIZE
                pygame.draw.rect(field, pygame.color.Color("purple"), (row_px_position, col_px_position, CELL_SIZE, CELL_SIZE))


def generate_field_map(width, height):
    field_map = []
    for i in range(height):
        field_map.append([1] * width)

    return field_map


def configure_field_map(field_map):
    for i in range(len(field_map)):
        for j in range(len(field_map[0])):
            if i % 2 == 1:
                if j % 2 == 0:
                    field_map[i][j] = 1
                else:
                    field_map[i][j] = 0

def get_neighbours(step_map, x, y):
    neighbours = []

    if x + 1 < len(step_map[0]):
        neighbours.append((x + 1, y))

    if x - 1 >= 0:
        neighbours.append((x - 1, y))

    if y + 1 < len(step_map):
        neighbours.append((x, y + 1))

    if y - 1 >= 0:
        neighbours.append((x, y - 1))

    neighbours = [neighbour
                  for neighbour in neighbours
                  if step_map[neighbour[0]][neighbour[1]] == 0]
    return neighbours


def generate_maze(field):
    step_width = len(field) // 2
    step_height = len(field[0]) // 2

    step_map = [step_width * [0] for i in range(step_height)]
    stack = []
    counter = (0, 0)
    step_map[0][0] = 1

    while sum([sum(row) for row in step_map]) < (step_width * step_height):
        neighbours = get_neighbours(step_map, counter[0], counter[1])
        if len(neighbours) > 0:
            stack.append(counter)
            next = random.choice(neighbours)

            diff_x = next[0] - counter[0]
            diff_y = next[1] - counter[1]

            field[counter[0] * 2 + diff_x + 1][counter[1] * 2 + diff_y + 1] = 0
            counter = next
            step_map[counter[0]][counter[1]] = 1
        elif len(stack) != 0:
            counter = stack.pop()

        # else:

        print(step_map)



FIELD_SIZE = 420
CELL_SIZE = 20

pygame.init()
clock = pygame.time.Clock()

field = pygame.display.set_mode([FIELD_SIZE, FIELD_SIZE])

gamer = [1, 1]
endgame = [FIELD_SIZE - 2 * CELL_SIZE, FIELD_SIZE - 2 * CELL_SIZE]
# 1 - wall, 0 - empty

dx = 0
dy = 0
fps = 10

field_map = generate_field_map(21, 21)
configure_field_map(field_map)
generate_maze(field_map)
while True:
    field.fill(pygame.Color("black"))

    gamer_pos_x = gamer[0] * CELL_SIZE
    gamer_pos_y = gamer[1] * CELL_SIZE

    pygame.draw.rect(field, pygame.Color("red"), (gamer_pos_x, gamer_pos_y, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(field, pygame.Color("blue"), (endgame[0], endgame[1], CELL_SIZE, CELL_SIZE))
    draw_field(field, field_map)

    # make a move
    if -1 < (gamer[0] + dx) < (FIELD_SIZE / CELL_SIZE):
        if field_map[gamer[0] + dx][gamer[1]] == 0:
            gamer[0] += dx

    if -1 < (gamer[1] + dy) < (FIELD_SIZE / CELL_SIZE):
        if field_map[gamer[0]][gamer[1] + dy] == 0:
            gamer[1] += dy

    if gamer[0] * CELL_SIZE == endgame[0] and gamer[1] * CELL_SIZE == endgame[1]:
        font = pygame.font.SysFont("Times Now Roman", 50)
        endgame_text = font.render("Перемога!", True, pygame.Color("white"))
        field.blit(endgame_text, (FIELD_SIZE / 2 - 100, FIELD_SIZE / 2 - 20))

    # set up to 0 values where to be placed next
    dx = 0
    dy = 0

    pygame.display.flip()
    clock.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            dx = -1
            dy = 0
        elif key[pygame.K_RIGHT]:
            dx = 1
            dy = 0
        elif key[pygame.K_UP]:
            dx = 0
            dy = -1
        elif key[pygame.K_DOWN]:
            dx = 0
            dy = 1
