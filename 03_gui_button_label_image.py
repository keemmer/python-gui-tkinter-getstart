from tkinter import *


def basic():
    root = Tk()
    # photo = PhotoImage(file="./image/user_setting.png")
    # Button(root, image=photo).pack()
    user_setting_photo = PhotoImage(file="./image/user_setting.png")
    Button(root, image=user_setting_photo, borderwidth=0).pack(
        side=LEFT, padx=20, pady=15)

    copy_photo = PhotoImage(file="./image/copy.png")
    Button(root, image=copy_photo, borderwidth=0).pack(
        side=LEFT, padx=20, pady=15)

    coffee_photo = PhotoImage(file="./image/coffee.png")
    Button(root, image=coffee_photo, borderwidth=0).pack(
        side=LEFT, padx=20, pady=15)

    root.mainloop()


def adv():
    root = Tk()
    images = ['user_setting', 'copy', 'coffee', 'password', 'login']
    photos = [PhotoImage(file=f'./image/{img}.png') for img in images]
    for p in photos:
        Button(root, image=p, borderwidth=0).pack(
            side=LEFT, padx=20, pady=15)
        Label(root, image=p, borderwidth=0).pack(
            side=LEFT, padx=20, pady=15)

    root.mainloop()


adv()
