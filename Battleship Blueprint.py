from random import randrange
#Creates a 5x5 board.
def MakeBoard(square):
    board = [["[   ]"]*square]*square
    return board
#Method which prints the game board with labels 0-4
def PrintBoard(board):
    y = "+  0"
    for i in range(len(board[0])-1):
        y = y + "    " + str(i + 1)
    print(y)
    for row in range(len(board[0])):
        y = str(row)
        for col in range(len(board[0])):
            y = y + board[row][col]
        print(y)

board = MakeBoard(4)
PrintBoard(board)