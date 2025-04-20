import pygame
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Dino Game")
icon = pygame.image.load(r'assets\dinosaur.png')
screen = pygame.display.set_mode((600, 300))

# Hình ảnh
bg = pygame.image.load(r'assets\background.jpg')
tree = pygame.image.load(r'assets\tree.png')
dino = pygame.image.load(r'assets\dinosaur.png')

# Tọa độ ban đầu
bg_x, bg_y = 0, 0
tree_x, tree_y = 550, 230
dino_x, dino_y = 30, 230
x_def = 5
y_def = 7
jum = False
gameplay = True

# Font cho chữ "Game Over"
font = pygame.font.SysFont('comicsansms', 40)
score = 0
scored = False 

def checkvc(dino_rect, tree_rect):
    return not dino_rect.colliderect(tree_rect)

running = True
while running:
    clock.tick(60)

    for even in pygame.event.get():
        if even.type == pygame.QUIT:
            running = False
        if even.type == pygame.KEYDOWN:
            if even.key == pygame.K_SPACE and gameplay:
                if dino_y == 230:
                    jum = True

    if gameplay:
        # Vẽ background
        screen.blit(bg, (bg_x, bg_y))
        screen.blit(bg, (bg_x + 600, bg_y))
        bg_x -= x_def
        if bg_x == -600:
            bg_x = 0

        # Vẽ cây
        tree_hcn = screen.blit(tree, (tree_x, tree_y))
        tree_x -= x_def
        if tree_x == -20:
            tree_x = 550

        # Vẽ khủng long
        dino_hcn = screen.blit(dino, (dino_x, dino_y))

        # Nhảy
        if dino_y >= 80 and jum:
            dino_y -= y_def
        else:
            jum = False

        if dino_y < 230 and not jum:
            dino_y += y_def

        # Kiểm tra va chạm
        gameplay = checkvc(dino_hcn, tree_hcn)

        # Cộng điểm nếu cây vừa vượt qua dino mà không va chạm
        if tree_x + tree.get_width() < dino_x and not scored:
            score += 1
            scored = True  # đã ghi điểm cho cây này rồi

        # Reset cờ ghi điểm nếu cây chạy vòng lại
        if tree_x > dino_x:
            scored = False


        score_text = font.render(f"Score: {score}", True, (0, 0, 0))
        screen.blit(score_text, (10, 10))




    else:
        # Vẽ lại nền để làm sạch
        screen.blit(bg, (0, 0))
        # Hiện chữ "Game Over"
        over_text = font.render("GAME OVER", True, (255, 0, 0))
        screen.blit(over_text, (180, 130))
        score_text = font.render(f"Score: {score}", True, (0, 0, 0))
        screen.blit(score_text, (10, 10))


    pygame.display.update()
