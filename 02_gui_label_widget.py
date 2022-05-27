from tkinter import *


root = Tk()
root.title("Label")
root.option_add('*Font','consolas 18')


Label(root,text="keemmer",fg="red").pack(anchor=W)
Label(root,text="keemmer",bg="green").pack(anchor=E)
Label(root,text="keemmer",fg="green").pack()
Label(root,text="keemmer",fg="white",bg="red").pack()
Label(root,text="keemmer",fg="white",bg="red").pack()
Label(root,text="สวัสดี",fg="green").pack(pady=10)
Label(root,text="banana",fg="red",bg="yellow",width=15).pack()
Label(root,text="coconut",fg="white",bg="red").pack(fill=X)
Label(root,text="keemmer",fg="white",bg="red").pack()
Label(root,text="green\ntea",fg="white",bg="red").pack(fill=X)
Label(root,text="happy birthdays to you happy birthdays to you happy birthdays to you",fg="gold",bg="red").pack()
Label(root,text="happy birthdays to you happy birthdays to you happy birthdays to you",fg="gold",bg="orange", wraplength=400).pack()
Label(root,text="happy birthdays to you happy birthdays to you happy birthdays to you",fg="white",bg="orange", wraplength=400).pack(fill=X)
Label(root,text="happy birthdays to you happy birthdays to you happy birthdays to you\n\nkeemmer",fg="white",bg="purple", wraplength=700).pack(fill=X)
Label(root,text="happy birthdays to you happy birthdays to you happy birthdays to you\n\nkeemmer",fg="white",bg="pink", wraplength=700,justify=LEFT).pack(fill=X)
Label(root,text="happy birthdays to you happy birthdays to you happy birthdays to you\n\nkeemmer",fg="white",bg="dark green", wraplength=700,justify=RIGHT).pack(fill=X)

root.mainloop()