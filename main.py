from tkinter import *
from tkinter import messagebox

#The code for the GUI comes from stack overflow: https://stackoverflow.com/questions/7591294/how-to-create-a-self-resizing-grid-of-buttons-in-tkinter
#the answer was provided by Gabriel Staples.
root = Tk()
root.title("TIC-TAC-TOE")
root.geometry("500x500")
Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)

#creating a frame for the grid 
frame=Frame(root)
frame.grid(row=0, column=0, sticky=N+S+E+W)

#create a 3x3 grid of buttons for the game board.
for row_index in range(3):
    Grid.rowconfigure(frame, row_index, weight=1)
    for col_index in range(3):
        Grid.columnconfigure(frame, col_index, weight=1)
        btn = Button(frame) #create a button inside frame 
        btn.grid(row=row_index, column=col_index, sticky=N+S+E+W)  

root.mainloop()