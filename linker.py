import webbrowser
import tkinter
from tkinter import * 
import linecache
import requests

def search(name , winname, index , sider):
    for answers in data[f"{name}"][index] :
        user_button = tkinter.Button(winname, bg= 'black',fg = 'white',
                                    text=answers,
                                    command=lambda searches=answers : webbrowser.open(data[f"{name}"][index].get(searches)))
        user_button.pack(side = sider, pady = 5 )

def center(toplevel):
    toplevel.update_idletasks()
    screen_width = toplevel.winfo_screenwidth()
    screen_height = toplevel.winfo_screenheight()
    size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
    x = screen_width/2 - size[0]/2
    y = screen_height/2 - size[1]/2
    toplevel.geometry("+%d+%d" % (x, y))
 
def windows(tit,dimensions):
    global window2
    window2 = tkinter.Tk()
    window2.title(tit)
    window2.geometry(dimensions)
    window2.resizable(0,0)
    center(window2)

data = requests.get('https://json.extendsclass.com/bin/566991591d28').json()
window = tkinter.Tk()
window.title('MITS') 
window.geometry('200x250')
window.resizable(0,0)
center(window)
firstframe = Frame(window) 
firstframe.pack(side = TOP, pady = 20) 
middleframe = Frame(window)
middleframe.pack(side = TOP)
bottomframe = Frame(window)
bottomframe.pack( side = TOP,pady = 20)
feedbackframe = Frame(window)
feedbackframe.pack(side= BOTTOM)

def BCM():
    window.destroy()
    window2 = tkinter.Tk()
    window2.title('BCM')
    window2.geometry('150x80')
    window2.resizable(0,0)
    center(window2)
    firstframe2 = Frame(window2) 
    firstframe2.pack(side = TOP, pady = 20) 

    def BCM_civil():
        webbrowser.open(list(data["BCM"][0].values())[0])
        window2.destroy()
        
    def BCM_mechanics():
        window2.destroy()
        window3 = tkinter.Tk()
        window3.title('BCM')
        window3.geometry('300x400')
        window3.resizable(0,0)
        center(window3)
        firstframe3 = Frame(window3) 
        firstframe3.pack(side = LEFT, fill = 'y',padx = 20)
        secondframe3 = Frame(window3)
        secondframe3.pack(side =  RIGHT, fill = 'y',padx= 20)
        tkinter.Label(firstframe3 ,text = 'Lectures:',font=(None, 12)).pack(side = TOP , pady = 5)
        tkinter.Label(secondframe3 ,text = 'Remedial:',font=(None, 12)).pack(side = TOP , pady = 5)
        for answers in list(data['BCM'][1].values())[0][0] :
            mechanical_butt_lec = tkinter.Button(firstframe3,bg ='black', fg = 'white',text=answers, command= lambda searches = answers : webbrowser.open(list(data['BCM'][1].values())[0][0].get(searches)))
            mechanical_butt_lec.pack(side =TOP, pady = 5)
        for answers in list(data['BCM'][1].values())[0][1] :
            mechanical_butt_lab = tkinter.Button(secondframe3,bg = 'black',fg = 'white', text=answers, command= lambda searches = answers : webbrowser.open(list(data['BCM'][1].values())[0][1].get(searches)))
            mechanical_butt_lab.pack(side =TOP, pady = 5)
    BCMlect = tkinter.Button(firstframe2,background = 'black',fg ='white', text= 'Civil', command = BCM_civil)
    BCMlect.pack(side = LEFT , padx =5 , ipadx = 5 , ipady = 5)
    BCMlabo = tkinter.Button(firstframe2, text= 'Mechanics',background = 'black',fg ='white', command = BCM_mechanics)
    BCMlabo.pack(side= RIGHT , padx = 5 , ipadx = 5 , ipady = 5)

def BEEE():
    window.destroy()
    window2 = tkinter.Tk()
    window2.title('BEEE')
    window2.geometry('150x80')
    window2.resizable(0,0)
    center(window2)
    firstframe = Frame(window2) 
    firstframe.pack(side = TOP, pady = 20) 
    def BEEElec():
        webbrowser.open(list(data["BEEE"][1].values())[0])
        window2.destroy()
    def BEEElab():
        webbrowser.open(list(data["BEEE"][0].values())[0])
        window2.destroy()
    BEEElect = tkinter.Button(firstframe,background = 'black',fg ='white', text= 'Lectures', command = BEEElec)
    BEEElect.pack(side = LEFT , padx =5 , ipadx = 5 , ipady = 5)
    BEEElabo = tkinter.Button(firstframe, text= 'Lab',background = 'black',fg ='white', command = BEEElab)
    BEEElabo.pack(side= RIGHT , padx = 5 , ipadx = 5 , ipady = 5)

