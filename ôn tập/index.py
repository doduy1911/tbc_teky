import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Danh sách lưu tài khoản (giả lập database)
users = {"admin": "1"}  # Tên đăng nhập cố định

def register():
    messagebox.showerror("Lỗi", "Không thể đăng ký tài khoản mới!")

def login():
    username = entry_username.get()
    password = entry_password.get()
    
    if users.get(username) == password:
        messagebox.showinfo("Thành công", "Đăng nhập thành công!")
    else:
        messagebox.showerror("Lỗi", "Tên người dùng hoặc mật khẩu không đúng!")

# Tạo giao diện
root = tk.Tk()
root.title("Đăng nhập")
root.geometry("300x200")

# Thêm ảnh nền
bg_image = Image.open("a.jpg")  # Đổi tên ảnh nền nếu cần
bg_image = bg_image.resize((300, 200))
bg_photo = ImageTk.PhotoImage(bg_image)
background_label = tk.Label(root, image=bg_photo)
background_label.place(relwidth=1, relheight=1)

tk.Label(root, text="Tên đăng nhập:", bg="lightgray").pack()
entry_username = tk.Entry(root)
entry_username.insert(0, "admin")  # Gán tên đăng nhập cố định
entry_username.config(state="disabled")
entry_username.pack()

tk.Label(root, text="Mật khẩu:", bg="lightgray").pack()
entry_password = tk.Entry(root, show="*")
entry_password.pack()

tk.Button(root, text="Đăng nhập", command=login).pack()

root.mainloop()
