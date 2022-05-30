from tkinter import *

def demo1():

    root = Tk()
    root.option_add("*Font","consolas 18")

    # Label(root,text="mocha", bg="green").pack(side=TOP)
    # Label(root,text="latte",bg="orange").pack(side=TOP)
    # Label(root,text="expresso",bg="purple").pack(side=TOP)

    # Label(root,text="mocha", bg="green").pack(side=TOP,fill=X)
    # Label(root,text="latte",bg="orange").pack(side=TOP,fill=X)
    # Label(root,text="expresso",bg="purple").pack(side=TOP,fill=X)

    # Label(root,text="mocha", bg="green").pack(side=TOP,fill=X, ipadx=40)
    # Label(root,text="latte",bg="orange").pack(side=TOP,fill=X, ipadx=40)
    # Label(root,text="expresso",bg="purple").pack(side=TOP,fill=X, ipadx=40)

    Label(root,text="mocha", bg="green").pack(side=TOP,fill=X, ipadx=40,ipady=20)
    Label(root,text="latte",bg="orange").pack(side=TOP,fill=X, ipadx=40,ipady=20)
    Label(root,text="expresso",bg="purple").pack(side=TOP,fill=X, ipadx=40,ipady=20)

    root.mainloop()

def demo2():

    root = Tk()
    root.option_add("*Font","consolas 18")

    # Label(root,text="mocha", bg="green").pack(side=LEFT,fill=X, ipadx=20,ipady=40,padx=10)
    Label(root,text="mocha", bg="green").pack(side=LEFT,fill=X, ipadx=20,ipady=40,padx=10,pady=50)
    Label(root,text="latte",bg="orange").pack(side=LEFT,fill=X, ipadx=20,ipady=30)
    Label(root,text="expresso",bg="purple").pack(side=LEFT,fill=X, ipadx=20,ipady=20)

    root.mainloop()
def demo3():

    root = Tk()
    root.option_add("*Font","consolas 18")
    menus =["mocha","latte","expresso"]
    colors = ["green","orange","purple"]
    # for i,m in enumerate(menus):
    #     Label(root,text=m, bg=colors[i]).pack(side=LEFT)
    for i,m in enumerate(menus):
        Label(root,text=m, bg=colors[i],width=15).pack(side=LEFT)


    root.mainloop()


if __name__ == "__main__":
    # demo2()
    demo3()
