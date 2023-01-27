# Import module

from tkinter import *
from student_pub import *
from PIL import ImageTk, Image
from random import randrange

# Create object
root = Tk()
root.title("Croc game")


# Adjust size
#root.geometry("700x450")

width= root.winfo_screenwidth()
height= root.winfo_screenheight()

#set screensize as fullscreen and not resizable
root.geometry("%dx%d" % (width, height))
root.resizable(False, False)


# put image in a label and place label as background
imgTemp = Image.open("mouth.png")
img2 = imgTemp.resize((height,700))
img = ImageTk.PhotoImage(img2)

label = Label(root,image=img)
label.pack(side='top',fill=Y,expand=True)



# Create Frame
frame1 = Frame(root)
frame1.pack()

# Add buttons
buttons= []
for indexs in range(0, 13):

    button1 = Button(text="0",state=DISABLED,command=lambda index=0 : process(index), font=("Arial",25))
    button1.place(x=410,y=375)
    button2 = Button(text="1",state=DISABLED, command=lambda index=1 : process(index), font=("Arial",25))
    button2.place(x=476,y=274)
    button3 = Button(text="2",state=DISABLED, command=lambda index=2 : process(index), font=("Arial",25))
    button3.place(x=650,y=255)
    button4 = Button(text="3",state=DISABLED, command=lambda index=3 : process(index), font=("Arial",25))
    button4.place(x=840,y=255)
    button5 = Button(text="4",state=DISABLED, command=lambda index=4 : process(index), font=("Arial",25))
    button5.place(x=1010,y=274)
    button6 = Button(text="5",state=DISABLED, command=lambda index=5 : process(index), font=("Arial",25))
    button6.place(x=1080,y=375)

    button7 = Button(text="6",state=DISABLED, command=lambda index=6 : process(index), font=("Arial",25))
    button7.place(x=1080,y=505)
    button8 = Button(text="7",state=DISABLED, command=lambda index=7 : process(index), font=("Arial",25))
    button8.place(x=1010,y=600)
    button9 = Button(text="8",state=DISABLED, command=lambda index=8 : process(index), font=("Arial",25))
    button9.place(x=840,y=625)
    button10 = Button(text="9",state=DISABLED, command=lambda index=9 : process(index), font=("Arial",25))
    button10.place(x=650,y=625)
    button11 = Button(text="10",state=DISABLED, command=lambda index=10 : process(index), font=("Arial",25))
    button11.place(x=473,y=600)
    button12 = Button(text="11",state=DISABLED, command=lambda index=11 : process(index), font=("Arial",25))
    button12.place(x=400,y=505)
    buttons.append(buttons)

btnStartGameList = []
for index in range(0, 1):
    btnStartGame = Button(text="Start Game",state=NORMAL, command=lambda : startgame(index),font=("Arial",15))
    btnStartGame.place(x=710,y=450)
    btnStartGameList.append(btnStartGame)
    


guess = 0
totalNumberOfGuesses = 0
secretNumber = randrange(12)
print (secretNumber)

def init():
    global buttons, guess, totalNumberOfGuesses, secretNumber
    guess = 0
    totalNumberOfGuesses = 0
    secretNumber = randrange(12)
    print(secretNumber)



