from tkinter import *

root = Tk()
root.option_add("*Font","consolas 18")

Label(root,text="weight (kg.)").grid(sticky=E,row=0,column=0,pady=10)
Entry(root,width=10).grid(row=0,column=1)
Label(root,text="height (m.)").grid(sticky=E,row=1,column=0,pady=10)
Entry(root,width=10).grid(row=1,column=1)

Label(root,text="BMI").grid(sticky=E,row=2,column=0,pady=20)
Button(root,text="Calculate").grid(row=3,columnspan=2,pady=20)

root.mainloop()
