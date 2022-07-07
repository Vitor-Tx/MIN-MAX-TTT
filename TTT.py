#Lógica do Jogo da Velha!                               #  
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
    "X": " X ",
    "O": " O ",
    "W": "   "
}

def createBoard():
    print("Bem-vindo! vamos criar nosso tabuleiro!")
    print("*Se a quantidade de X for maior que a de O no tabuleiro, significa que O será o primeiro a jogar!")
    print("*Se não, se a quantia de X for igual á de O, significa que X será o primeiro a jogar!")
    print("*Caso contrário, se a quantidade de O for maior que a de X no tabuleiro, então se tratará de um tabuleiro inválido!")
    print("*A quantidade máxima de X é 5, e de O é 4.")
    print("*Se a quantia de X é igual á de O, então essa quantia deve ser menor do que 5.")
    print("---------------------------------------------------------------------------------------------------")

    #tabuleiro vazio.
    board = [[dictionary["W"], dictionary["W"], dictionary["W"]],
            [dictionary["W"], dictionary["W"], dictionary["W"]],
            [dictionary["W"], dictionary["W"], dictionary["W"]]
    ]

    amounts = {}
    amounts["X"] = 0
    amounts["O"] = 0
    amounts["W"] = 0

    #regras que devem ser respeitas para garantir que o dado tabuleiro seja válido e coeso.
    first = (amounts["X"] < 6) and (amounts["O"] < 5)
    second = amounts["O"] == (amounts["X"] - 1)
    third = (amounts["X"] == amounts["O"]) and (amounts["X"] < 5)
    fourth = (second and (not third)) or ((not second) and third)   #second xor third
    isValid = False         #variável cujo valor é trocado quando se garante que o tabuleiro é válido e coeso.
    
    while (isValid == False):
        for i in range(3):          #preenchimento do tabuleiro dado em laços aninhados.
            for j in range(3):
                token = None
                while (token != "X" and token != "O" and token != "W"):     #só é permitido inserir as três letras maiúsculas que representam os tokens: X, O e W.
                    token = input("Coloque o " + str(j+1) + " valor da " + str(i+1) + " linha(X, O, W(Espaço em Branco): ")
                board[i][j] = dictionary[token]
            
                if (token == "X"):
                    amounts["X"] += 1
                elif (token == "O"):
                    amounts["O"] += 1
                else:
                    amounts["W"] += 1
                    
        if (first and fourth):      #se essas duas condições forem verdadeiras, é um tabuleiro válido, e o preenchimento está completo.
            isValid = True
        else:
            print("--------------------------------------------")
            print("Tabuleiro inválido! Vamos criar novamente ;)")
            print("--------------------------------------------")
         
    return board, amounts

def printBoard(board):
    print(" ")
    print("-----------")
    for i in range(3):
        print("|".join(board[i]))
        print("-----------")
        

def getValidInput(message): #Verifica se uma entrada dada pelo usuário é válida. Usada tanto para obter a linha quanto a coluna da jogada.
    try:
        n = int(input(message))
        if (n >= 1 and n <=3):
            return n-1
        else:
            print("Deve estar no intervalo especificado!")
            return getValidInput(message)
    except:
        print("Deve ser um valor inteiro!")
        return getValidInput(message)

def getSelectedPosition(board): #Converte os valores obtidos na função anterior em uma posição, retornando ela para que a respectiva jogada do usuário seja feita.
    while(1):
        selectedLine = getValidInput("Insira o número da linha (1, 2 ou 3): ")
        selectedColumn = getValidInput("Insira o número da coluna (1, 2 or 3): ")
        if(board[selectedLine][selectedColumn] == BLANKSPACE):
            return selectedLine, selectedColumn
        else:
            print("Esta posição já está sendo utilizada! tente novamente.")

def doMove(board, selectedLine, selectedColumn, player):    #Faz a jogada utilizando a posição obtida pela função anterior.
    if (player == 0):
        board[selectedLine][selectedColumn] = MAX_TOKEN
    else:
        board[selectedLine][selectedColumn] = MIN_TOKEN

def verifyVictoryCondiction(board): #Função usada á cada jogada para verificar o estado do jogo.
    for i in range(3):              # 1 = Vitória alcançada, independente do jogador
        if ((board[i][0] != BLANKSPACE) and (board[i][0] == board[i][1] == board[i][2])):   #verifica se há uma trinca de tokens iguais em alguma linha.
            return 1
        if ((board[0][i] != BLANKSPACE) and (board[0][i] == board[1][i] == board[2][i])):   #verifica se há uma trinca de tokens iguais em alguma coluna.
            return 1
    if ((board[0][0] != BLANKSPACE) and (board[0][0] == board[1][1] == board[2][2])):       #verifica se há uma trinca de tokens iguais na diagonal principal.
        return 1
    if ((board[0][2] != BLANKSPACE) and (board[0][2] == board[1][1] == board[2][0])):       #verifica se há uma trinca de tokens iguais na diagonal oposta.
        return 1

    for i in range(3):
        for j in range(3):
            if(board[i][j] == BLANKSPACE):
                return -1       # -1 = Há pelo menos uma posição em branco ainda. Logo, o jogo ainda se encontra em andamento.
    return 0                    # 0 = Empate, a famosa "Velha"
