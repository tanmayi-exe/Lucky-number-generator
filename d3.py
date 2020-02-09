from tkinter import *

win = Tk() # ...generates a window...
win.title("Lotto Number Generator") 
#win.geometry("500x500")
win.resizable(False,False)

#-----Widget Declaration-----# ...With Labels and Buttons
Labl = [Label(win),Label(win),Label(win),Label(win),Label(win),Label(win),Label(win),Label(win),Label(win),Label(win)]
ResetBtn = Button(win , text = "Reset")
PickBtn = Button(win , text = "Pick My Lucky Numbers")

#-----Position Widgets-----#
for i in range(0,9):
    Labl[i].grid(row = 1 , column = i+1 , padx = 10)

ResetBtn.grid(row = 2 , column = 6 , columnspan = 2)
PickBtn.grid(row = 2 , column = 1 , columnspan = 5)

#-----Functions-----#
def reset(): 
    for i in range(0,9):
        Labl[i].configure(text='...')
    PickBtn.configure(state = NORMAL)
    ResetBtn.configure(state = DISABLED)

def pick(): #...and can pick random numbers WITH a bonus number
    picks = [100, 150 ,60, 120, 40, 135, 1500, 900, 1100, 1001]
    for i in range(0,9):
        Labl[i].configure(text=picks[i])
    PickBtn.configure(state = DISABLED)
    ResetBtn.configure(state = NORMAL)

#-----Assign Functions-----#
ResetBtn.configure(command = reset)
PickBtn.configure(command = pick)

#-----Initialise-----#
reset()



win.mainloop()
