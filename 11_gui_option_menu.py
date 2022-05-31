from tkinter import *

root = Tk()
root.option_add("*Font", "consolas 18")
# contries = "Thailand", "Japan", "Korea"]
contries = {"Thailand":"TH", "Japan":"JP", "Korea":"KR"}


def on_click(e):
    print(selectOpt.get())
    # tv_strings.set(f'You selected : {selectOpt.get()}')
    tv_strings.set(f'You selected : {selectOpt.get()} ({contries[selectOpt.get()]})')


selectOpt = StringVar()
selectOpt.set("Thailand")
om = OptionMenu(root, selectOpt, *contries)
om.config(width=15)
om.grid(row=0, column=0)

btn = Button(root, text="select", bg="orange")
btn.grid(row=0, column=1)
btn.bind("<Button-1>", on_click)

tv_strings = StringVar()
tv_strings.set("You selected : -")
Label(root, textvariable=tv_strings).grid(row=1, columnspan=2)


root.mainloop()
