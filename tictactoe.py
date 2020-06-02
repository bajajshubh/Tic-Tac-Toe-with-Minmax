9# -*- coding: utf-8 -*-
"""
Created on Sun May 31 18:26:06 2020
"""

board = [' ' for x in range(10)] 

def insertLetter(letter, pos):
    board[pos] = letter

def spaceIsFree(pos):
    return board[pos] == ' '

def printBoard(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

def isWinner(bo, le):
    return (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or (bo[1] == le and bo[2] == le and bo[3] == le) or (bo[1] == le and bo[4] == le and bo[7] == le) or (bo[2] == le and bo[5] == le and bo[8] == le) or (bo[3] == le and bo[6] == le and bo[9] == le) or (bo[1] == le and bo[5] == le and bo[9] == le) or (bo[3] == le and bo[5] == le and bo[7] == le)
 
def playerMove():
    run = True
    while run:
        move = input('Please select a position to place an \'O\' (1-9): ')
        try:
            move = int(move)
            if  move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('O', move)
                else:
                    print('Sorry, this space is occupied!')
            else:
                print('Please type a number within the range!')
        except:
            print('Please type a number!')
            

def compMove():
    bestScore = float('-inf')
    move = None
    
    for i in range(1, 10):
        if(spaceIsFree(i)):
            board[i] = 'X'
            score = miniMax(board, 0, False)
            board[i] = ' '
            if score>bestScore:
                bestScore = score
                move = i
    insertLetter('X', move)
   
    

def miniMax(board, depth, isMaximizing):
    
    if not(isWinner(board, 'X') == False and isWinner(board, 'O') == False and isBoardFull(board) == False):
      if(isWinner(board, 'X')):
          return 1
      elif(isWinner(board, 'O')):
          return -1
      elif(isWinner(board, 'X') == False and isWinner(board, 'O') == False and isBoardFull(board) == True):
          return 0
      
    
    if(isMaximizing):
        bestScore = float('-inf')
        for i in range(1, 10):
            if(spaceIsFree(i)):
                board[i] = 'X'
                score = miniMax(board, depth+1, False)
                board[i] = ' '
                bestScore = max(score, bestScore)
        return bestScore
    else:
        bestScore = float('inf')
        for i in range(1, 10):
            if(spaceIsFree(i)):
                board[i] = 'O'
                score = miniMax(board, depth+1, True)
                board[i] = ' '
                bestScore = min(score, bestScore)
        return bestScore
        

def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

def main():
    print('Welcome to the Game')
    printBoard(board)
    
    while not(isBoardFull(board)):
        if not(isWinner(board, 'O')):
            compMove()
            printBoard(board)
        else:
            print('Congrats, O\'s won this time!')
            break
        if not(isWinner(board, 'X')):
            playerMove()
            printBoard(board)
        else:
            print('Sorry, X\'s won this time!')
            break
        
        
        
    
    if isBoardFull(board):
        print('Game is tie')
        
main()
    