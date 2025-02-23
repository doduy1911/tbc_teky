import tkinter as tk
root = tk.Tk()


root.title("menu")
root.geometry("400x400")
menu_bar=tk.Menu(root)

file_tuychon=tk.Menu(menu_bar, tearoff=0)
file_tuychon.add_command(label="Thông Tin")
file_tuychon.add_command(label="danh sách")
# làm thêm một cái menu tương tự

menu_bar.add_cascade(label="Tùy Chọn", menu=file_tuychon)

root.config(menu=menu_bar)
root.mainloop()