def CSE():
    window.destroy()
    windows('CSE' , '150x80')
    window2.resizable(0,0)
    firstframe = Frame(window2) 
    firstframe.pack(side = TOP, pady = 20) 
    def CSElab():
        webbrowser.open(list(data['CSE'][0].values())[0])
        window2.destroy()
    def CSElec():
        webbrowser.open(list(data['CSE'][1].values())[0])
        window2.destroy()
    CSElect = tkinter.Button(firstframe,background = 'black',fg ='white', text= 'Lectures', command = CSElec)
    CSElect.pack(side = LEFT , padx =5 , ipadx = 5 , ipady = 5)
    CSElabo = tkinter.Button(firstframe, text= 'Lab',background = 'black',fg ='white', command = CSElab)
    CSElabo.pack(side= RIGHT , padx = 5 , ipadx = 5 , ipady = 5)
    
def EEES():
    window.destroy()
    webbrowser.open(list(data['EEES'][0].values())[0])

def BME():
    window.destroy()
    windows('BME' , '300x400')
    firstframe = Frame(window2) 
    firstframe.pack(side = LEFT, fill = 'y',padx = 20)
    secondframe = Frame(window2)
    secondframe.pack(side =  RIGHT, fill = 'y',padx= 20)
    tkinter.Label(firstframe ,text = 'Lectures:',font=(None, 12)).pack(side = TOP , pady = 5)
    tkinter.Label(secondframe ,text = 'Remedial:',font=(None, 12)).pack(side = TOP , pady = 5)
    search('BME', firstframe, 0 , TOP)
    search('BME', secondframe , 1 , TOP)

def IT_workshop():
    window.destroy()
    webbrowser.open(list(data["IT Workshop"][0].values())[0])

def feedback():
    windows('Feedback', '200x260')
    feedback_frame1 = Frame(window2)
    feedback_frame1.pack(side=TOP ,fill = 'x')
    tkinter.Label(feedback_frame1, text ="Hi, I am Nischal, your batchmate😛\nMade this project out of frustation\nfrom all the messed up link process.\nHope this will help you.\n\nFor your valuable\nsuggestions & feedback\nor if you find any bugs\nyou can find me here.\n" ).pack(side =TOP)
    tkinter.Label(feedback_frame1, text ="Whatsapp:" ,bg='black',fg='white',font = (None ,12 ) ).pack(side =TOP,pady=3)
    tkinter.Label(feedback_frame1, text ="7000578930" , font = (None ,10 ) ).pack(side =TOP)
    tkinter.Label(feedback_frame1, text ="Mail:" ,bg='black',fg='white', font = (None ,12 ) ).pack(side =TOP,pady=3)
    link1 = Label(feedback_frame1, text="nischal.singh38@gmail.com", fg="blue", cursor="hand2")
    link1.pack(side=TOP)
    link1.bind("<Button-1>", lambda e: webbrowser.open("https://mail.google.com/mail/u/0/?tab=wm#inbox?compose=GTvVlcSHxTkXXpftRChhLPHwzDjKgDHRLXdXwNBFbxQZzkKKgpvQbmRxlZFgXKvFvmdpVXHVNbChR"))

BCM_button = tkinter.Button(firstframe, text= 'BCM "20"',background = "black", fg = "white", command = BCM)
BCM_button.pack(side = LEFT,padx=10, ipadx =2 , ipady = 8)
BEEE = tkinter.Button(firstframe, text= 'BEEE "22"',background = "black", fg = "white", command = BEEE)
BEEE.pack(side = RIGHT,padx=10, ipadx =2 , ipady = 8)
CSE = tkinter.Button(middleframe, text= 'CSE "02"',background = "black", fg = "white", command = CSE)
CSE.pack(side = LEFT,padx=10,ipadx =5 , ipady = 8)
EEES = Button(middleframe, text= 'EEES "15"',background = "black", fg = "white", command = EEES)
EEES.pack(side = RIGHT,padx=10,ipadx =2 , ipady = 8)
BME = tkinter.Button(bottomframe, text= 'BME "21"',background = "black", fg = "white", command = BME)
BME.pack(side = LEFT ,padx= 13, ipadx =4 , ipady = 8)
IT = tkinter.Button(bottomframe, text= 'IT Workshop',background = "black", fg = "white", command = IT_workshop)
IT.pack(side = RIGHT ,padx = 5, ipadx =2 , ipady = 8)
IT = tkinter.Button(feedbackframe, text= 'Feedback',background = 'sky blue',command = feedback)
IT.pack(side = RIGHT ,pady = 2)

window.mainloop()
