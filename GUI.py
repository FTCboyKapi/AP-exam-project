import tkinter as tk

root = tk.Tk()

root.title("Ultimate Tic Tac Toe")
root.configure(background="white")
root.minsize(1000, 1000)
root.maxsize(1200, 1200)
root.geometry("1200x1200+1200+100")
buttons = []

def jp_move(x, y):
    print(x*9+y)
    return(x*9+y)

for row in range(9):
    for column in range(9):
        button = tk.Button(root, width= 16, height = 8,command= lambda x=row, y=column: jp_move(x, y))
        button.grid(column=column, row=row)
        buttons.append(button)




root.mainloop()