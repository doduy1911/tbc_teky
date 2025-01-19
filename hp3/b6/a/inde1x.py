import tkinter as tk

# Tạo cửa sổ chính
root = tk.Tk()
root.title("menu")
root.geometry("400x300")
# tạo menu
menu_bar = tk.Menu(root)


# tạo menu con cho tuychon
filemenu=tk.Menu(menu_bar, tearoff=0)
filemenu.add_command(label="trang chủ")
filemenu.add_command(label="thông tin người dùng")
filemenu.add_separator()
filemenu.add_command(label="đăng xuất", command=root.quit)

menu_bar.add_cascade(label="tùy chọn" ,menu=filemenu)
menu_bar.add_cascade(label="trợ giúp")

root.config(menu=menu_bar)
root.mainloop()