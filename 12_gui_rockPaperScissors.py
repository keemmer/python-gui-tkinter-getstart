from tkinter import *

import random







def game():
    root = Tk()
    root.option_add("*Font", "consolas 18")

    shapes = ["rock","paper","scissors"]
    p1_shapes = [PhotoImage(file=f'./image/{img}.png') for img in shapes]

    p1_stat={"wins":0,"losses":0,"ties":0}

    tv_result = StringVar()
    tv_stat = StringVar()
       
    def rule(p1_shape, p2_shape):
        if (p1_shape == p2_shape):
            p1_stat["ties"]+=1
            return "tied"
        elif (p1_shape == "rock" and p2_shape == "scissors") or (p1_shape == "paper" and p2_shape == "rock") or (p1_shape == "scissors" and p2_shape == "paper"):
            p1_stat["wins"]+=1
            return "p1 won"
        else:
            p1_stat["losses"]+=1
            return "p1 lost"

    def on_click(e):
        p1_shapes =e.widget["text"]
        p2_shapes = random.choice(shapes)
        result = rule(p1_shapes, p2_shapes)
        print(result)
        tv_result.set(f'p1:{p1_shapes} - p2:{p2_shapes} = {result}')
        tv_stat.set(f'{p1_stat["wins"]} win,{p1_stat["losses"]} lossed, {p1_stat["ties"]} ties')
 
   

    f1 = Frame(root)
    f1.grid(row=0,column=0)
    for i in range(len(shapes)):
        w = Button(f1,image=p1_shapes[i],text=shapes[i],borderwidth=0)
        w.pack(side=LEFT,padx=20)
        w.bind("<Button-1>",on_click)

    f2 = Frame(root)
    f2.grid(row=1,column=0)
    Label(f2,textvariable=tv_result,width=40).pack()
    Label(f2,textvariable=tv_stat,bg="gold",width=40).pack()

    root.mainloop()

if __name__ == "__main__":
    # print(rule("rock","paper"))
    # print(rule("rock","scissors"))
    # print(rule("rock","rock"))

    game()
