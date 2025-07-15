from tkinter import *
import tkinter.font as font
from fifteen import Fifteen
import sys
          
# global list of all buttons
buttons = []
def clickButton(tiles, name):
    move = int(name)
    if tiles.is_valid_move(move):
        tiles.update(move)
        
        # for debug
        # tiles.draw()

        # swap buttons in the gui
        index_zero = -1
        index_move = -1
        for i in range(0, 16):
            button = buttons[i]
            text = str(button.cget('text'))
            if text == '':
                index_zero = i
            elif text == name:
                index_move = i

        # if messed up then exit
        if index_zero == -1 or index_move == -1:
            print('Sorry, internal error')
            sys.exit()

        # create variables for buttons
        zero_button = buttons[index_zero]
        move_button = buttons[index_move]

        buttons[index_move] = zero_button
        buttons[index_zero] = move_button

        for i in range(0, 4):
           for j in range(0, 4):
                buttons[i*4+j].grid(row=i+1, column=j)

        if tiles.is_solved():
            print('Awesome! Quit and restart to play again.')

    # for debug
    # if empty tile is clicked then print valid moves
    # elif move == 0:
    #     tiles.print_valid_moves()
    
if __name__ == '__main__':

    # make tiles
    tiles = Fifteen()
    tiles.shuffle()

    # for debug
    # tiles.draw()

    # make a window
    gui = Tk()
    gui.title("Fifteen")

    # make font
    font = font.Font(family='Helveca', size='25', weight='bold')

    # make buttons
    for i in range(0, 16):
        text = StringVar()
        if not tiles.tiles[i] == 0:
            text.set(tiles.tiles[i])
        else:
            text.set('')

        name = str(tiles.tiles[i])
        button = Button(gui, textvariable=text, name=name,
                        bg='white', fg='black', font=font, height=2, width=5,
                        command = lambda name=name: clickButton(tiles, name))

        # color is not changing on my laptop
        if not tiles.tiles[i] == 0:
            gui.nametowidget(name).configure(bg='coral')

        # add button to list of buttons
        buttons.append(button)

    for i in range(0, 4):
        for j in range(0, 4):
            buttons[i*4+j].grid(row=i+1, column=j)

    # update the window
    gui.mainloop()
