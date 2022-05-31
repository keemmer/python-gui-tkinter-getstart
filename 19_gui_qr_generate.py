import qrcode
from tkinter import *
from PIL import Image, ImageTk


def create_qrcode(text):
    qr = qrcode.QRCode()
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    return img


def demo():
    def on_click(e):
        input_text = txt.get("0.0", "end-1c")
        print(input_text)
        img = create_qrcode(input_text).resize((300, 300))
        imgTk = ImageTk.PhotoImage(img)
        qr.configure(image=imgTk)
        qr.image = imgTk

    root = Tk()
    root.option_add("*Font", "consolas 18")
    root.title("QR code generator")

    Label(root, text="Enter text").grid(row=0, column=0)
    txt = Text(root, height=4, width=30, fg="green")
    txt.grid(row=1, column=0)
    btn = Button(root, text="create QR Code", bg="gold")
    btn.grid(row=2, column=0)
    btn.bind("<Button-1>", on_click)

    qr = Label(root)
    qr.grid(row=0, column=1, rowspan=3)

    root.mainloop()


if __name__ == "__main__":
    # create_qrcode("kemmer").show()
    demo()
