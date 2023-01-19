# Import module

from tkinter import *

from random import randrange

# Create object
root = Tk()


# Adjust size
root.geometry("170x170")

# Add image file
bg = PhotoImage(file = "mouth.png")

# Show image using label
label1 = Label( root, image = bg)
label1.place(x = 0, y = 0)

# Create Frame
frame1 = Frame(root)
frame1.pack()

# Add buttons
buttons= []
for indexs in range(0, 13):

    button1 = Button(text="0",state=DISABLED,command=lambda index=0 : process(index), font=("Arial",7))
    button1.place(x=13,y=71)
    button2 = Button(text="1",state=DISABLED, command=lambda index=1 : process(index), font=("Arial",7))
    button2.place(x=27,y=45)
    button3 = Button(text="2",state=DISABLED, command=lambda index=2 : process(index), font=("Arial",7))
    button3.place(x=61,y=41)
    button4 = Button(text="3",state=DISABLED, command=lambda index=3 : process(index), font=("Arial",7))
    button4.place(x=98,y=41)
    button5 = Button(text="4",state=DISABLED, command=lambda index=4 : process(index), font=("Arial",7))
    button5.place(x=133,y=45)
    button6 = Button(text="5",state=DISABLED, command=lambda index=5 : process(index), font=("Arial",7))
    button6.place(x=147,y=71)

    button7 = Button(text="6",state=DISABLED, command=lambda index=6 : process(index), font=("Arial",7))
    button7.place(x=14,y=102)
    button8 = Button(text="7",state=DISABLED, command=lambda index=7 : process(index), font=("Arial",7))
    button8.place(x=27,y=126)
    button9 = Button(text="8",state=DISABLED, command=lambda index=8 : process(index), font=("Arial",7))
    button9.place(x=61,y=134)
    button10 = Button(text="9",state=DISABLED, command=lambda index=9 : process(index), font=("Arial",7))
    button10.place(x=96,y=134)
    button11 = Button(text="10",state=DISABLED, command=lambda index=10 : process(index), font=("Arial",7))
    button11.place(x=130,y=126)
    button12 = Button(text="11",state=DISABLED, command=lambda index=11 : process(index), font=("Arial",7))
    button12.place(x=143,y=102)
    buttons.append(buttons)

btnStartGameList = []
for index in range(0, 1):
    btnStartGame = Button(text="Start Game",state=NORMAL, command=lambda : startgame(index),font=("Arial",7))
    btnStartGame.place(x=58,y=87)
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
  

    # elif (button1["state"] == NORMAL) != secretNumber:
    #     button1["state"] = DISABLED
    # elif (button2["state"] == NORMAL) != secretNumber:
    #     button2["state"] = DISABLED
    # elif guess and (button3["state"] == NORMAL) != secretNumber:
    #     button3["state"] = DISABLED
    # elif guess and (button4["state"] == NORMAL) != secretNumber:
    #     button4["state"] = DISABLED
    # elif guess and (button5["state"] == NORMAL) != secretNumber:
    #     button5["state"] = DISABLED
    # elif guess and (button6["state"] == NORMAL) != secretNumber:
    #     button6["state"] = DISABLED
    # elif guess and (button7["state"] == NORMAL) != secretNumber:
    #     button7["state"] = DISABLED
    # elif guess and (button8["state"] == NORMAL) != secretNumber:
    #     button8["state"] = DISABLED
    # elif guess and (button9["state"] == NORMAL) != secretNumber:
    #     button9["state"] = DISABLED
    # elif guess and (button10["state"] == NORMAL) != secretNumber:
    #     button10["state"] = DISABLED
    # elif guess and (button11["state"] == NORMAL) != secretNumber:
    #     button11["state"] = DISABLED
    # elif guess and (button12["state"] == NORMAL) != secretNumber:
    #     button12["state"] = DISABLED

        
       



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
