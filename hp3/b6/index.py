import tkinter as tk
from PIL import Image , ImageTk
from tkinter import filedialog , messagebox

# tạo cửa sổ chính 
root = tk.Tk()
root.title("Hệ Thống Đăng Nhập")
root.geometry("300x200")

# tạo giao diện chính 
users= {}

tk.Label(root,text="Tên Đăng nhập ").pack(pady=5)
entry_userName=tk.Entry(root)
entry_userName.pack(pady=5)

tk.Label(root,text="Mật Khẩu ").pack(pady=5)
entry_password=tk.Entry(root)
entry_password.pack(pady=5)

btn_login=tk.Button(root,text="Đăng Nhập",)
btn_login.pack(pady=10)
btn_register=tk.Button(root,text="Đăng Ký " ).pack(pady=10)

# tạo cửa sổ đăng ký 

register_window=tk.Toplevel(root)
register_window.title("Đăng Ký ")
register_window.geometry("400x450")

# form chính 
frame_main = tk.Frame(register_window)
frame_main.pack(padx=10,pady=10,fill="both", expand=True)

tk.Label(frame_main,text="Tên Đăng Nhập ").pack(anchor="w",pady=5)
entry_userName=tk.Entry(frame_main)
entry_userName.pack(fill="x",pady=5)

tk.Label(frame_main,text="Mật Khẩu " ).pack(anchor="w",pady=5)
entry_password=tk.Entry(frame_main,show="*")
entry_password.pack(fill="x",pady=5)

# Thêm Lựa chọn giới tính 
tk.Label(frame_main,text="Giới Tính ").pack(anchor="w",pady=5)
gender_var = tk.StringVar(value="Nam") # Giá Trị Mặc định là nam 
frame_gender=tk.Frame(frame_main)
frame_gender.pack(fill="x",pady=5)
tk.Radiobutton(frame_gender,text="Nam",variable=gender_var,value="Nam").pack(side="left",padx="5")
tk.Radiobutton(frame_gender,text="Nữ",variable=gender_var,value="Nữ").pack(side="left",padx="5")

#Thêm Ảnh 

tk.Label(frame_main,text="Ảnh Đại Diện")
frame_avatar = tk.Frame(frame_main)
frame_avatar.pack(fill="x",pady="5")

btn_select_avatar = tk.Button(frame_avatar,text="Chọn Ảnh " , )
btn_select_avatar.pack(side="left",padx=5)

lbi_avatar_path= tk.Label(frame_avatar,text="",anchor="w")
lbi_avatar_path.pack(side="left",padx=5)

lbi_avatar_preview = tk.Label(frame_main)
lbi_avatar_preview.pack(pady=10)

btn_save = tk.Button(frame_main,text="Đăng Ký ")
btn_save.pack(pady=10)

def login():
    username = entry_userName.get()
    password = entry_password.get()

    if username in username and users[username]["password"] ==password:
        gender = users[username]["gender"]
        messagebox.showinfo("Thành Công ")
    else:
        messagebox.showerror("Thất bại")


def register():
    def save_user():
        username = entry_userName.get()
        password = entry_password.get()
        gender =  gender_var.get()
        avatar = lbi_avatar_path.cget("text")
        if not username and not password :
            messagebox.showerror("Tên Đăng Nhập Và Mật Khẩu Không Được Để Trống ")
            return
        else:
            messagebox.showerror("Tên Đăng Nhập Và Mật Khẩu Không Chính Xác ")
            return
root.mainloop()
        