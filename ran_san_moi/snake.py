import pygame as pg
import random
pg.init()

screen = pg.display.set_mode((400, 400))
pg.display.set_caption("Thầy Duy Đẹp Trai")

# Variables
snake_part = 20
x = 200
y = 200
x_change = y_change = 0

body_snake = []
length = 1

# Food
food_x = random.randint(0, 19) * snake_part
food_y = random.randint(0, 19) * snake_part

# Clock & Speed
clock = pg.time.Clock()
speed = 5

# Scores
score = 0
high_score = 0

# Game state
gameplay = True

# Functions
def check_vc():
    if x < 0 or x >= 400 or y < 0 or y >= 400 or (x, y) in body_snake[:-1]:
        return False
    return True

def score_view():
    font = pg.font.Font(None, 36)
    if gameplay:
        score_txt = font.render(f'Score: {score}', True, (255, 255, 255))
        screen.blit(score_txt, (10, 10))
        hscore_txt = font.render(f'High Score: {high_score}', True, (255, 255, 255))
        screen.blit(hscore_txt, (200, 10))
    else:
        note_txt = font.render('Press SPACE to play again', True, (255, 255, 255))
        screen.blit(note_txt, (30, 180))

# Game loop
while True:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            pg.quit()
            exit()
        if e.type == pg.KEYDOWN:
            if e.key == pg.K_LEFT and x_change == 0:
                x_change = -snake_part
                y_change = 0
            elif e.key == pg.K_RIGHT and x_change == 0:
                x_change = snake_part
                y_change = 0
            elif e.key == pg.K_UP and y_change == 0:
                x_change = 0
                y_change = -snake_part
            elif e.key == pg.K_DOWN and y_change == 0:
                x_change = 0
                y_change = snake_part
            elif e.key == pg.K_SPACE:
                if not gameplay:
                    # Reset
                    x = 200
                    y = 200
                    x_change = y_change = 0
                    body_snake = []
                    length = 1
                    score = 0
                    gameplay = True

    screen.fill((0, 0, 0))
    score_view()

    if gameplay:
        x += x_change
        y += y_change

        body_snake.append((x, y))
        if len(body_snake) > length:
            del body_snake[0]

        if x == food_x and y == food_y:
            length += 1
            score += 1
            if score > high_score:
                high_score = score
            food_x = random.randint(0, 19) * snake_part
            food_y = random.randint(0, 19) * snake_part

        for part in body_snake:
            pg.draw.rect(screen, (255, 255, 255), (part[0], part[1], snake_part, snake_part))

        pg.draw.rect(screen, (255, 0, 0), (food_x, food_y, snake_part, snake_part))

        gameplay = check_vc()

    pg.display.update()
    clock.tick(speed)
