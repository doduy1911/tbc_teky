import pygame
import random

# Khởi tạo pygame
pygame.init()

# Kích thước màn hình
WIDTH, HEIGHT = 300, 600
BLOCK_SIZE = 30
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris")

# Màu sắc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
COLORS = [
    (0, 255, 255),  # Cyan
    (255, 165, 0),  # Orange
    (0, 0, 255),    # Blue
    (255, 255, 0),  # Yellow
    (0, 255, 0),    # Green
    (128, 0, 128),  # Purple
    (255, 0, 0)     # Red
]

# Các hình dạng Tetris
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[0, 1, 0], [1, 1, 1]],  # T
    [[1, 0, 0], [1, 1, 1]],  # L
    [[0, 0, 1], [1, 1, 1]],  # J
    [[0, 1, 1], [1, 1, 0]],  # S
    [[1, 1, 0], [0, 1, 1]]   # Z
]

# Lưới trò chơi
GRID_WIDTH = WIDTH // BLOCK_SIZE
GRID_HEIGHT = HEIGHT // BLOCK_SIZE
grid = [[BLACK for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]


class Piece:
    def __init__(self, shape):
        # Khởi tạo mảnh ghép với hình dạng (shape) được truyền vào
        self.shape = shape
        # Chọn màu ngẫu nhiên từ danh sách COLORS
        self.color = random.choice(COLORS)
        # Đặt vị trí ban đầu của mảnh ghép ở giữa lưới theo chiều ngang
        self.x = GRID_WIDTH // 2 - len(shape[0]) // 2
        # Đặt vị trí ban đầu của mảnh ghép ở trên cùng của lưới
        self.y = 0

    def rotate(self):
        # Xoay mảnh ghép 90 độ theo chiều kim đồng hồ
        self.shape = [list(row) for row in zip(*self.shape[::-1])]


def draw_grid():
    # Vẽ lưới trò chơi
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            # Vẽ từng ô trong lưới với màu tương ứng
            pygame.draw.rect(screen, grid[y][x], (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
            # Vẽ viền màu xám cho từng ô
            pygame.draw.rect(screen, GRAY, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)


def draw_piece(piece):
    # Vẽ mảnh ghép hiện tại lên màn hình
    for y, row in enumerate(piece.shape):
        for x, cell in enumerate(row):
            if cell:  # Nếu ô trong mảnh ghép không rỗng
                # Vẽ ô với màu của mảnh ghép
                pygame.draw.rect(screen, piece.color,
                                 ((piece.x + x) * BLOCK_SIZE, (piece.y + y) * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))


def check_collision(piece, dx=0, dy=0):
    # Kiểm tra xem mảnh ghép có va chạm với lưới hoặc biên không
    for y, row in enumerate(piece.shape):
        for x, cell in enumerate(row):
            if cell:  # Nếu ô trong mảnh ghép không rỗng
                new_x = piece.x + x + dx  # Tính vị trí mới theo trục x
                new_y = piece.y + y + dy  # Tính vị trí mới theo trục y
                # Kiểm tra va chạm với biên hoặc ô đã có màu trong lưới
                if new_x < 0 or new_x >= GRID_WIDTH or new_y >= GRID_HEIGHT or grid[new_y][new_x] != BLACK:
                    return True  # Có va chạm
    return False  # Không có va chạm


def merge_piece(piece):
    # Hợp nhất mảnh ghép vào lưới
    for y, row in enumerate(piece.shape):
        for x, cell in enumerate(row):
            if cell:  # Nếu ô trong mảnh ghép không rỗng
                # Gán màu của mảnh ghép vào lưới tại vị trí tương ứng
                grid[piece.y + y][piece.x + x] = piece.color


def clear_lines():
    # Xóa các hàng đầy đủ trong lưới
    global grid
    # Giữ lại các hàng có ít nhất một ô màu đen (chưa đầy)
    grid = [row for row in grid if any(cell == BLACK for cell in row)]
    # Thêm các hàng trống (màu đen) ở trên cùng để giữ nguyên chiều cao lưới
    while len(grid) < GRID_HEIGHT:
        grid.insert(0, [BLACK for _ in range(GRID_WIDTH)])


# Khởi tạo đồng hồ để kiểm soát tốc độ khung hình
clock = pygame.time.Clock()

# Tạo mảnh ghép hiện tại (ngẫu nhiên chọn từ danh sách SHAPES)
current_piece = Piece(random.choice(SHAPES))

# Biến điều khiển vòng lặp trò chơi
running = True

# Thời gian để kiểm soát tốc độ rơi của mảnh ghép
fall_time = 0

# Vòng lặp chính của trò chơi
while running:
    # Xóa màn hình bằng màu đen
    screen.fill(BLACK)

    # Vẽ lưới trò chơi
    draw_grid()

    # Vẽ mảnh ghép hiện tại
    draw_piece(current_piece)

    # Xử lý các sự kiện (như nhấn phím hoặc đóng cửa sổ)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Nếu người dùng đóng cửa sổ
            running = False  # Thoát vòng lặp trò chơi
        if event.type == pygame.KEYDOWN:  # Nếu người dùng nhấn phím
            # Di chuyển mảnh ghép sang trái nếu không có va chạm
            if event.key == pygame.K_LEFT and not check_collision(current_piece, dx=-1):
                current_piece.x -= 1
            # Di chuyển mảnh ghép sang phải nếu không có va chạm
            if event.key == pygame.K_RIGHT and not check_collision(current_piece, dx=1):
                current_piece.x += 1
            # Di chuyển mảnh ghép xuống nhanh hơn nếu không có va chạm
            if event.key == pygame.K_DOWN and not check_collision(current_piece, dy=1):
                current_piece.y += 1
            # Xoay mảnh ghép nếu không có va chạm
            if event.key == pygame.K_UP:
                current_piece.rotate()
                # Nếu xoay gây va chạm, hoàn tác xoay bằng cách xoay ngược lại 3 lần
                if check_collision(current_piece):
                    current_piece.rotate()
                    current_piece.rotate()
                    current_piece.rotate()

    # Tăng thời gian rơi của mảnh ghép
    fall_time += clock.get_rawtime()

    # Giới hạn tốc độ khung hình (30 FPS)
    clock.tick(30)

    # Nếu thời gian rơi vượt quá 500ms, mảnh ghép sẽ tự động rơi xuống
    if fall_time > 500:
        # Nếu không có va chạm, mảnh ghép rơi xuống một ô
        if not check_collision(current_piece, dy=1):
            current_piece.y += 1
        else:
            # Nếu có va chạm, hợp nhất mảnh ghép vào lưới
            merge_piece(current_piece)
            # Xóa các hàng đầy đủ
            clear_lines()
            # Tạo mảnh ghép mới
            current_piece = Piece(random.choice(SHAPES))
            # Nếu mảnh ghép mới va chạm ngay khi xuất hiện, kết thúc trò chơi
            if check_collision(current_piece):
                running = False
        # Đặt lại thời gian rơi
        fall_time = 100

    # Cập nhật màn hình
    pygame.display.flip()

# Thoát pygame khi trò chơi kết thúc
pygame.quit()