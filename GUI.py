# Hamza/Yousuf
import tkinter as tk
import turtle
from turtle import RawTurtle, ScrolledCanvas, TurtleScreen
from math import floor





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

for i in (135*1.5, -135*1.5):
    c.goto(-600, i)
    c.pendown()
    c.forward(1200)
    c.penup()

c.setheading(90)

for i in (135*1.5, -135*1.5):
    c.goto(i, -600)
    c.pendown()
    c.forward(1200)
    c.penup()

buttons = []
placeholder = tk.PhotoImage()

x=0
def jp_move(row, col):
    global x
    i=row * 9 + col 
    button = buttons[i]
    if x == 0:
        button.destroy()
        draw_x((col-4) * 135,(row-4) * -135)
        x+=1
        x%=2   
    else:
        button.destroy()
        draw_circle((col-4) * 135,(row-4) * -135)
        x+=1
        x%=2


for row in range(9):
    root.rowconfigure(row,minsize=100, weight=1)
    
    for column in range(9):
        
        root.columnconfigure(column,minsize=100, weight=1)
        button = tk.Button(root,image=placeholder, width= 100, height = 100,command= lambda row =  row, col = column : jp_move(row, col))
        button.grid(column=column, row=row)
        buttons.append(button)
#############################################################



root.mainloop()
