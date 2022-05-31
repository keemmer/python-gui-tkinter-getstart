from tkinter import *

root = Tk()
root.option_add("*Font","consolas 18")

def on_drag(e):
    color_hex = f'#{sc[0].get():02X}{sc[1].get():02X}{sc[2].get():02X}'
    tv_rgb.set(color_hex)
    lbl_color["bg"]=color_hex

tv_rgb = StringVar()
rgb = ['red','green','blue']
sc = []

for i,c in enumerate(rgb):
    Label(root,text=c).grid(row=i,column=0,sticky="sw",padx=10)
    w = Scale(root,from_=0,to=255,orient=HORIZONTAL,length=255,width=30,fg=c)
    w.grid(row=i,column=1)
    w.bind("<B1-Motion>",on_drag)
    w.bind("<Button-1>",on_drag)
    sc.append(w)


lbl_color = Label(root,textvariable=tv_rgb)
lbl_color.grid(row=3,columnspan=2,sticky="news")

root.mainloop()