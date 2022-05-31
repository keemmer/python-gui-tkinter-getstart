from tkinter import *

root = Tk()
root.option_add("*Font","consolas 18")


def on_select():
    print(v_gender.get())
showIndicator = True
v_gender = StringVar()
v_gender.set("f")
Radiobutton(root, text="male", value="m",variable=v_gender,fg="deep sky blue",indicatoron=showIndicator,command=on_select).pack(side=LEFT,padx=20)
Radiobutton(root, text="female", value="f",variable=v_gender,fg="hot pink",indicatoron=showIndicator,command=on_select).pack(side=LEFT)

root.mainloop()
