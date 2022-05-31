from tkinter import *

feelings = ['vd','d','n','s','vs']
images = [f'./image/{s}.png' for s in feelings]
scores = {s:0 for s in feelings}
# scores = {'vd':0,'d':0,'n':0,'s':0,'vs':0}

def on_click(e):
    global scores
    selected = e.widget["text"]
    # print(selected)
    scores[selected]+=1
    print(scores)

root = Tk()
root.option_add("*Font","consolas 18")


photo = [PhotoImage(file=img) for img in images]
for i in range(len(images)):
    btn = Button(root,image=photo[i],text=feelings[i],borderwidth=0)
    btn.pack(side=LEFT)
    btn.bind("<Button-1>",on_click)

root.mainloop()