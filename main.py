# Make a tictactoe

BOARD = [
        '-','-','-',
        '-','-','-',
        '-','-','-'
        ]

def printBoard(board):
    print(board[0] + '|' + board[1] + '|' + board[2])
    print(board[3] + '|' + board[4] + '|' + board[5])
    print(board[6] + '|' + board[7] + '|' + board[8])

def runGame():

    turn = 'X'
    count = 0
    
    while True:
        printBoard(BOARD)
        print(f"{turn} turn. Move to which place : ")
        move = int(input())

        if BOARD[move - 1] == '-':
            BOARD[move - 1] = turn
            count += 1
        else:
            print(f"That place has been filled with {BOARD[move - 1]}")
            continue
        
        # Check row
        if BOARD[0] == BOARD[1] == BOARD[2] != '-':
            printBoard(BOARD)
            print(f"{turn} won!")
            isWin = True
            break
        elif BOARD[3] == BOARD[4] == BOARD[5] != '-':
            printBoard(BOARD)
            print(f"{turn} won!")
            isWin = True
            break
        elif BOARD[6] == BOARD[7] == BOARD[8] != '-':
            printBoard(BOARD)
            print(f"{turn} won!")
            isWin = True
            break

        # check column
        if BOARD[0] == BOARD[3] == BOARD[6] != '-':
            printBoard(BOARD)
            print(f"{turn} won!")
            isWin = True
            break
        elif BOARD[1] == BOARD[4] == BOARD[7] != '-':
            printBoard(BOARD)
            print(f"{turn} won!")
            isWin = True
            break
        elif BOARD[2] == BOARD[5] == BOARD[8] != '-':
            printBoard(BOARD)
            print(f"{turn} won!")
            isWin = True
            break

        # Check Diagonal
        if BOARD[0] == BOARD[4] == BOARD[8] != '-':
            printBoard(BOARD)
            print(f"{turn} won!")
            isWin = True
            break
        elif BOARD[2] == BOARD[4] == BOARD[6] != '-':
            printBoard(BOARD)
            print(f"{turn} won!")
            isWin = True
            break
        
        if count == 9:
            printBoard(BOARD)
            print("Game Over!")
            print("TIE GAME!!")
            break

        # Change player
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
        
if __name__ == '__main__':
    runGame()
