from random import choice
board = [' ']*9


def findEmpty(board):
    for index, item in enumerate(board):
        if item == ' ':
            return index


def printBoard(board):
    print('   |   |   ')
    print(f' {board[0]} | {board[1]} | {board[2]} ')
    print('   |   |   ')
    print('_'*11)
    print('   |   |   ')
    print(f' {board[3]} | {board[4]} | {board[5]} ')
    print('   |   |   ')
    print('_'*11)
    print('   |   |   ')
    print(f' {board[6]} | {board[7]} | {board[8]} ')
    print('   |   |   ')


def boardFilled(board):
    return ' ' not in board


def gameOver(board, letter):
    rowCheck = (board[0] == letter and board[1] == letter and board[2] == letter) or (board[3] == letter and board[4] == letter and board[5] == letter) or (board[6] == letter and board[7] == letter and board[8] == letter)

    diagonalCheck = (board[0] == letter and board[4] == letter and board[8] == letter) or (board[2] == letter and board[4] == letter and board[6] == letter) 

    columnCheck = (board[0] == letter and board[3] == letter and board[6] == letter) or (board[1] == letter and board[4] == letter and board[7] == letter) or (board[2] == letter and board[5] == letter and board[8] == letter)
    
    return rowCheck or diagonalCheck or columnCheck


def computeMoveMinimax(board,depth=0,isComputer=True):
    if gameOver(board,'X'):
        return (-10+depth,None)
    elif gameOver(board,'O'):
        return (10-depth,None)        
    elif boardFilled(board):
        return (0,None)
    if isComputer:
        bestScore=-float("inf")
        bestMove=None
        possibleMoves=[i for i,el in enumerate(board) if el==' ']
        # print(possibleMoves)
        for move in possibleMoves:
            board[move]='O'
            # print(f'Computer Trying O at {move}')
            score=computeMoveMinimax(board,depth+1,False)[0]
            b1=score>bestScore
            b2=score>=bestScore
            if(choice([b1,b2])):
                  bestScore=score
                  bestMove=move
            board[move]=' '
        return bestScore,bestMove
    else:
        bestScore=float("inf")
        bestMove=None        
        possibleMoves=[i for i,el in enumerate(board) if el==' ']
        for move in possibleMoves:
            board[move]='X'
            score=computeMoveMinimax(board,depth+1,True)[0]
            b1=score<bestScore
            b2=score<=bestScore
            if(choice([b1,b2])):
                bestScore=score
                bestMove=move
            board[move]=' '
        return bestScore,bestMove


def computeMoveAlphaBetaPruning(board,depth=0,alpha=-float("inf"),beta=float("inf"),isComputer=True):
    if gameOver(board,'X'):
        return (-10+depth,None)
    elif gameOver(board,'O'):
        return (10-depth,None)        
    elif boardFilled(board):
        return (0,None)
    if isComputer:
        bestScore=-float("inf")
        bestMove=None
        possibleMoves=[i for i,el in enumerate(board) if el==' ']
        # print(possibleMoves)
        for move in possibleMoves:
            board[move]='O'
            # print(f'Computer Trying O at {move}')
            score=computeMoveAlphaBetaPruning(board,depth+1,alpha,beta,False)[0]
            if(score>bestScore):
                bestScore=score
                bestMove=move
            alpha=max(alpha,bestScore)
            board[move]=' '
            if alpha>=beta:
                break
        return bestScore,bestMove
    else:
        bestScore=float("inf")
        bestMove=None        
        possibleMoves=[i for i,el in enumerate(board) if el==' ']
        for move in possibleMoves:
            board[move]='X'
            score=computeMoveAlphaBetaPruning(board,depth+1,alpha,beta,True)[0]
            if(score<bestScore):
                bestScore=score
                bestMove=move
            beta=min(beta,bestScore)
            board[move]=' '
            if beta<=alpha:
                break
        return bestScore,bestMove


    
def takeMove():
    try:
        move = 10
        while move > 9 or move<1 :
            move = int(input("Enter The Index To Place Your X: "))
            if move < 10 and board[move-1]==' ':
                return move-1
    except:
        print("Enter an Ineger from 1 to 9")
        return takeMove()
    
def playGame(board):
    while True:
        pMove=takeMove()
        availableMoves=[i for i,el in enumerate(board) if el==' ']
        if pMove in availableMoves:
            board[pMove]='X'
        else:
            continue
        if gameOver(board,'O'):
            printBoard(board)
            print("COMPUTER WON")
            break
        if gameOver(board,'X'):
            printBoard(board)
            print("COMPUTER LOST")
            break
        if boardFilled(board):
            printBoard(board)
            print("TIE")
            break
        printBoard(board)
        cMove=computeMoveAlphaBetaPruning(board)[1]
        print(f"Computer Moved {cMove+1}")
        board[cMove]='O'
        if gameOver(board,'O'):
            printBoard(board)
            print("COMPUTER WON")
            break
        if gameOver(board,'X'):
            printBoard(board)
            print("COMPUTER LOST")
            break
        if boardFilled(board):
            printBoard(board)
            print("TIE")
            break
        printBoard(board)
        
        
if __name__ == "__main__":
    playGame(board)
