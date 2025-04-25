# -*- coding: utf-8 -*-
# Ultimate Tic Tac Toe

#CODE FOR THE BOARD ~AYUSH
################################################################################
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
    board[grid] = ['⁕' if i == 0 else i for i in board[grid]]
   
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
def move(box):
    global grid
    global player




    if board[grid][box] == 0:
        board[grid][box] = player
        check(grid)
        grid = box
        display()
        if meta[box] != 0:
            grid = int(input('Choose any grid'))
    else:
        display()
        print('Square Taken')
        player -= 1


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

while True:
    try:
        # Alternate between players 1 and 2
        player %= 2
        player += 1

        print('PLAYER ' + str(player))
    
        # Validate input and ensure it's within the range 1-9
        player_input = int(input('Pick a Number 1-9: '))
        if not (1<= int(player_input) <= 9):
            print("input must be between 1 and 9")
        
        player_move = move(int(player_input) - 1)

### checks if there are any errors in the input

    except ValueError as value_error:
        print(f"Invalid Input: {value_error} - Please enter a number between 1 and 9.")
        
    except IndexError as index_error:
        print(f"Invalid Input: {index_error} - Please enter a number between 1 and 9.")

    except Exception as exception:
        display()
        print(f"An error occurred: {exception} - Please try again.")

#Keeps the player number if there is any error present 
    if ValueError or IndexError or Exception == True:
        player %= 2
        player += 1


    


