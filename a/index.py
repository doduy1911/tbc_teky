import tkinter as tk
from tkinter import messagebox, Scrollbar
from PIL import Image, ImageTk
import os

def load_image_from_file(file_path, size=None):
    try:
        img = Image.open(file_path)
        if size:
            img = img.resize(size)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"Lỗi khi tải ảnh {file_path}: {e}")
        return None

def open_cart():
    cart_window = tk.Toplevel(root)
    cart_window.title("Giỏ Hàng")
    cart_window.geometry("600x500")
    
    frame = tk.Frame(cart_window)
    frame.pack(fill=tk.BOTH, expand=True)
    
    canvas = tk.Canvas(frame)
    scrollbar = Scrollbar(frame, orient=tk.VERTICAL, command=canvas.yview)
    scrollable_frame = tk.Frame(canvas)
    
    scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    
    tk.Label(scrollable_frame, text="Giỏ hàng của bạn:", font=("Arial", 18, "bold")).pack(pady=10)
    
    for product in cart_items:
        tk.Label(scrollable_frame, text=product, font=("Arial", 14)).pack()
    
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

def add_to_cart(product):
    cart_items.append(product)
    messagebox.showinfo("Thông báo", f"{product} đã được thêm vào giỏ hàng")

def open_menu():
    menu_window = tk.Toplevel(root)
    menu_window.title("Menu Sản Phẩm")
    menu_window.geometry("900x800")
    
    # Tạo một label để hiển thị ảnh nền
    bg_label = tk.Label(menu_window)
    bg_label.place(relwidth=1, relheight=1)  # Đặt label chiếm toàn bộ cửa sổ
    
    # Hàm cập nhật ảnh nền
    def update_bg():
        global menu_bg_image  # Giữ tham chiếu ảnh để không bị xóa khỏi bộ nhớ
        width = menu_window.winfo_width()  # Lấy chiều rộng hiện tại của cửa sổ
        height = menu_window.winfo_height()  # Lấy chiều cao hiện tại của cửa sổ
        menu_bg_image = load_image_from_file("a/a.jpg", size=(width, height))  # Tải lại ảnh với kích thước mới
        if menu_bg_image:
            bg_label.config(image=menu_bg_image)  # Cập nhật ảnh nền
            bg_label.image = menu_bg_image  # Giữ tham chiếu ảnh

    # Gọi hàm cập nhật ảnh nền ngay lần đầu tiên
    update_bg()
    
    # Liên kết sự kiện thay đổi kích thước cửa sổ với hàm cập nhật ảnh nền
    menu_window.bind("<Configure>", lambda e: update_bg())
    
    # Phần còn lại của code để hiển thị menu
    frame = tk.Frame(menu_window)
    frame.pack(fill=tk.BOTH, expand=True)
    
    canvas = tk.Canvas(frame)
    scrollbar = Scrollbar(frame, orient=tk.VERTICAL, command=canvas.yview)
    scrollable_frame = tk.Frame(canvas)
    
    scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    
    canvas.create_window((0, 0), window=scrollable_frame, anchor="n")
    canvas.configure(yscrollcommand=scrollbar.set)
    
    tk.Label(scrollable_frame, text="Danh sách sản phẩm:", font=("Arial", 18, "bold")).pack(pady=10)
    
    product_details = [
        ("Sản phẩm 1", "100,000đ", "a/a.jpg"),
        ("Sản phẩm 2", "200,000đ", "images/product2.jpg"),
        ("Sản phẩm 3", "300,000đ", "images/product3.jpg"),
        ("Sản phẩm 4", "400,000đ", "images/product4.jpg"),
        ("Sản phẩm 5", "500,000đ", "images/product5.jpg"),
        ("Sản phẩm 6", "600,000đ", "images/product6.jpg"),
        ("Sản phẩm 7", "700,000đ", "images/product7.jpg"),
        ("Sản phẩm 8", "800,000đ", "images/product8.jpg"),
        ("Sản phẩm 9", "900,000đ", "images/product9.jpg"),
        ("Sản phẩm 10", "1,000,000đ", "images/product10.jpg")
    ]
    
    product_images = []
    
    grid_frame = tk.Frame(scrollable_frame)
    grid_frame.pack()
    
    for index, (product, price, image_path) in enumerate(product_details):
        frame = tk.Frame(grid_frame, relief=tk.RAISED, borderwidth=2)
        frame.grid(row=index//4, column=index%4, padx=20, pady=20)
        
        img = load_image_from_file(image_path, size=(200, 200))
        if img:
            product_images.append(img)
            img_label = tk.Label(frame, image=img)
            img_label.image = img
            img_label.pack()
        else:
            tk.Label(frame, text="[Không có ảnh]", font=("Arial", 12, "italic")).pack()
        
        tk.Label(frame, text=product, font=("Arial", 16, "bold")).pack()
        tk.Label(frame, text=price, font=("Arial", 14)).pack()
        tk.Button(frame, text="Đặt hàng", font=("Arial", 14), command=lambda p=product: add_to_cart(p), background="red").pack()
    
    tk.Button(scrollable_frame, text="Xem Giỏ Hàng", font=("Arial", 16), command=open_cart).pack(pady=10)
    
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

def login():
    username = entry_username.get()
    password = entry_password.get()
    if username == "admin" and password == "123":
        messagebox.showinfo("Đăng nhập thành công", "Chào mừng, " + username + "!")
        open_menu()
    else:
        messagebox.showerror("Lỗi", "Sai tên đăng nhập hoặc mật khẩu")

root = tk.Tk()
root.title("Đăng nhập")
root.geometry("700x600")

login_bg = load_image_from_file("images/login_bg.jpg", size=(700, 600))
if login_bg:
    bg_label = tk.Label(root, image=login_bg)
    bg_label.image = login_bg
    bg_label.place(relwidth=1, relheight=1)

cart_items = []

tk.Label(root, text="Tên đăng nhập:", font=("Arial", 14)).pack(pady=5)
entry_username = tk.Entry(root, font=("Arial", 14))
entry_username.pack(pady=5)

tk.Label(root, text="Mật khẩu:", font=("Arial", 14)).pack(pady=5)
entry_password = tk.Entry(root, show="*", font=("Arial", 14))
entry_password.pack(pady=5)

tk.Button(root, text="Đăng nhập", font=("Arial", 14), command=login).pack(pady=10)
tk.Button(root, text="Giỏ Hàng", font=("Arial", 14), command=open_cart).pack(pady=5)

root.mainloop()
