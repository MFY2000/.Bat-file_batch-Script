from tkinter import *
from PIL import ImageTk,Image
from Code.Controller.Image.ImagePicker import ImagePicker


class Cus_Button:
    def __init__(self,RepeWith, borderwidth = 0,  padx = 0, pady = 0,
                    highlightbackground = "#008618", highlightcolor = "white", height = 20, width = 30,
                    highlightthickness = 0, text = "",  underline = False, wraplength = True, bg = "red",
                    image = None,place = [0, 355] ):

        self.activebackground = bg
        self.highlightbackground = highlightbackground
        if image == None:
            image =  PhotoImage(file = r"../../Image/Icon/Icon_image.png",)

        self.btn = Button(RepeWith,
                          borderwidth=borderwidth, bg = bg,
                          activebackground = bg,
                          padx = padx, pady = pady,
                          highlightbackground = highlightbackground,
                          highlightcolor = highlightcolor,
                          highlightthickness = highlightthickness,
                          text = text,  underline = underline,
                          wraplength = wraplength, command=RepeWith.destroy,
                          image = image,
                          height = height, width = width)

        self.btn.place(x = place[1], y = place[0])

        self.btn.bind('<Enter>', self.change_on_hovering)
        self.btn.bind('<Leave>', self.return_to_normalstate)



    def change_on_hovering(self, event):
        self.btn['bg'] = self.highlightbackground

    def return_to_normalstate(self, event):
        self.btn['bg'] = self.activebackground


class button2:
    # def __init__(self, head, size, path):
    #     Canvasbtn = Canvas(head, width=size[0], height=size[1], bg="white", highlightthickness=0, borderwidth=0)
    #     Canvasbtn.place(x=925, y=450)
    #     img = (ImagePicker(imagePath=path.ButtonBackground, width=size[0]-2, height=size[1]-2)).image
    #     Canvasbtn.create_image(0, 0, anchor=NW, image=img)
    #     Canvasbtn.create_text((size[0]/2), (size[1]/2), text="HELLO WORLD", fill="white", font=('Helvetica 10 bold'))
    #
    #     self.btn = Canvasbtn
    #     print("hello")


    def getButton(self, head, size, path):
        Canvasbtn = Canvas(head, width=size[0], height=size[1], bg="white", highlightthickness=0, borderwidth=0)
        Canvasbtn.place(x=925, y=450)
        img = (ImagePicker(imagePath=path, width = size[0] - 2, height = size[1] - 2)).image
        Canvasbtn.create_image(0, 0, anchor=NW, image=img)
        Canvasbtn.create_text((size[0] / 2), (size[1] / 2), text="Commit", fill="#D1D1D1", font=('Helvetica 10 bold'))
        return Canvasbtn

    def getImage(self, path, size):
        img = (ImagePicker(imagePath=path, width=size[0] - 2, height=size[1] - 2)).image
        return img