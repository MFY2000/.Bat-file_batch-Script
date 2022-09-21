from tkinter import *

from Code.Controller.Commit import Committer
from Code.Controller.Image.ImagePicker import ImagePicker
from Code.Screen.Component.Button.Cus_Btn import *
from Code.Model.Paths import *
from Code.Controller.FileValidation import *

from tkinter import ttk
import csv, datetime
from datetime import datetime
data = list()
my_game = None

def readFile():
    with open(r"../../../log.csv", 'r') as file:
        csv_file = csv.DictReader(file, fieldnames=None, restkey=None, restval=None, dialect='excel')
        i = 1
        for row in csv_file:
            populateTable(i,dict(row))
            data.append(dict(row))
            i += 1

def populateTable(index,data):
    isSafe = isFile(data["Address"])
    # laseCommit(data["last Commit"])
    my_game.insert(parent='', index='end', iid=index, text='', values=(data["Name"], 0))

# def laseCommit(timeCommit):
#     print(timeCommit)
#     time_1 = datetime.strftime(timeCommit, '%m/%d/%y %H:%M:%S')
#     time_2 = datetime.now()
#
#     time_interval = time_1 - time_2
#     print(time_interval)



def uploadOldData():
    with open(r'../../../log.csv', 'w', newline='') as file:
        fieldnames = ['Name', 'Address', "last Commit", "total Commit"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        for item in data:
            name = item[(item.rfind("\\")+1):(len(item))]
            writer.writerow({'Address': item, 'Name': name,
                             "last Commit": datetime.datetime.now(), "total Commit":0 })


app = Tk()

# app screen size
window_height = 600
window_width = 1080

#window screen Size
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()

#get
x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

#
app.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

# Image resize Code




# Object used in appx
path = ImagePath()

# change title bar text
app.wm_title("Git Commiter")

# change title bar style
app.overrideredirect(True)

# Bounded the screen
app.minsize(window_width+1,window_height+1)
app.maxsize(window_width+1,window_height+1)

# Change Icon Done title Bar
app.iconbitmap(default="../../Image/Icon/app_Icon.ico")



# Background code
dashborad = Canvas( app, width = window_width, height = window_width)
dashborad.pack(fill = "both", expand = True)
bg_Image = (ImagePicker(imagePath = path.dashborad_background,
                        width = window_width, height = window_height)).image

dashborad.create_image(0, 0, image = bg_Image,anchor = "nw")


button = {"width": 39, "height": 43}
nav = [200, 20]


photo = (ImagePicker(imagePath = path.closeIcon, width = 20, height = 20)).image
photo2 = (ImagePicker(imagePath = path.minimizeIcon, width = 20, height = 2)).image
photo3 = (ImagePicker(imagePath = path.nav_commitby, width = 200, height = 20)).image
photo4 = (ImagePicker(imagePath = path.nav_dashborad, width = 200, height = 20)).image
photo5 = (ImagePicker(imagePath = path.nav_header, width = 200, height = 20)).image
photo6 = (ImagePicker(imagePath = path.nav_path, width = 200, height = 20)).image

# btn set of app
closebtn = Cus_Button(RepeWith = app, image = photo,highlightbackground = "red", bg = "#008618",
                    place=[2,(window_width - button["width"])],
                    height = button["height"], width = button["width"])

minimizebtn = Cus_Button(RepeWith = app, image = photo2, highlightbackground = "#F5F5F5", bg = "#008618",
                         place=[2,(window_width - (button["width"] * 2))],
                         height = button["height"], width = button["width"])

#
# nav_headerbtn = Cus_Button(RepeWith = app, image = photo5, highlightbackground = "#F5F5F5", bg = "#008618",
#                          place=[15,10], height = nav[1], width = nav[0])

# nav_dashboradbtn = Cus_Button(RepeWith = app, image = photo4, highlightbackground = "#F5F5F5", bg = "#008618",
#                             place=[240, 10], height = nav[1], width = nav[0])
#
# nav_pathbtn = Cus_Button(RepeWith = app, image = photo6, highlightbackground = "#F5F5F5", bg = "#008618",
#                          place=[300, 10], height = nav[1], width = nav[0])
#
# nav_commitbybtn = Cus_Button(RepeWith = app, image = photo3, highlightbackground = "#F5F5F5", bg = "#008618",
#                          place=[340, 10], height = nav[1], width = nav[0])



game_frame = Frame(app,borderwidth=0,)
game_frame.place(x = 238, y = 180)

style = ttk.Style()
style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Calibri', 11)) # Modify the font of the body
style.configure("mystyle.Treeview.Heading", font=('Calibri', 13,'bold')) # Modify the font of the headings
style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders

my_game = ttk.Treeview(game_frame,show="tree",style="mystyle.Treeview")

my_game['columns'] = ('name', 'Commit')

my_game.column("#0", width=0,  stretch=NO)
my_game.column("name", width=175, anchor="w")
my_game.column("Commit",width=40,anchor=CENTER)

dashborad_item = {}
def get():
    return Label(text = "", background = "white")

dashborad_item.update({"name": get(),"Count": get(),"Address": get(), "Current": get(),
                       "ListOfItem": Listbox(app,height = 18, width = 96,),"textForMessage": get() })


dashborad_item["name"].place(x=530, y = 55)
dashborad_item["Count"].place(x=760, y = 55)
dashborad_item["Address"].place(x=545, y = 83)
dashborad_item["Current"].place(x=238, y = 123)
dashborad_item["ListOfItem"].place(x=480, y = 120)
dashborad_item["textForMessage"].place(x=700, y = 250)

dashborad_item["textForMessage"].config(text = "Nothing to Commit")

b2 = (button2()).getButton(head=dashborad, size=[130, 40], path=path.ButtonBackground)

size=[130, 40]

Canvasbtn = Canvas(dashborad, width=size[0], height=size[1], bg="white", highlightthickness=0, borderwidth=0)
Canvasbtn.place(x=925, y=450)
img = (ImagePicker(imagePath=path.ButtonBackground, width = size[0] - 2, height = size[1] - 2)).image
Canvasbtn.create_image(0, 0, anchor=NW, image=img)
mytext = Canvasbtn.create_text((size[0] / 2), (size[1] / 2), text="Commit", fill="#D1D1D1", font=('Helvetica 10 bold'))


size2 = [130, 20]
Canvasbtn2 = Canvas(dashborad, width=size2[0], height=size2[1], bg="white", highlightthickness=0, borderwidth=0)
Canvasbtn2.place(x=485, y=435)
img2 = (ImagePicker(imagePath=path.checkBoxBackground, width = size2[0] - 2, height = size2[1] - 2)).image
img3 = (ImagePicker(imagePath=path.checkBoxIcon, width = 20, height = 10)).image
Canvasbtn2.create_image(0, 0, anchor=NW, image=img2)
Canvasbtn2.create_image(10, 4, anchor=N, image=img3)

# Canvasbtn.config(fill="white")



def onClick(event):
    try:
        item = int(my_game.selection()[0])-1

        dashborad_item["name"].config(text = data[item]["Name"])
        dashborad_item["name"].config(text = data[item]["Name"])
        dashborad_item["Current"].config(text = data[item]["Name"])
        dashborad_item["Count"].config(text = getCommit(data[item]["Address"]))
        dashborad_item["Address"].config(text = data[item]["Address"])



    except Exception as e:
        print(e)


def getCommit(Address):
    obj = Committer(Address)
    listOfChanges = obj.NoOfChanges()
    dashborad_item["ListOfItem"].delete(0, END)

    if listOfChanges:
        dashborad_item["textForMessage"].place_forget()


    for i in range(len(listOfChanges)):
        dashborad_item["ListOfItem"].insert(i, listOfChanges[i])


    # b2 = button2(head = dashborad, size = [50,50], path = path.dashborad_background)
    # b2.btn.place(x=300, y=100)

    return len(listOfChanges)

my_game.bind("<Button-1>", onClick)
readFile()
# writeInfile()

my_game.pack()


# main display
app.mainloop()



