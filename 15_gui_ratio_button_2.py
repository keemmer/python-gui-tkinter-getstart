from tkinter import *

d = {"Thai":"th","Japan":"jp","Korean":"kr","Chinese":"cn","French":"fr","Australia":"au","america":"us"}
showIndicator = False

def on_select(e):
    print(e.widget["text"],e.widget["value"])


root = Tk()
root.option_add("*Font","consolas 18")

tv_code = StringVar()
tv_code.set("th")
for k,v in d.items():
    r = Radiobutton(root,text=k,value=v,variable=tv_code,width=11,indicatoron=showIndicator)
    r.pack(anchor=W,side=LEFT)
    r.bind("<Button-1>",on_select)
root.mainloop()
