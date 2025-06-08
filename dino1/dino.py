# import thư viện python 
import pygame
pygame.init()
clock = pygame.time.Clock()
# tiêu đề

pygame.display.set_caption("dino game")
icon=pygame.image.load(r'dino/assets/dinosaur.png')
screen=pygame.display.set_mode((600,300))
# lấy hình ảnh nên 
bg=pygame.image.load(r'dino/assets/background.jpg')
tree = pygame.image.load(r'dino/assets/tree.png')
dino = pygame.image.load(r'dino/assets/dinosaur.png')
# tọa độ ban đầu

bg_x,bg_y=0,0
tree_x,tree_y=550,230
dino_x,dino_y=0,230
x_def = 5
y_def=7
jum=False
score,hscore=0,0
gameplay = True
def checkvc():
    if dino_hcn.colliderect(tree_hcn):
        return False
    return True

# Đưa Điểm vào game
game_font = pygame.font.Font(r'dino/04B_19.TTF', 20)
def score_view():
    if gameplay:
        score_txt = game_font.render(f'Score: {int(score)}',True,(255,0,0))
        screen.blit(score_txt,(10,10))
    else:
        score_txt = game_font.render(f'Score: {int(score)}',True,(255,0,0))
        screen.blit(score_txt,(10,10))

runing=True
while runing:
    # chỉnh fps
    clock.tick(60)
    for even in pygame.event.get():
        if even.type == pygame.QUIT:
            runing=False
        if even.type==pygame.KEYDOWN:
            if even.key==pygame.K_SPACE and gameplay:
                if dino_y==230:
                    jum = True
            if even.key==pygame.K_SPACE and gameplay==False:
                gameplay=True
    if gameplay == True:
        # bg
        bg_hcn=screen.blit(bg,(bg_x,bg_y))
        bg2_hcn=screen.blit(bg,(bg_x+600,bg_y))
        bg_x-=x_def
        if bg_x==-600: bg_x=0


        tree_hcn=screen.blit(tree,(tree_x,tree_y))
        tree_x-=x_def
        if tree_x==-20: tree_x=550


        dino_hcn=screen.blit(dino,(dino_x,dino_y))

        # nhảy 
        if dino_y >=80 and jum:
            dino_y-=y_def
        else:
            jum=False

        # xử lý dino tụt xuống 
        if dino_y<230 and jum==False:
            dino_y+=y_def
        score+=0.01
        if hscore < score : hscore=score
        gameplay=checkvc()
        score_view()
    else:
        bg_x,bg_y = 0,0
        tree_x,tree_y=550,230
        dino_x,dino_y=0,230
        score=0
        score_view()
        bg_hcn=screen.blit(bg,(bg_x,bg_y))
        tree_hcn=screen.blit(tree,(tree_x,tree_y))
        dino_hcn=screen.blit(dino,(dino_x,dino_y))



    pygame.display.update()       