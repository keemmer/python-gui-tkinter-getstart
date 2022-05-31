from tkinter import *

root = Tk()
root.option_add("*Font","consolas 18")

tv_bmi = StringVar()

Label(root,text="weight (kg.)").grid(row=0,column=0,sticky="sw",padx=10)
Label(root,text="height (cm.)").grid(row=1,column=0,sticky="sw",padx=10)

w = Scale(root,from_=1,to=100,orient=HORIZONTAL,length=200,width=30)
w.set(50)
w.grid(row=0,column=1)

h = Scale(root,from_=1,to=200,orient=HORIZONTAL,length=200,width=30)
h.set(160)
h.grid(row=1,column=1)

Label(root,textvariable=tv_bmi).grid(row=3,columnspan=2)

root.mainloop()