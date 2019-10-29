# CMPT 120 Intro to Programming
# Lab #6 -  Lists and Error Handling
# Author: Descartes Tuyishime
# Created: 2019-10-22
symbol = [ " ", "x", "o" ]

def printRow(row):
    rowStr = "| "
    for square in row:
        rowStr = rowStr + symbol[square] + " | "
    print(rowStr)

    pass

def printBoard(board):
    print("+------------+")
    for row in board:
        printRow(row)
        print("+------------+")

    pass

def markBoard(board, row, col, player):
    
    if board[row][col] == 0:
        board[row][col] = player
        return True
    else:
        return False

    pass

def getPlayerMove():
    row = int(input("Enter the row number: ")) 
    col = int(input("Enter the column number: ")) 
    return (row,col)
    pass

def hasBlanks(board):

    for row in board:
        for square in row:
            if square == 0:
                return True
    return False

    pass

def main():
    board= [[0,0,0],
            [0,0,0],
            [0,0,0]] 
    player = 1

    while hasBlanks(board):
        printBoard(board)
        row,col = getPlayerMove()
        markBoard(board,row,col,player)
        player = player % 2 + 1

    printBoard(board)


main()
