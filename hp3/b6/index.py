import tkinter as tk
from tkinter import filedialog , messagebox
from PLI import Image , ImageTk

users={}
# logic người đăng ký 
# tạo cửa sổ người đăng ký 
#tạo cửa sổ người đăng nhập
def register():
    def save_user():
        username = entry_username.get()
        password = entry_password.get()
        gender = gender_var.get()
        avatar_path = lbl_avatar_path.cget("text")
        
        if not username or not password:
            messagebox.showerror("Lỗi", "Tên đăng nhập và mật khẩu không được để trống!")
            return
        
        if username in users:
            messagebox.showerror("Lỗi", "Tên đăng nhập đã tồn tại!")
            return
        
        users[username] = {"password": password, "gender": gender, "avatar": avatar_path}
        messagebox.showinfo("Thành công", f"Đăng ký thành công cho {username}!")
        register_window.destroy()

    def select_avatar():
        file_path = filedialog.askopenfilename(
            title="Chọn ảnh đại diện",
            filetypes=[("Image files", "*.jpg *.jpeg *.png *.gif")]
        )
        if file_path:
            lbl_avatar_path.config(text=file_path)
            img = Image.open(file_path)
            img.thumbnail((100, 100))
            avatar_img = ImageTk.PhotoImage(img)
            lbl_avatar_preview.config(image=avatar_img)
            lbl_avatar_preview.image = avatar_img

    # Tạo cửa sổ đăng ký
    register_window = tk.Toplevel(main_window)
    register_window.title("Đăng ký")
    register_window.geometry("400x450")

    # Frame chính
    frame_main = tk.Frame(register_window)
    frame_main.pack(pady=10, padx=10, fill="both", expand=True)

    # Giao diện nhập thông tin
    tk.Label(frame_main, text="Tên đăng nhập:").pack(anchor="w", pady=5)
    entry_username = tk.Entry(frame_main)
    entry_username.pack(fill="x", pady=5)

    tk.Label(frame_main, text="Mật khẩu:").pack(anchor="w", pady=5)
    entry_password = tk.Entry(frame_main, show="*")
    entry_password.pack(fill="x", pady=5)

    # Thêm lựa chọn giới tính
    tk.Label(frame_main, text="Giới tính:").pack(anchor="w", pady=5)
    gender_var = tk.StringVar(value="Nam")  # Giá trị mặc định
    frame_gender = tk.Frame(frame_main)
    frame_gender.pack(fill="x", pady=5)
    tk.Radiobutton(frame_gender, text="Nam", variable=gender_var, value="Nam").pack(side="left", padx=5)
    tk.Radiobutton(frame_gender, text="Nữ", variable=gender_var, value="Nữ").pack(side="left", padx=5)

    # Khu vực chọn ảnh đại diện
    tk.Label(frame_main, text="Ảnh đại diện:").pack(anchor="w", pady=5)
    frame_avatar = tk.Frame(frame_main)
    frame_avatar.pack(fill="x", pady=5)

    btn_select_avatar = tk.Button(frame_avatar, text="Chọn ảnh", command=select_avatar)
    btn_select_avatar.pack(side="left", padx=5)

    lbl_avatar_path = tk.Label(frame_avatar, text="", anchor="w")
    lbl_avatar_path.pack(side="left", padx=5)

    lbl_avatar_preview = tk.Label(frame_main)
    lbl_avatar_preview.pack(pady=10)

    # Nút Đăng ký
    btn_save = tk.Button(frame_main, text="Đăng ký", command=save_user)
    btn_save.pack(pady=10)


def login():
    username = entry_userName.get()
    password = entry_password.get()
    
    if username in users and users[username]["password"] == password:
        gender = users[username]["gender"]
        messagebox.showinfo("Thành công", f"Đăng nhập thành công!\nChào mừng {username} ({gender}).")
    else:
        messagebox.showerror("Lỗi", "Tên đăng nhập hoặc mật khẩu không đúng!")
# tạo cửa sổ chính 
main_window = tk.Tk()
main_window.title("Hệ Thống Đăng Nhập")
main_window.geometry("300x200")

tk.Label(main_window,text="Tên Đăng Nhập").pack(pady=5)
entry_userName = tk.Entry(main_window)
entry_userName.pack(pady=5)

tk.Label(main_window,text="Nhập Mật Khẩu ").pack(pady=5)
entry_password = tk.Entry(main_window , show="*")
entry_password.pack(pady=5)

btn_login = tk.Button(main_window,text="Đăng Nhập", command=login)
btn_login.pack(pady=10)
btn_register = tk.Button(main_window,text="Đăng Ký", command=register)
btn_register.pack(pady=10)

# chạy ứng dụng
main_window.mainloop()