import time
import pygame
from random import randrange

FIELD_SIZE = 900
CELL_SIZE = 50

points = 0

def draw_field2(field):
    field_1_image = pygame.image.load("textures/grass1.png")
    field_1_image = pygame.transform.scale(field_1_image, (CELL_SIZE, CELL_SIZE))

    field_2_image = pygame.image.load("textures/grass2.png")
    field_2_image = pygame.transform.scale(field_2_image, (CELL_SIZE, CELL_SIZE))

    row_counter = 0
    column_counter = 0

    for place_x in range(0, FIELD_SIZE, CELL_SIZE):
        for place_y in range(0, FIELD_SIZE, CELL_SIZE):
            if (row_counter + column_counter) % 2 == 0:
                field.blit(field_1_image, (place_x, place_y))
            else:
                field.blit(field_2_image, (place_x, place_y))

            column_counter += 1

        row_counter += 1
        column_counter = 0


def draw_field(field):
    field_image = pygame.image.load("textures/grass1.png")
    field_image = pygame.transform.scale(field_image, (CELL_SIZE, CELL_SIZE))

    row_counter = 0
    column_counter = 0

    for place_x in range(0, FIELD_SIZE, CELL_SIZE):
        for place_y in range(0, FIELD_SIZE, CELL_SIZE):
            field.blit(field_image, (place_x, place_y))


def draw_board(field):
    board_image = pygame.image.load("textures/grass2.png")
    board_image = pygame.transform.scale(board_image, (CELL_SIZE, CELL_SIZE))

    for place_y in range(0, FIELD_SIZE, CELL_SIZE):
        field.blit(board_image, (0, place_y))
        field.blit(board_image, (FIELD_SIZE - CELL_SIZE, place_y))

        field.blit(board_image, (place_y, 0))
        field.blit(board_image, (place_y, FIELD_SIZE - CELL_SIZE))


def draw_apple(field, apple):
    apple_image = pygame.image.load("textures/fruit.png")
    apple_image = pygame.transform.scale(apple_image, (CELL_SIZE, CELL_SIZE))

    apple_x, apple_y = apple
    field.blit(apple_image, (apple_x, apple_y))


def draw_snake_head(field, snake_pos, direction):
    dx, dy = direction
    x, y = snake_pos[-1]

    head_image = pygame.image.load("textures/head.png")
    head_image = pygame.transform.scale(head_image, (CELL_SIZE, CELL_SIZE))

    if dy == -1 and dx == 0:
        head_image = pygame.transform.rotate(head_image, 90)
    elif dy == 1 and dx == 0:
        head_image = pygame.transform.rotate(head_image, -90)
    elif dy == 0 and dx == -1:
        head_image = pygame.transform.rotate(head_image, 180)

    field.blit(head_image, (x, y))


def draw_snake_body(field, snake):
    snake_body_image = pygame.image.load("textures/body.png")
    snake_body_image = pygame.transform.scale(snake_body_image, (CELL_SIZE, CELL_SIZE))

    for snake_body_pos in snake[1:-1]:
        field.blit(snake_body_image, (snake_body_pos[0], snake_body_pos[1]))


def draw_snake_tail(field, snake):
    if len(snake) <= 1:
        return

    snake_tail_image = pygame.image.load("textures/tail.png")
    snake_tail_image = pygame.transform.scale(snake_tail_image, (CELL_SIZE, CELL_SIZE))

    snake_tail = snake[0]
    snake_before_tail = snake[1]

    if snake_before_tail[0] < snake_tail[0]:
        snake_tail_image = pygame.transform.rotate(snake_tail_image, 180)
    elif snake_before_tail[1] < snake_tail[1]:
        snake_tail_image = pygame.transform.rotate(snake_tail_image, 90)
    elif snake_before_tail[1] > snake_tail[1]:
        snake_tail_image = pygame.transform.rotate(snake_tail_image, -90)

    field.blit(snake_tail_image, (snake_tail[0], snake_tail[1]))


def draw_points(field, points):
    font = pygame.font.SysFont("Time New Roman", 150)
    points_text = font.render(str(points), True, pygame.color.Color("WHITE"))
    field.blit(points_text, (20, 20))


def random_position():
    x = randrange(0, FIELD_SIZE, CELL_SIZE)
    y = randrange(0, FIELD_SIZE, CELL_SIZE)
    return x, y


# 1 - random pos of the snake
snake = [random_position()]
length = 1
# 2 - random pos of the apple
apple = random_position()

pygame.init()
field = pygame.display.set_mode([FIELD_SIZE, FIELD_SIZE])
clock = pygame.time.Clock()

fps = 10

dx = 0
dy = 0

while True:
    # draw_field(field)
    # draw_board(field)
    draw_field2(field)
    # [(pygame.draw.rect(field, pygame.Color("green"), (x, y, CELL_SIZE, CELL_SIZE))) for x, y in snake]
    draw_snake_body(field, snake)
    draw_snake_head(field, snake, (dx, dy))
    draw_snake_tail(field, snake)
    draw_apple(field, apple)
    draw_points(field, points)

    x = snake[-1][0]
    y = snake[-1][1]

    x += dx * CELL_SIZE
    y += dy * CELL_SIZE
    snake.append((x, y))
    snake = snake[-length:]

    # eating apples
    if snake[-1] == apple:
        length += 1
        apple = random_position()
        points += 1

    if x > FIELD_SIZE or x < 0 or y > FIELD_SIZE or y < 0:
        break

    if len(set(snake)) != len(snake):
        break

    pygame.display.flip()
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        key = pygame.key.get_pressed()
        if key[pygame.K_UP]:
            dx = 0
            dy = -1
        elif key[pygame.K_DOWN]:
            dx = 0
            dy = 1
        elif key[pygame.K_LEFT]:
            dx = -1
            dy = 0
        elif key[pygame.K_RIGHT]:
            dx = 1
            dy = 0