def process(i):
    global totalNumberOfGuesses, buttons
    guess = i
    if guess == secretNumber:
        
        print("GameOver!")
        pubpic([[7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7], [7, 7, 7, 4, 2, 1, 1, 2, 4, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 4, 2, 1, 1, 2, 4, 7, 7, 7], [7, 7, 3, 1, 0, 0, 0, 0, 1, 2, 7, 7, 
        7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 2, 1, 0, 0, 0, 0, 1, 3, 7, 7], [7, 4, 2, 1, 0, 0, 0, 0, 0, 0, 1, 4, 7, 7, 7, 7, 7, 7, 7, 7, 5, 1, 0, 0, 0, 0, 0, 0, 1, 2, 4, 7], [5, 4, 1, 3, 1, 0, 0, 0, 0, 0, 0, 1, 2, 3, 7, 7, 7, 7, 3, 2, 1, 0, 0, 0, 0, 0, 0, 1, 3, 1, 4, 5], [5, 3, 0, 6, 4, 3, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 
        0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 1, 0, 2, 5], [5, 0, 5, 6, 7, 7, 4, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 4, 7, 6, 6, 5, 0, 5], [5, 0, 6, 7, 7, 7, 6, 5, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 5, 6, 7, 7, 7, 6, 0, 5], [5, 0, 6, 7, 7, 7, 6, 6, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 
        6, 6, 7, 7, 7, 6, 0, 5], [5, 0, 6, 6, 7, 7, 6, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 6, 7, 7, 6, 6, 0, 5], [5, 0, 0, 6, 6, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 6, 6, 0, 0, 5], [5, 4, 0, 3, 
        2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 0, 
        3, 5], [5, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 3, 3, 3, 4, 5], [5, 4, 4, 3, 3, 2, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 3, 3, 4, 4, 5], [5, 4, 4, 3, 2, 1, 1, 1, 1, 0, 
        1, 6, 6, 1, 0, 0, 0, 0, 1, 6, 6, 0, 0, 1, 1, 1, 1, 2, 3, 4, 4, 5], [5, 5, 4, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 4, 5, 5], [5, 5, 4, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 4, 5, 5], [5, 5, 4, 3, 2, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 
        2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 2, 3, 4, 5, 5], [5, 5, 4, 3, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 3, 4, 5, 5], [5, 5, 4, 3, 3, 3, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 3, 3, 3, 4, 5, 5], [5, 5, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 
        3, 3, 3, 3, 3, 3, 3, 4, 5, 5], [5, 5, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 5, 5], [5, 5, 4, 4, 4, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 4, 4, 4, 5, 5], [6, 5, 
        5, 4, 4, 4, 3, 3, 3, 3, 1, 0, 0, 5, 3, 3, 3, 3, 4, 0, 0, 0, 3, 3, 3, 3, 4, 4, 
        4, 5, 5, 6], [6, 5, 5, 4, 4, 4, 4, 4, 4, 4, 3, 0, 0, 4, 4, 4, 4, 4, 4, 0, 0, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 6], [6, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 6], [6, 6, 5, 5, 5, 5, 5, 4, 
        4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6], [6, 6, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6], [7, 6, 6, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6], [7, 7, 6, 6, 6, 6, 6, 5, 5, 5, 5, 5, 5, 5, 
        5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7], [7, 7, 7, 7, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 5, 7, 7, 7, 7], [7, 7, 7, 7, 7, 7, 7, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7]])
        root.destroy()


    if i != secretNumber:
        if i == 0:
            button1["state"] = DISABLED
        elif i == 1:
            button2["state"] = DISABLED
        elif i == 2:
            button3["state"] = DISABLED
        elif i == 3:
            button4["state"] = DISABLED
        elif i == 4:
            button5["state"] = DISABLED
        elif i == 5:
            button6["state"] = DISABLED
        elif i == 6:
            button7["state"] = DISABLED
        elif i == 7:
            button8["state"] = DISABLED
        elif i == 8:
            button9["state"] = DISABLED
        elif i == 9:
            button10["state"] = DISABLED
        elif i == 10:
            button11["state"] = DISABLED
        elif i == 11:
            button12["state"] = DISABLED
  


status = "none"

