import tkinter as tk
from PIL import Image, ImageTk

# Tạo cửa sổ Tkinter
root = tk.Tk()
root.title("Hiển thị ảnh trong Tkinter")

# Mở ảnh bằng Pillow
image = Image.open("a/a.jpg")
photo = ImageTk.PhotoImage(image)

# Tạo một nhãn để chứa ảnh
label = tk.Label(root, image=photo)
label.pack()

# Chạy vòng lặp chính của Tkinter
root.mainloop()