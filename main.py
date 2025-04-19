#CODE FOR THE BOARD AYUSH/KAPISHH
################################################################################
board = [[0,0,0, 0,0,0, 0,0,0],  [0,0,0, 0,0,0, 0,0,0],  [0,0,0, 0,0,0, 0,0,0],
         [0,0,0, 0,0,0, 0,0,0],  [0,0,0, 0,0,0, 0,0,0],  [0,0,0, 0,0,0, 0,0,0],
         [0,0,0, 0,0,0, 0,0,0],  [0,0,0, 0,0,0, 0,0,0],  [0,0,0, 0,0,0, 0,0,0]]


meta = [0,0,0, 0,0,0, 0,0,0]


player = 0


grid = 4


ans = 0


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


# Move function creates an X or O in an empty space
def move(box):
    global grid
    global player


    if board[grid][box] == 0:
        board[grid][box] = player
        check(grid)
        grid = box
        display()
        if meta[box] == 0:
            grid = int(input('Choose any grid'))
    else:
        display()
        print('Square Taken')
        player -= 1






# WIP
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


# Mainloop
while True:
    try:
        player %= 2
        player += 1


        print('P' + str(player))
        move(int(input('Number 1-9: '))-1)
    except:
        display()
        print('Invalid Input')




#########################
#Kapishh add a conditional to make sure that when you enter the same value, it says "value already chosen"
