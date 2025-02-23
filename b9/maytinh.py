import tkinter as tk
from tkinter import messagebox

# tạo cửa sổ chính 
root= tk.Tk()
root.title("Máy Tính ")
root.geometry("400x400")

def on_click(even):
    text = even.widget.cget("text")

#Khung NHập 
entry_var = tk.StringVar()
entry = tk.Entry(root, textvar=entry_var, font=("Arial", 20), justify='right')
entry.pack(fill=tk.BOTH, ipadx=8, ipady=8, padx=10, pady=10)

# khung để nhập phím 
frame = tk.Frame(root)
frame.pack()

# các phím nút
# nút số 7 
btn7 = tk.Button(frame, text="7", font=("Arial", 18), width=5, height=2)
btn7.grid(row=0, column=0, padx=5, pady=5)
btn7.bind("<Button-1>", on_click)


btn8 = tk.Button(frame, text="8", font=("Arial", 18), width=5, height=2)
btn8.grid(row=0, column=1, padx=5, pady=5)
btn8.bind("<Button-1>", on_click)

btn9 = tk.Button(frame, text="9", font=("Arial", 18), width=5, height=2)
btn9.grid(row=0, column=2, padx=5, pady=5)
btn9.bind("<Button-1>", on_click)

# btn_div = tk.Button(frame, text="/", font=("Arial", 18), width=5, height=2)
# btn_div.grid(row=0, column=3, padx=5, pady=5)
# btn_div.bind("<Button-1>", on_click)

btn4 = tk.Button(frame, text="4", font=("Arial", 18), width=5, height=2)
btn4.grid(row=1, column=0, padx=5, pady=5)
btn4.bind("<Button-1>", on_click)

btn5 = tk.Button(frame, text="5", font=("Arial", 18), width=5, height=2)
btn5.grid(row=1, column=1, padx=5, pady=5)
btn5.bind("<Button-1>", on_click)

btn6 = tk.Button(frame, text="6", font=("Arial", 18), width=5, height=2)
btn6.grid(row=1, column=2, padx=5, pady=5)
btn6.bind("<Button-1>", on_click)

# btn_mul = tk.Button(frame, text="*", font=("Arial", 18), width=5, height=2)
# btn_mul.grid(row=1, column=3, padx=5, pady=5)
# btn_mul.bind("<Button-1>", on_click)

btn1 = tk.Button(frame, text="1", font=("Arial", 18), width=5, height=2)
btn1.grid(row=2, column=0, padx=5, pady=5)
btn1.bind("<Button-1>", on_click)

btn2 = tk.Button(frame, text="2", font=("Arial", 18), width=5, height=2)
btn2.grid(row=2, column=1, padx=5, pady=5)
btn2.bind("<Button-1>", on_click)

btn3 = tk.Button(frame, text="3", font=("Arial", 18), width=5, height=2)
btn3.grid(row=2, column=2, padx=5, pady=5)
btn3.bind("<Button-1>", on_click)

root.mainloop()