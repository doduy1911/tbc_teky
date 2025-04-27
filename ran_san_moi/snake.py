import pygame as pg
import random
pg.init()

screen = pg.display.set_mode((400,400))
pg.display.set_caption("snake Game")

# var
sanke_part = 20 
x=200
y=200

x_change=y_change = 0

body_snake = []
length = 1 

# create_fooot
food_x = random.randint(0,19)*sanke_part
food_y = random.randint(0,19)*sanke_part

# snake speed
clock = pg.time.Clock()
speed = 3

# def fun
def check_vc():
    if x<0 or x>400 or y<0 or y>400 or(x,y) in body_snake[:-1]:
        return False
    return True

score=hight_score=0
def score_view():
    font=pg.font.Font(None,36)
    if gameplay:
        score_txt =font.render(f'Score :{score}',True,(255,255,255))
        screen.blit(score_txt,(0,0))
        hscore_txt =font.render(f'hightScore :{hight_score}',True,(255,255,255))
        screen.blit(hscore_txt,(170,0))

    else:
        note_txt =font.render(f'Press space to play a game :{score}',True,(255,255,255))
        screen.blit(note_txt,(0,0))


gameplay = True
while True:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            pg.quit()
        # snake_move
        if e.type == pg.KEYDOWN:
            if e.key==pg.K_LEFT:
                x_change-=sanke_part
                y_change=0
        
            elif e.key == pg.K_RIGHT:
                x_change+=sanke_part
                y_change=0
            
            elif e.key == pg.K_UP:
                x_change=0
                y_change-=sanke_part
            elif e.key == pg.K_DOWN:
                x_change=0
                y_change+=sanke_part
            elif e.key == pg.K_SPACE:
                gameplay=True
            

    # clear screen
    screen.fill((0,0,0))
    score_view()
    if gameplay:
        # update pisition sanke_part
        x+=x_change
        y+=y_change
        # add snake part
        body_snake.append((x,y))
        # remvo snake
        if len(body_snake)> length:
            del body_snake[0]
        # check snake ear foood
        if x==food_x and y==food_y:
            length+=1
            score+=1
            if score>hight_score:hight_score=score
            # ramdum lại mồi 
            food_x = random.randint(0,19)*sanke_part
            food_y = random.randint(0,19)*sanke_part
        # vẽ lại thân rắn
        for x,y in body_snake:
            pg.draw.rect(screen,(255,255,255),(x,y,sanke_part,sanke_part))
        # draw foood
            pg.draw.rect(screen,(255,0,0),(food_x,food_y,sanke_part,sanke_part))

        gameplay=check_vc()
    else:
            # reset
            x=200
            y=200
            x_change=y_change = 0
            body_snake = []
            length=1
            score=1
               
        


           


    pg.display.update()
    clock.tick(speed)
