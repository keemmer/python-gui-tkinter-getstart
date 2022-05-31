from tkinter import *

male_cnt=0
female_cnt=0
total_cnt=0



root = Tk()
root.option_add("*Font","consolas 18")

tv_male = IntVar()
tv_female = IntVar()
tv_total = StringVar()

def male_click():
    global male_cnt
    global total_cnt
    male_cnt+=1
    total_cnt+=1
    tv_male.set(male_cnt)
    tv_total.set(f'total = {total_cnt}')
def female_click():
    global female_cnt
    global total_cnt
    female_cnt+=1
    total_cnt+=1
    tv_female.set(female_cnt)
    tv_total.set(f'total = {total_cnt}')


Button(root,text="Male",bg="deep sky blue",command=male_click,width=8).grid(row=0,column=0,ipady=20)
Button(root,text="Female",bg="hot pink",command=female_click,width=8).grid(row=0,column=1,ipady=20)
Label(root,textvariable=tv_male,bg="deep sky blue").grid(row=1,column=0,sticky="news")
Label(root,textvariable=tv_female,bg="hot pink").grid(row=1,column=1,sticky="news")
Label(root,textvariable=tv_total,bg="orange").grid(row=2,columnspan=2,sticky="news")



root.mainloop()
