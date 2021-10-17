import ctypes, sys
from datetime import datetime,date

from tkinter import *
# from tkinter import tk
from tkinter import ttk

from Components import Filling,Commit,Date


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

    def setHeading(self):
        self.tree.heading('#1', text='S.No',anchor=CENTER)
        self.tree.column("#1", minwidth=0, width=50, stretch=NO)

        self.tree.heading('#2', text='Folder', anchor=CENTER)
        self.tree.column("#2", minwidth=0, width=200, stretch=NO)

        self.tree.heading('#3', text='Changes', anchor=CENTER)
        self.tree.column("#3", minwidth=0, width=80, stretch=NO)

        self.tree.heading('#4', text='Timer', anchor=CENTER)
        self.tree.column("#4", minwidth=0, width=200, stretch=NO)

        self.tree.heading('#5', text='Operation', anchor=CENTER)
        self.tree.column("#5", minwidth=0, width=100, stretch=NO)

        self.tree.heading('#6', text='Status', anchor=CENTER)
        self.tree.column("#6", minwidth=0, width=60, stretch=NO)

    def destory(self):
        self.dashborad.destroy

    def treeStyling(self):
        self.style = ttk.Style()
        self.style.configure("mystyle.Treeview",rowheight=30, highlightthickness=0, bd=0, font=('Calibri', 11)) # Modify the font of the body
        self.style.configure("mystyle.Treeview.Heading", font=('Calibri', 13,'bold')) # Modify the font of the headings
        self.style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders

    def CommitRepo(self,event):
        items = self.tree.selection()
        for item in items:
            main_dics = list(self.GitRefernce.values())[ (int(item[-1]) - 1) ] # self.GitRefernce.item(item, "CommiterRefernce")
            myRepo = main_dics["CommiterRefernce"]
            if myRepo.status.isStatus():
                myRepo.status.status()
                chocie = main_dics["Type"] != "Single";
                myRepo.run(chocie)

        self.loadRow()

    def operationType(self,event):
        item = self.tree.selection()
        for i in item:
            self.changeState_tree(item,4,["Single", "Multiple"])

    def changeState_tree(self,row,index,value):
        temp = list(self.tree.item(row, "values"))
        temp[index] = value[0] if temp[index] != value[0] else value[1]
        temp = tuple(temp)
        self.tree.item(row, values=temp)

        # return temp[index] != value;


    def initialDashborad(self):
        columns = ('#1','#2','#3',"#4","#5",'#6')
        self.treeStyling()

        self.tree = ttk.Treeview(self.dashborad, columns=columns, show='headings',style="mystyle.Treeview")

    # define headings
        self.setHeading()
    #
        self.loadRow()
        self.tree.tag_configure('odd', background='#E8E8E8')
        self.tree.tag_configure('even', background='#DFDFDF')

        self.tree.bind("<<TreeviewSelect>>", self.CommitRepo)
        self.tree.bind("<Double-1>", self.operationType)

        self.tree.pack(fill=None,expand=0)
        self.tree.place(in_=self.dashborad,bordermode=OUTSIDE, anchor=CENTER, relx=.5, rely=.5)

    def loadRow(self):
        for i in self.tree.get_children():
            self.tree.delete(i)

        self.dashborad.update()

        n=1
        for key,value in self.GitRefernce.items():
            temp = value["CommiterRefernce"];
            self.tree.insert('', 'end' ,text=f"{n}",
                             values=(f'{n}', f'{key[0:25]}',f'{len(temp.status.changes)}', f'{value["NextSchdelus"]}',
                                     f'{value["Type"]}',f'{value["Status"]}'),

                             tags = (f'{"odd" if n % 2 == 0 else "even"}'))
            n = n + 1



def main():
    my = date(year=2000, month=12, day=1).weekday()
    print(my)


if __name__ == '__main__':
    obj = AutoCommiter()
    # # obj.newDisplay()
    obj.initialDashborad()
    # main()


    # main.mainloop()


