# Hamza/Yousuf
import tkinter as tk
import turtle
from turtle import RawTurtle, ScrolledCanvas, TurtleScreen
from math import floor

##################################################################################################################################################################################################################################################################################################
#CODE FOR THE BOARD ~AYUSH

board = [[0,0,0, 0,0,0, 0,0,0],  [0,0,0, 0,0,0, 0,0,0],  [0,0,0, 0,0,0, 0,0,0],
         [0,0,0, 0,0,0, 0,0,0],  [0,0,0, 0,0,0, 0,0,0],  [0,0,0, 0,0,0, 0,0,0],
         [0,0,0, 0,0,0, 0,0,0],  [0,0,0, 0,0,0, 0,0,0],  [0,0,0, 0,0,0, 0,0,0]]




meta = [0,0,0, 0,0,0, 0,0,0]




player = 0


i=0
#Used for which grid you want to start at

# while i == 0:
#     try:
#         grid = 4
#         i+=1
#     except:
#         None
grid=4


# Display will become irrelevant when a GUI is made
# List comprehension: https://docs.python.org/3/glossary.html#term-list-comprehension
def display():
    global board
    global grid



    dp = '-----------------------------\n'
    if grid!=9: board[grid] = ['⁕' if i == 0 else i for i in board[grid]]
   
    for i in range(3):
        for j in range(3):
            for k in range(3):
                dp += '| '
                for l in range(3):
                    dp += str(board[3*i+k][3*j+l]) + ' '
                dp += '| '
            dp += '\n'
        dp += '-----------------------------\n'
   
    print(dp.replace('0', '•').replace('1', 'X').replace('2', 'O'))
    board[grid] = [0 if i == '⁕' else i for i in board[grid]]




####### Move function creates an X or O in an empty space #########
def move(list_grid, box):
    global grid
    global player

    if list_grid != grid and grid != 9:
        print("Invalid input")

    elif board[list_grid][box] == 0:
        board[list_grid][box] = player
        check(list_grid)
        grid = box
        display()
        if meta[box] != 0:
            list_grid = int(input('Choose any grid'))
        player %= 2
        player += 1
    else:
        display()
        print('Square Taken')


### CHECKS THE GRID FOR IF YOU WIN ###

def check(list_grid):
    global meta

    for i in [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]:
        if board[list_grid][i[0]] == board[list_grid][i[1]] == board[list_grid][i[2]] != 0:
            for j in range(9):
                board[list_grid][j] = player
                meta[list_grid] = player




    for i in [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]:
        if meta[i[0]] == board[i[1]] == board[i[2]] != 0:
            print('P' + str(player) + 'Wins')




display()



#####################################################################
# this is the old conditional statment
# while True:
#     try:
#         player %= 2
#         player += 1

#         print('PLAYER ' + str(player))
#         player_move= move(int(input('Pick a Number 1-9 : '))-1)
#     except:
#         display()
#         print('Invalid Input')


######################################
#Re worked conditionals (Kapishh Rajan)

'''while True:
    try:
        # Alternate between players 1 and 2
        player %= 2
        player += 1

        print('PLAYER ' + str(player))

        # Validate input and ensure it's within the range 1-9
        player_input = int(input('Pick a Number 1-9: '))
        while not (1<= int(player_input) <= 9):
            player_input = int(input('Input must be between 1 and 9. Pick a Number 1-9: '))

        player_move = move(int(input('grid: ')), int(player_input) - 1)

### checks if there are any errors in the input
    except:
        print("Invalid Input")'''


##################################################################################################################################################################################################################################################################################################

def draw_x(x, y):
    c.penup()
    c.goto(x,y)
    c.color('red')

    c.pendown()
    c.setheading(45)
    c.forward(70)
    c.back(140)
    c.forward(70)
    
    c.right(90)
    c.forward(70)
    c.back(140)
    c.penup()

def draw_circle(x, y):
    
    c.penup()
    c.setheading(0)
    c.goto(x, y - 50) 
    c.color('blue')

    c.pendown()
    c.circle(50)  
    c.penup()


root = tk.Tk()

root.title("Ultimate Tic Tac Toe")
root.configure(background="white")
root.minsize(1000, 1000)
root.maxsize(1200, 1200)
root.geometry("1200x1200+1200+100")
canvas = tk.Canvas(master = root, width = 1200, height = 1200)
canvas.grid(padx=2, pady=2, row=0, column=0, rowspan=10, columnspan=10)

c = turtle.RawTurtle(canvas)
c.speed(0)
c.penup()
c.pensize(15)

# Ayush- drawing thick border lines
for i in range(4):
    c.setheading([0, 0, 90, 90][i])
    c.goto([-600, -600, 135*1.5, -135*1.5][i], [135*1.5, -135*1.5, -600, -600][i])
    c.pendown()
    c.forward(1200)
    c.penup()

buttons = []
placeholder = tk.PhotoImage()

# Ayush
def jp_move(row, col):
    global player
    player %= 2
    player += 1
    list_grid, box = (floor(col/3)+3*floor(row/3), col%3 + row%3*3)
    player_move = move(list_grid, box)

def updategui():
    global row
    global col
    
    replace(row, col)

# Hamza
def replace(row, col):
    global player
    i=row * 9 + col 
    button = buttons[i]
# destroys the button and places an X or an O in the empty space
    if player == 1:
        button.destroy()
        draw_x((col-4) * 135,(row-4) * -135)     
    else:
        button.destroy()
        draw_circle((col-4) * 135,(row-4) * -135)
# changes the active player
    player+=1
    player%=2

# Hamza - CITE SOURCES
for row in range(9):
    root.rowconfigure(row,minsize=100, weight=1)
    
    for column in range(9):
        
        root.columnconfigure(column,minsize=100, weight=1)
        button = tk.Button(root,image=placeholder, width= 100, height = 100,command= lambda row =  row, col = column : jp_move(row, col))
        button.grid(column=column, row=row)
        buttons.append(button)
##################################################################################################################################################################################################################################################################################################

# -*- coding: utf-8 -*-
# Ultimate Tic Tac Toe


root.mainloop()
