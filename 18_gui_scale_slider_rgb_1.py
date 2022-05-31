from tkinter import *

root = Tk()
root.option_add("*Font","consolas 18")

def on_drag(e):
    color_hex = f'#{r.get():02X}{g.get():02X}{b.get():02X}'
    tv_rgb.set(color_hex)
    lbl_color["bg"]=color_hex



tv_rgb = StringVar()

Label(root,text="red").grid(row=0,column=0,sticky="sw",padx=10)
Label(root,text="green").grid(row=1,column=0,sticky="sw",padx=10)
Label(root,text="blue").grid(row=2,column=0,sticky="sw",padx=10)

r = Scale(root,from_=0,to=255,orient=HORIZONTAL,length=255,width=30,fg="red")
r.grid(row=0,column=1)
r.bind("<B1-Motion>",on_drag)
r.bind("<Button-1>",on_drag)

g = Scale(root,from_=0,to=255,orient=HORIZONTAL,length=255,width=30,fg="green")
g.grid(row=1,column=1)
g.bind("<B1-Motion>",on_drag)
g.bind("<Button-1>",on_drag)

b = Scale(root,from_=0,to=255,orient=HORIZONTAL,length=255,width=30,fg="blue")
b.grid(row=2,column=1)
b.bind("<B1-Motion>",on_drag)
b.bind("<Button-1>",on_drag)

lbl_color = Label(root,textvariable=tv_rgb)
lbl_color.grid(row=3,columnspan=2,sticky="news")

root.mainloop()