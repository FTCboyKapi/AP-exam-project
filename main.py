#CODE FOR THE BOARD 
################################################################################
board = [[0,0,0, 0,0,0, 0,0,0],  [0,0,0, 0,0,0, 0,0,0],  [0,0,0, 0,0,0, 0,0,0], 
         [0,0,0, 0,0,0, 0,0,0],  [0,0,0, 0,0,0, 0,0,0],  [0,0,0, 0,0,0, 0,0,0], 
         [0,0,0, 0,0,0, 0,0,0],  [0,0,0, 0,0,0, 0,0,0],  [0,0,0, 0,0,0, 0,0,0]]

meta = [0,0,0, 0,0,0, 0,0,0]

player = 0

grid = 4

# Display will become irrelevant when a GUI is made
# List comprehension: https://docs.python.org/3/glossary.html#term-list-comprehension
def display():
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
    if board[grid][box] == 0:
        board[grid][box] = player+1
    print(board)
    grid = box

# WIP
def check(list_grid):
    for i in [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]:
        print(i)
        print(i[2])
        print(board[list_grid][i[0]] == board[list_grid][i[1]] == board[list_grid][i[2]] != 0)
        if board[list_grid][i[0]] == board[list_grid][i[1]] == board[list_grid][i[2]] != 0:
            for j in range(9):
                board[list_grid][j] = board[list_grid][[i][0]]
                meta[list_grid] = player+1
                print(meta)

# Mainloop
while True:
    player %= 2
    display()
    print('P' + str(player+1))

    move(int(input('Number 1-9: '))-1)
    player += 1
    check(grid)

#########################
#Kapishh add a conditional to make sure that when you enter the same value, it says "value already chosen"
