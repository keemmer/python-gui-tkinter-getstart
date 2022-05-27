import tkinter as tk

root = tk.Tk()
root.option_add("*Font","consolas 20")
root.title("Setting")
# tk.Label(root,text="Hello word!").grid()

for i in range(10):
    tk.Label(root,text="Hello word!").grid()


root.mainloop()