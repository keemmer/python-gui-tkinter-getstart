from tkinter import *



root = Tk()
root.option_add("*Font","consolas 18")

# Button(root,text="phone").pack()
# Button(root,text="phone",bg="red",fg="white").pack()
# Button(root,text="computer",fg="blue").pack()
Button(root,text="phone",width=20).pack()
Button(root,text="camera",bg="orange",fg="white").pack(fill=X)
Button(root,text="computer",fg="blue",padx=30).pack()
Button(root,text="computer",fg="blue",bd=10,width=20).pack()
Button(root,text="computer",fg="blue",bd=10,state=DISABLED).pack()
Button(root,text="green\ntea",fg="green",bd=10,state=DISABLED).pack()

photo = PhotoImage(file="./image/lamp.png")
# Button(root,text="LED 01",image=photo).pack()
Button(root,text="LED 01",image=photo,compound=LEFT).pack()
Button(root,text="LED 01",image=photo,compound=LEFT,padx=20).pack()
Button(root,text="LED 01",image=photo,compound=RIGHT).pack()
Button(root,text="LED 01",image=photo,compound=TOP,pady=20).pack()
Button(root,text="LED 01",image=photo,compound=TOP,).pack()
Button(root,text="LED 01",image=photo,compound=BOTTOM).pack()


root.mainloop()
