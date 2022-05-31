from tkinter import *


interests = ["Music", "Book", "Movie", "Photography", "Game", "Travel"]

root = Tk()
root.option_add("*Font", "consolas 18")

chks = [BooleanVar() for i in interests]


def on_click():
    #    for i, chk in enumerate(chks):
    #     #    print(chk.get())
    #         if chk.get() == True:
    #            print(interests[i])
    lst = [interests[i] for i,chk in enumerate(chks) if chk.get() == True]
    print(lst)
    print(",".join(lst))


Label(root, text="Your interests", bg="gold").pack()

for i, s in enumerate(interests):
    Checkbutton(root, text=s, variable=chks[i]).pack(anchor=W)


Button(root, text="sumit", command=on_click).pack()

root.mainloop()
