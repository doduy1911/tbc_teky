import tkinter as tk
from tkinter import messagebox

def on_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(str(entry_var.get()))
            entry_var.set(result)
        except Exception as e:
            messagebox.showerror("Lỗi", "Biểu thức không hợp lệ")
            entry_var.set("")
    elif text == "C":
        entry_var.set("")
    else:
        entry_var.set(entry_var.get() + text)

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Máy Tính")
root.geometry("300x400")

# Khung nhập
entry_var = tk.StringVar()
entry = tk.Entry(root, textvar=entry_var, font=("Arial", 20), justify='right')
entry.pack(fill=tk.BOTH, ipadx=8, ipady=8, padx=10, pady=10)

# Khung chứa các nút
frame = tk.Frame(root)
frame.pack()

# Tạo các nút bấm riêng lẻ
btn7 = tk.Button(frame, text="7", font=("Arial", 18), width=5, height=2)
btn7.grid(row=0, column=0, padx=5, pady=5)
btn7.bind("<Button-1>", on_click)

btn8 = tk.Button(frame, text="8", font=("Arial", 18), width=5, height=2)
btn8.grid(row=0, column=1, padx=5, pady=5)
btn8.bind("<Button-1>", on_click)

btn9 = tk.Button(frame, text="9", font=("Arial", 18), width=5, height=2)
btn9.grid(row=0, column=2, padx=5, pady=5)
btn9.bind("<Button-1>", on_click)

btn_div = tk.Button(frame, text="/", font=("Arial", 18), width=5, height=2)
btn_div.grid(row=0, column=3, padx=5, pady=5)
btn_div.bind("<Button-1>", on_click)

btn4 = tk.Button(frame, text="4", font=("Arial", 18), width=5, height=2)
btn4.grid(row=1, column=0, padx=5, pady=5)
btn4.bind("<Button-1>", on_click)

btn5 = tk.Button(frame, text="5", font=("Arial", 18), width=5, height=2)
btn5.grid(row=1, column=1, padx=5, pady=5)
btn5.bind("<Button-1>", on_click)

btn6 = tk.Button(frame, text="6", font=("Arial", 18), width=5, height=2)
btn6.grid(row=1, column=2, padx=5, pady=5)
btn6.bind("<Button-1>", on_click)

btn_mul = tk.Button(frame, text="*", font=("Arial", 18), width=5, height=2)
btn_mul.grid(row=1, column=3, padx=5, pady=5)
btn_mul.bind("<Button-1>", on_click)

btn1 = tk.Button(frame, text="1", font=("Arial", 18), width=5, height=2)
btn1.grid(row=2, column=0, padx=5, pady=5)
btn1.bind("<Button-1>", on_click)

btn2 = tk.Button(frame, text="2", font=("Arial", 18), width=5, height=2)
btn2.grid(row=2, column=1, padx=5, pady=5)
btn2.bind("<Button-1>", on_click)

btn3 = tk.Button(frame, text="3", font=("Arial", 18), width=5, height=2)
btn3.grid(row=2, column=2, padx=5, pady=5)
btn3.bind("<Button-1>", on_click)

btn_sub = tk.Button(frame, text="-", font=("Arial", 18), width=5, height=2)
btn_sub.grid(row=2, column=3, padx=5, pady=5)
btn_sub.bind("<Button-1>", on_click)

btn_clear = tk.Button(frame, text="C", font=("Arial", 18), width=5, height=2)
btn_clear.grid(row=3, column=0, padx=5, pady=5)
btn_clear.bind("<Button-1>", on_click)

btn0 = tk.Button(frame, text="0", font=("Arial", 18), width=5, height=2)
btn0.grid(row=3, column=1, padx=5, pady=5)
btn0.bind("<Button-1>", on_click)

btn_equal = tk.Button(frame, text="=", font=("Arial", 18), width=5, height=2)
btn_equal.grid(row=3, column=2, padx=5, pady=5)
btn_equal.bind("<Button-1>", on_click)

btn_add = tk.Button(frame, text="+", font=("Arial", 18), width=5, height=2)
btn_add.grid(row=3, column=3, padx=5, pady=5)
btn_add.bind("<Button-1>", on_click)

# Chạy chương trình
root.mainloop()
