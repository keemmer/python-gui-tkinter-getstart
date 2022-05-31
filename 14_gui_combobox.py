from tkinter import *
from tkinter import ttk
from datetime import date

def on_click(e):
    print(cbo_day.get(),cbo_month.get(),cbo_year.get())
    mm = month_list.index(cbo_month.get()) + 1
    bd = date(int(cbo_year.get()),mm,int(cbo_day.get()))
    print(bd)

root = Tk()
root.option_add("*Font","consolas 18")


month_list = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

# cbo_day = ttk.Combobox(root,value=list(range(1,32)),width=3)
cbo_day = ttk.Combobox(root,value=list(range(1,32)),width=3,state='readonly')
cbo_day.current(1)
cbo_day.pack(side=LEFT)

cbo_month = ttk.Combobox(root,value=month_list,width=4,state='readonly')
cbo_month.current(1)
cbo_month.pack(side=LEFT)

cbo_year = ttk.Combobox(root,value=list(range(2000,2012)),width=5)
cbo_year.current(0)
cbo_year.pack(side=LEFT)

btn = Button(root,text='submit')
btn.pack()
btn.bind("<Button-1>",on_click)


root.mainloop()