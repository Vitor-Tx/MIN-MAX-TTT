#TicTacToe logic!                                       #  
                                                        #
#Made by:                                               #
#Gabriel Dal Belo Gomes Santos                          #
#Henrique Tornelli Duarte                               #
#Vitor Teixeira                                         #
                                                        #
#########################################################

import math

BLANKSPACE = "   "
MAX_TOKEN = " X "
MIN_TOKEN = " O "

dictionary = {
    "X": MAX_TOKEN,
    "O": MIN_TOKEN,
    "W": BLANKSPACE
}

def createBoard():
    print("Welcome! Let's create our board!")
    print("*If the amount of X is greater than that of O in the board, O will be the first player!")
    print("*Else if the amount of X is equal than that of O, X will be the first player!")
    print("*Otherwise, if the amount of O is greather than that of X in the board, it will be a invalid board!")
    print("*The maximum amount of X is 5, and for O is 4.")
    print("*If the amount of X is equal to that of O, this amount must be less than 4.")
    print("---------------------------------------------------------------------------------------------------")

    board = [
            [BLANKSPACE, BLANKSPACE, BLANKSPACE],
            [BLANKSPACE, BLANKSPACE, BLANKSPACE],
            [BLANKSPACE, BLANKSPACE, BLANKSPACE]
    ]
    
    amounts = {}
    amounts["X"] = 0
    amounts["O"] = 0
    amounts["W"] = 0
    
    first = (amounts["X"] < 6) and (amounts["O"] < 5)
    second = amounts["O"] == (amounts["X"] - 1)
    third = (amounts["X"] == amounts["O"]) and (amounts["X"] < 4)
    fourth = (second and (not third)) or ((not second) and third)   #second xor third
    isValid = False
    
    while (isValid == False):
        for i in range(3):
            for j in range(3):
                token = None
                while (token != "X" and token != "O" and token != "W"):
                    token = input("Input the " + str(j+1) + " value of the " + str(i+1) + " line (X, O, W(Blankspace): ")
                board[i][j] = dictionary[token]
            
                if (token == "X"):
                    amounts["X"] += 1
                elif (token == "O"):
                    amounts["O"] += 1
                else:
                    amounts["W"] += 1
                    
        if (first and fourth):
            isValid = True
        else:
            print("------------------------------------")
            print("Invalid board! let's create again ;)")
            print("------------------------------------")
         
    return board, amounts

def printBoard(board):
    print(" ")
    print("-----------")
    for i in range(3):
        print("|".join(board[i]))
        print("-----------")
        

def getValidInput(message): #Verifica se uma entrada é válida. Usada tanto para obter a linha quanto a coluna da jogada
    try:
        n = int(input(message))
        if (n >= 1 and n <=3):
            return n-1
        else:
            print("Must be in the especified range!")
            return getValidInput(message)
    except:
        print("Must be a integer value!")
        return getValidInput(message)

def getSelectedPosition(board): #Converte os valores obtidos da função anterior em uma posição, retornando ela para que a respectiva jogada seja feita
    while(1):
        selectedLine = getValidInput("Input line number (1, 2 or 3): ")
        selectedColumn = getValidInput("Input column number (1, 2 or 3): ")
        if(board[selectedLine][selectedColumn] == BLANKSPACE):
            return selectedLine, selectedColumn
        else:
            print("Position already in use!")

def doMove(board, selectedLine, selectedColumn, player):    #Faz a jogada utilizando a posição obtida pela função anterior
    if (player == 0):
        board[selectedLine][selectedColumn] = MAX_TOKEN
    else:
        board[selectedLine][selectedColumn] = MIN_TOKEN

def verifyVictoryCondiction(board): #Função usada á cada jogada para verificar o estado do jogo  
    for i in range(3):              # 1 = Vitória alcançada, independente do jogador
        if ((board[i][0] != BLANKSPACE) and (board[i][0] == board[i][1] == board[i][2])):
            return 1
        if ((board[0][i] != BLANKSPACE) and (board[0][i] == board[1][i] == board[2][i])):
            return 1
    if ((board[0][0] != BLANKSPACE) and (board[0][0] == board[1][1] == board[2][2])):
        return 1
    if ((board[0][2] != BLANKSPACE) and (board[0][2] == board[1][1] == board[2][0])):
        return 1

    for i in range(3):
        for j in range(3):
            if(board[i][j] == BLANKSPACE):
                return -1       # -1 = Jogo ainda em andamento
    return 0    # 0 = Empate
