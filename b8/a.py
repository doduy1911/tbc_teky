import tkinter as tk
root = tk.Tk()


root.title("form a ")
root.geometry("400x400")
menu_bar=tk.Menu(root)

def windowA ():
    window2 = tk.Toplevel()
    window2.title("Cửa Sổ 1 ")
    window2.geometry("300*300")
    btnA = tk.Button(windowA, text='Next', command=windowB) 
    btnA.pack(padx= 5, pady=5)
 
def windowB():
    window3 = tk.Toplevel()
    window3.title("Cửa Sổ 2 ")
    window3.geometry("300*300")
    btnB = tk.Button(windowB, text='Next', command=windowA)
    btnB.pack(padx= 2, pady=2)


btnC = tk.Button(root, text='Next', command=windowA)
btnC.pack(padx= 2, pady=2)
btnd = tk.Button(root, text='Next', command=windowB)
btnd.pack(padx= 2, pady=2)

root.mainloop()