# Hamza/Yousuf
import tkinter as tk
import turtle
from turtle import RawTurtle, ScrolledCanvas, TurtleScreen
from math import floor

#############################################################
#Displays the instructions on the screen for the players to see. 
#(Kapishh Rajan)
print("Instructions on how to play the game:")
print("Welcome to Ultimate tic-tac-toe, this is a 2 player game where your goal is to place your markers (X and 0) into your desired positions to try and get 3 in a row.")
print("You can either try 3 in a row horizontally, 3 in a row vertically, or 3 in a row diagonaly")
print("But this is ULTIMATE tic-tac-toe, its not just one grid, now you got 6 grids that you have to fill out.")
print("Your goal is not only to get 3 in a row and win the grid, but also win 3 grids in a row in the same fashion as you would win the grids")
print("The square that you choose to place your marker in is the corresponding grid that your opponant will start in.")
print("May the best player win!!!!!")

root = tk.Tk()

root.title("Ultimate Tic Tac Toe")
root.configure(background="white")
root.minsize(1000, 1000)
root.maxsize(1200, 1200)
root.geometry("1200x1200+1200+100")

canvas = tk.Canvas(master = root, width = 1200, height = 1200)
canvas.grid(padx=2, pady=2, row=0, column=0, rowspan=10, columnspan=10)


screen = turtle.TurtleScreen(canvas)
c = turtle.RawTurtle(screen)

screen.tracer(0)

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



anygrid = True
####### Move function creates an X or O in an empty space #########
#Kapishh Rajan
def move(list_grid, box):
    global grid
    global anygrid
    global player

    if list_grid != grid and not anygrid:
        print("Invalid input")

    elif board[list_grid][box] == 0:
        board[list_grid][box] = player
        check(list_grid)
        grid = box
        anygrid = False
        display()
        if meta[box] != 0:
            anygrid = True
        player %= 2
        player += 1
        print('P'+str(player)+': ')
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
        if meta[i[0]] == meta[i[1]] == meta[i[2]] != 0:
            print('P' + str(player) + 'Wins')
            quit




display()


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

# Kapishh Rajan
def jp_move(row, col):
    global player
    list_grid, box = (floor(col/3)+3*floor(row/3), col%3 + row%3*3)
    player_move = move(list_grid, box)
    updategui()
    screen.update()

def updategui():
    for i in range(9):
        for j in range(9):
            if board[i][j] == 1:
                replace(3*(i%3) + j%3, 3*floor(i/3) + floor(j/3), 1)
            elif board[i][j] == 2:
                replace(3*(i%3) + j%3, 3*floor(i/3) + floor(j/3), 2)

# Hamza
def replace(col, row, p):
    i=row * 9 + col 
    button = buttons[i]
# destroys the button and places an X or an O in the empty space
    if p == 1:
        button.destroy()
        draw_x((col-4) * 135,(row-4) * -135)     
    else:
        button.destroy()
        draw_circle((col-4) * 135,(row-4) * -135)
# changes the active player

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
