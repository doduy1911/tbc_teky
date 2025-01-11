import tkinter as tk
from tkinter import messagebox
root = tk.Tk()


tk.Label(root , text="Tài Khoản ").grid(row=0,column=0 , padx=10,pady=10)
userName = tk.Entry(root)
userName.grid(row=0,column=1,padx=10,pady=10)

tk.Label(root,text="Mật Khẩu").grid(row =1 ,column=1,padx=10,pady=10)
matKhau = tk.Entry(root)
matKhau.grid(row=1 , column=1 ,padx=10,pady=10)


root.mainloop()