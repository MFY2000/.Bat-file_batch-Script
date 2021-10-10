import ctypes, sys

# library for bulding ui
from tkinter import *
# from tkinter import tk
from tkinter import ttk

from Components import Filling


class AutoCommiter:
    sizes = {"App": [840,600],"screen": [],"cord": [] }

    def __init__(self):
        self.dashborad = Tk()
        self.sizes["screen"] = [self.dashborad.winfo_screenwidth() , self.dashborad.winfo_screenheight()]
        self.sizes["cord"] = [self.calpostion(0), self.calpostion(1)]
        self.background = PhotoImage(file="images/background.png")
        self.GitRefernce = Filling.main_Runner()

        self.Display()
        self.initialDashborad()

        self.dashborad.mainloop()

    def Display(self):
        self.dashborad.geometry(f'{self.getSize("App", 0)}x{self.getSize("App", 1)}+'
                                f'{self.getSize("cord", 0)}+{self.getSize("cord", 1)}')

        self.dashborad.resizable(0, 0)
        background_label = Label(self.dashborad, image = self.background)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.dashborad.title("Git")
    def calpostion(self, iteration):
        return int((self.sizes.get("screen")[iteration] / 2) - (self.sizes.get("App")[iteration] / 2))
    def getSize(self, key, i):
        return (self.sizes.get(key)[i])
    def destory(self):
        self.dashborad.destroy

    def treeStyling(self):
        self.style = ttk.Style()
        self.style.configure("mystyle.Treeview",rowheight=30, highlightthickness=0, bd=0, font=('Calibri', 11)) # Modify the font of the body
        self.style.configure("mystyle.Treeview.Heading", font=('Calibri', 13,'bold')) # Modify the font of the headings
        self.style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders


    def initialDashborad(self):
        # self.dashborad.columnconfigure(0, weight=2)
        columns = ('#1', '#2', '#3',"#4","#5")
        self.treeStyling()

        tree = ttk.Treeview(self.dashborad, columns=columns, show='headings',style="mystyle.Treeview")

        # define headings
        tree.heading('#1', text='S.No',anchor=CENTER)
        tree.column("#1", minwidth=0, width=50, stretch=NO)

        tree.heading('#2', text='Folder', anchor=CENTER)
        tree.column("#2", minwidth=0, width=150, stretch=NO)

        tree.heading('#3', text='Timer', anchor=CENTER)
        tree.column("#3", minwidth=0, width=150, stretch=NO)

        tree.heading('#4', text='Operation', anchor=CENTER)
        tree.column("#4", minwidth=0, width=150, stretch=NO)

        tree.heading('#5', text='', anchor=CENTER)



        # generate sample data
        contacts = []

        for n in len(self.GitRefernce):
            if n % 2 == 0 :
                temp = "odd"
            else:
                temp = "even"

            tree.insert('', 'end' ,text=f"{n}", values=(f'{n}', f'last {n}', '4:24 am',f"{n*n}"), tags = (f'{temp}'))


        tree.tag_configure('odd', background='#E8E8E8')
        tree.tag_configure('even', background='#DFDFDF')

        tree.pack(fill=None,expand=0)
        tree.place(in_=self.dashborad,bordermode=OUTSIDE, anchor=CENTER, relx=.5, rely=.5)

if __name__ == '__main__':
    obj = AutoCommiter()
    # obj.newDisplay()
    obj.initialDashborad()
    # main.mainloop()


