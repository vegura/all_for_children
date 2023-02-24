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


FIELD_SIZE = 380
CELL_SIZE = 20

pygame.init()
clock = pygame.time.Clock()

field = pygame.display.set_mode([FIELD_SIZE, FIELD_SIZE])

gamer = [1, 1]
# 1 - wall, 0 - empty
field_map = [
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]


def generate_field_map(width, height):
    field = []
    for i in range(height):
        field.append([1] * width)

    return field


def configure_field_map(field_map):
    for i in range(0, len(field_map)):
        for j in range(1, len(field_map[0])):
            if i % 2 == 1:
                if j % 2 == 0:
                    field_map[i][j] = 1
                else:
                    field_map[i][j] = 0


def get_neighbours(step_map, pos_x, pos_y):
    neighbours = []
    if pos_x + 1 < len(step_map):
        neighbours.append((pos_x + 1, pos_y))

    if pos_x - 1 > 0:
        neighbours.append((pos_x - 1, pos_y))

    if pos_y + 1 < len(step_map):
        neighbours.append((pos_x, pos_y + 1))

    if pos_y - 1 > 0:
        neighbours.append((pos_x, pos_y - 1))

    # print("-> ", neighbours, end=", ")
    neighbours = [neighbour
                  for neighbour in neighbours
                  if step_map[neighbour[0]][neighbour[1]] == 0]
    return neighbours


def maze_generator(field):
    step_width = len(field) // 2
    step_height = len(field[0]) // 2

    step_map = [step_height * [0] for i in range(step_width)]

    stack = []
    counter = (0, 0)
    step_map[counter[0]][counter[1]] = 1
    while sum([sum(row) for row in step_map]) < (step_width * step_height):
        neighbours = get_neighbours(step_map, counter[0], counter[1])
        if len(neighbours) != 0:
            stack.append(counter)
            next = random.choice(neighbours)

            # deleting wall
            diff_x = next[0] - counter[0]
            diff_y = next[1] - counter[1]
            print("diff is: ", diff_x, " ", diff_y, end=", ")
            print("wall del: ", counter[1] * 2 + diff_x, "-", counter[0] * 2 + diff_y, end="\t")
            field[counter[1] * 2 + diff_x ][counter[0] * 2 + diff_y] = 0

            counter = next
            print("next is: ", next)
            step_map[counter[0]][counter[1]] = 1

        elif len(stack) != 0:
            counter = stack.pop()

        # else:


dx = 0
dy = 0
fps = 10
field_map = generate_field_map(19, 19)
configure_field_map(field_map)
maze_generator(field_map)
print(field_map)

while True:
    field.fill(pygame.Color("black"))

    gamer_pos_x = gamer[0] * CELL_SIZE
    gamer_pos_y = gamer[1] * CELL_SIZE

    pygame.draw.rect(field, pygame.Color("red"), (gamer_pos_x, gamer_pos_y, CELL_SIZE, CELL_SIZE))
    draw_field(field, field_map)

    # make a move
    if -1 < (gamer[0] + dx) < (FIELD_SIZE / CELL_SIZE):
        if field_map[gamer[0] + dx][gamer[1]] == 0:
            gamer[0] += dx

    if -1 < (gamer[1] + dy) < (FIELD_SIZE / CELL_SIZE):
        if field_map[gamer[0]][gamer[1] + dy] == 0:
            gamer[1] += dy

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
