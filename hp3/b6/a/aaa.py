import tkinter as tk

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Ví dụ Frame")
root.geometry("400x300")

# Tạo một frame
frame_main = tk.Frame(root, bg="lightblue")
frame_main.pack(padx=10, pady=10, fill="both", expand=True)

# Thêm một nhãn vào frame
label = tk.Label(frame_main, text="Đây là Frame chính", bg="lightblue", font=("Arial", 16))
label.pack(pady=20)

# Chạy ứng dụng
root.mainloop()
