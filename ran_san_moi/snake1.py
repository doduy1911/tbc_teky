import pygame as pg
import random
pg.init()
screen = pg.display.set_mode((400,400))
pg.display.set_caption("rắn săn mồi")

snake_part= 20 
x=200
y=200

x_change=y_change=0

body_snak = [] 
lenght = 1

food_X=random.randint(0,19)*snake_part
food_y=random.randint(0,19)*snake_part

clock= pg.time.Clock()
speed=3
def check_vc():
    if x<0 or x>400 or y<0 or y>400 or (x,y) in body_snak[:-1]:
        return False
    return True
score=height_score=0
def score_view():
    font=pg.font.Font(None,36)
    if gameplay:
        score_txt = font.render("Điểm của bạn là :{score}")
        screen.blit(score_txt,(0,0))
        # điểm cao nhất của bạn
gameplay = True
while True:
    for teacherDuy in pg.event.get():
        if teacherDuy.type == pg.QUIT:
            pg.quit()
        if teacherDuy.type == pg.KEYDOWN:
            if teacherDuy.key == pg.K_RIGHT:
                x_change+=snake_part
                y_change=0
            elif teacherDuy.key == pg.K_LEFT:
                x_change-=snake_part
                y_change=0
        
            elif teacherDuy.key == pg.K_DOWN:
                x_change=0
                y_change+=snake_part

            elif teacherDuy.key == pg.K_UP:
                x_change=0
                y_change-=snake_part
    screen.fill((0,0,0))
    if gameplay:
        x+=x_change
        y+=y_change
        body_snak.append((x,y))

        if len(body_snak ) > lenght:
            del body_snak[0]

        if x==food_X and y==food_y:
            length+=1
            score+=1
            if score>hight_score:hight_score=score
            # ramdum lại mồi 
            food_x = random.randint(0,19)*sanke_part
            food_y = random.randint(0,19)*sanke_part
    else:
        x=200
        y=200
        x_change=y_change=0
        body_snak=[]
        lenght=1
    pg.display.update()         