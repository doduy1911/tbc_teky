import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

# Danh sách lưu trữ thông tin người dùng
users = {}

def register():
    def save_user():
        username = entry_username.get()
        password = entry_password.get()
        gender = gender_var.get()
        avatar_path = lbi_avatar_path.cget("text")
        # Check thông tin đăng ký
        if not username or not password:
            messagebox.showerror("Lỗi", "Tên Đăng Nhập và Mật Khẩu không được để trống!")
            return
        
        if username in users:
            messagebox.showerror("Lỗi", "Tên Đăng Nhập đã tồn tại!")
            return
        # Lưu thông tin người dùng
        users[username] = {"password": password,"gender":gender,"avatar":avatar_path}
        messagebox.showinfo("Thành Công", f"Đăng Ký Thành Công Cho {username}!")
        register_window.destroy()
    def select_avatar():
        file_path = filedialog.askopenfilename(
            title="Chọn Ảnh Đại Diện",
            filetypes=[("Image files", "*.jpg *.jpeg *.png *.gif")]
        )
        if file_path:
            lbi_avatar_path.config(text=file_path)
            img = Image.open(file_path)
            img.thumbnail((100, 100))
            avatar_img = ImageTk.PhotoImage(img)
            lbi_avatar_preview.config(image=avatar_img)
            lbi_avatar_preview.image = avatar_img
   


    # Giao Diện Đăng Ký 

    register_window = tk.Toplevel(root)
    register_window.title("Đăng Ký")
    register_window.geometry("400x450")

    # Frame Chính
    frame_main = tk.Frame(register_window)
    frame_main.pack(pady=10, padx=10, fill="both", expand=True)

    # Giao DIện nhập thông tin đăng ký 
    tk.Label(frame_main, text="Tên Đăng Nhập:").pack(anchor="w", pady=5)
    entry_username = tk.Entry(frame_main)
    entry_username.pack(fill="x", pady=5)

    tk.Label(frame_main, text="Mật Khẩu:").pack(anchor="w", pady=5)
    entry_password = tk.Entry(frame_main, show="*")
    entry_password.pack(fill="x", pady=5)

    # thệm lựa chọn giới tính 
    tk.Label(frame_main, text="Giới Tính:").pack(anchor="w", pady=5)
    gender_var = tk.StringVar(value="Nam") # Giá trị mặc định
    frame_gender = tk.Frame(frame_main)
    frame_gender.pack(fill="x", pady=5)
    tk.Radiobutton(frame_gender, text="Nam", value="Nam", variable=gender_var ).pack(side="left", padx=5)
    tk.Radiobutton(frame_gender, text="Nữ", variable=gender_var,value="Nữ").pack(side="left", padx=5)

    # Khu Vực Chọn Ảnh Đại Diện
    tk.Label(frame_main, text="Ảnh Đại Diện:").pack(anchor="w", pady=5)
    frame_avatar = tk.Frame(frame_main)
    frame_avatar.pack(fill="x", pady=5)

    btn_select_avatar = tk.Button(frame_avatar, text="Chọn Ảnh",command=select_avatar) 
    btn_select_avatar.pack(side="left", padx=5)

    lbi_avatar_path = tk.Label(frame_avatar, text="", anchor="w")
    lbi_avatar_path.pack(side="left", padx=5)

    lbi_avatar_preview = tk.Label(frame_main)
    lbi_avatar_preview.pack(pady=10)

    # Nút Đăng Ký 
    btn_save = tk.Button(frame_main, text="Đăng Ký",command=save_user)
    btn_save.pack(pady=10)

def login():
    #     def check_login():
        username = entry_username.get()
        password = entry_password.get()
        if not username or not password:
            messagebox.showerror("Lỗi", "Tên Đăng Nhập và Mật Khẩu không được để trống!")
            return
        if username in users and users[username]["password"] == password:
            gender=users[username]["gender"]
            messagebox.showinfo("Thành Công", f"Đăng Nhập Thành Công Cho {username}! Giới Tính")
        else:
            messagebox.showerror("Lỗi", "Tên Đăng Nhập hoặc Mật Khẩu không chính xác!")
        

# Tạo Cửa Sổ Chính 
root = tk.Tk()
root.title("Hệ Thống Đăng Nhập")
root.geometry("400x400")

# Giao Diện Chính (Giao DIện Đăng Nhập)

tk.Label(root, text="Tên Đăng Nhập:").pack(pady=5)
entry_username = tk.Entry(root)
entry_username.pack(pady=5)

tk.Label(root, text="Mật Khẩu:").pack( pady=5)
entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=5)

btn_login=tk.Button(root, text="Đăng Nhập",command=login)
btn_login.pack(pady=10)

btn_resgister = tk.Button(root, text="Đăng Ký", command=register)
btn_resgister.pack(pady=10)


root.mainloop()