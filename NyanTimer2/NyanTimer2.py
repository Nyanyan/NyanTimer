import tkinter as tk

root= tk.Tk()
root.geometry('130x200')
button10 = tk.Button(root, text='Profile #1',command=push).pack()
button11 = tk.Button(root, text='Profile #2',command=push2).pack()
button12 = tk.Button(root, text='Profile #3',command=push3).pack()
sleep(0.01)
root.mainloop()