def startgame(i):
    global status
    btnStartGame = 0
    if btnStartGame == 0:
        button1["state"]= NORMAL
        button2["state"]= NORMAL
        button3["state"]= NORMAL
        button4["state"]= NORMAL
        button5["state"]= NORMAL
        button6["state"]= NORMAL
        button7["state"]= NORMAL
        button8["state"]= NORMAL
        button9["state"]= NORMAL
        button10["state"]= NORMAL
        button11["state"]= NORMAL
        button12["state"]= NORMAL
        btnStartGameList[i]["text"] = "  GO!  "
        pubpic([[5, 7, 7, 7, 7, 7, 7, 7, 7, 6, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 6, 7, 7, 
        7, 7, 7, 7, 7, 7, 7], [5, 7, 7, 7, 7, 7, 3, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 
        2, 2, 1, 2, 2, 2, 2, 3, 7, 7, 7, 7, 7, 7], [7, 7, 7, 7, 7, 2, 2, 1, 1, 1, 1, 
        0, 1, 2, 1, 1, 1, 1, 2, 1, 0, 1, 1, 1, 1, 2, 2, 7, 7, 7, 7, 7], [7, 7, 7, 5, 
        2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 2, 4, 7, 7, 7], [7, 7, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 7, 7], [7, 7, 2, 1, 0, 0, 1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 1, 0, 0, 1, 2, 7, 7], [7, 3, 2, 0, 1, 4, 2, 2, 2, 1, 1, 2, 3, 2, 1, 1, 1, 1, 2, 3, 2, 1, 1, 1, 2, 2, 4, 1, 0, 2, 3, 7], [7, 2, 1, 2, 4, 4, 4, 2, 1, 1, 4, 7, 7, 7, 4, 1, 1, 4, 7, 7, 7, 4, 1, 1, 2, 4, 4, 4, 2, 1, 2, 7], [4, 2, 2, 3, 7, 7, 7, 7, 2, 3, 7, 7, 7, 7, 7, 4, 4, 7, 7, 7, 7, 7, 3, 2, 7, 7, 7, 7, 4, 2, 2, 4], [3, 2, 4, 4, 7, 7, 7, 7, 4, 4, 3, 7, 7, 7, 7, 4, 4, 3, 7, 7, 7, 3, 4, 4, 7, 7, 7, 7, 4, 4, 2, 3], [3, 5, 3, 3, 7, 7, 7, 7, 5, 5, 5, 7, 7, 7, 6, 6, 6, 6, 7, 7, 7, 5, 5, 5, 7, 7, 7, 7, 3, 3, 5, 3], [3, 5, 3, 3, 3, 7, 7, 7, 5, 5, 5, 6, 7, 7, 5, 5, 5, 5, 7, 7, 6, 5, 5, 5, 7, 
        7, 7, 3, 3, 3, 4, 3], [3, 5, 4, 7, 4, 7, 7, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 
        5, 5, 5, 5, 5, 5, 5, 7, 7, 3, 7, 4, 5, 3], [4, 7, 7, 7, 7, 7, 6, 5, 5, 5, 5, 
        5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 7, 7, 7, 7, 7, 5], [5, 7, 7, 7, 
        7, 7, 6, 6, 5, 6, 6, 6, 6, 6, 6, 5, 5, 6, 6, 6, 6, 6, 6, 5, 6, 6, 7, 7, 7, 7, 7, 5], [4, 6, 7, 7, 7, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 6, 4], [4, 5, 7, 7, 7, 5, 6, 6, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 5, 7, 7, 7, 5, 4], [4, 6, 5, 6, 5, 5, 6, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 5, 6, 6, 5, 5, 4], [4, 4, 4, 7, 7, 4, 4, 5, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 5, 5, 4, 7, 7, 5, 4, 4], [4, 4, 7, 7, 7, 5, 4, 5, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 5, 4, 7, 7, 7, 4, 4], [4, 5, 7, 7, 7, 7, 4, 5, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 5, 7, 7, 7, 7, 5, 4], [5, 3, 7, 7, 7, 7, 4, 5, 4, 3, 3, 3, 3, 3, 3, 3, 2, 2, 3, 2, 3, 3, 3, 3, 4, 4, 7, 7, 7, 7, 2, 5], [4, 3, 7, 7, 7, 4, 7, 4, 4, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 4, 
        7, 7, 7, 7, 7, 3, 4], [3, 4, 2, 0, 0, 7, 7, 7, 4, 4, 3, 2, 3, 1, 1, 1, 1, 1, 
        1, 2, 2, 3, 3, 4, 7, 7, 7, 0, 0, 2, 4, 3], [3, 4, 3, 2, 7, 7, 7, 7, 4, 5, 4, 
        7, 7, 7, 3, 3, 3, 3, 7, 7, 7, 4, 4, 4, 7, 7, 7, 7, 2, 3, 4, 3], [5, 3, 3, 2, 
        7, 7, 7, 7, 2, 0, 0, 7, 7, 7, 0, 0, 0, 0, 7, 7, 7, 0, 0, 3, 7, 7, 7, 7, 2, 3, 3, 5], [7, 3, 4, 3, 7, 7, 7, 7, 1, 0, 7, 7, 7, 7, 7, 0, 0, 7, 7, 7, 7, 7, 0, 1, 7, 7, 7, 7, 3, 4, 3, 7], [7, 5, 2, 4, 1, 7, 7, 7, 0, 0, 7, 7, 7, 7, 7, 0, 0, 7, 7, 7, 7, 7, 0, 0, 7, 7, 7, 1, 4, 2, 5, 7], [7, 7, 4, 2, 5, 3, 3, 2, 2, 1, 1, 7, 7, 7, 0, 1, 1, 0, 7, 7, 7, 1, 1, 2, 2, 3, 3, 5, 2, 4, 7, 7], [7, 7, 7, 5, 2, 2, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 2, 2, 4, 7, 7, 7], [7, 7, 7, 7, 6, 4, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4, 6, 7, 7, 7, 7], [7, 7, 7, 7, 7, 7, 7, 7, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7]])

    else:
        btnStartGame["state"]= NORMAL
        button1["state"]= DISABLED
        button2["state"]= DISABLED
        button3["state"]= DISABLED
        button4["state"]= DISABLED
        button5["state"]= DISABLED
        button6["state"]= DISABLED
        button7["state"]= DISABLED
        button8["state"]= DISABLED
        button9["state"]= DISABLED
        button10["state"]= DISABLED
        button11["state"]= DISABLED
        button12["state"]= DISABLED
        btnStartGame = 1
        init()

        
    print("Game started")

# Execute tkinter
root.mainloop()
