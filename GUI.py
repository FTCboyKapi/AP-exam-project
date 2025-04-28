# Hamza/Yousuf
import tkinter as tk
import turtle
from turtle import RawTurtle, ScrolledCanvas, TurtleScreen
from math import floor

#############################################################
#Displays the instructions on the screen for the players to see. 
#(Kapishh Rajan)
print("Welcome to Ultimate tic-tac-toe, this is a 2 player game where your goal is to place your markers (X and 0) into your desired positions to try and get 3 in a row.")
print("You can either try 3 in a row horizontally, 3 in a row vertically, or 3 in a row diagonaly")
print("But this is ULTIMATE tic-tac-toe, its not just one grid, now you got 6 grids that you have to fill out.")
print("Your goal is not only to get 3 in a row and win the grid, but also win 3 grids in a row in the same fashion as you would win the grids")
print("")
#not finished yet 

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

# 
player=0
def jp_move(row, col):
    list_grid, box = (floor(col/3)+3*floor(row/3), col%3 + row%3*3)
    replace(row, col)

# Hamza
def replace(row, col):
    global player
    i=row * 9 + col 
    button = buttons[i]
# destroys the button and places an X or an O in the empty space
    if player == 0:
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
#############################################################



root.mainloop()
