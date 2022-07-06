#MiniMax Algorithm with Alpha-Beta Pruning!             #   
                                                        #
#Made by:                                               #
#Gabriel Dal Belo Gomes Santos                          #
#Henrique Tornelli Duarte                               #
#Vitor Teixeira                                         #
                                                        #
#########################################################

from TTT import BLANKSPACE, MAX_TOKEN, MIN_TOKEN, verifyVictoryCondiction
import time

score = {
    "DRAW": 0,
    " X ": 1,
    " O ": -1
}

MAX = 10000
MIN = -10000

def getPossibleMoves(board):    #Obtém uma lista dos espaços em branco(posições), que representam as possíveis jogadas
    positions = []
    for i in range(3):
        for j in range(3):
            if (board[i][j] == BLANKSPACE):
                positions.append([i, j])
    return positions

def minimax(board, player):
    if(verifyVictoryCondiction(board) == 1 and player == 0):   
        return score[MAX_TOKEN]                                      
    elif(verifyVictoryCondiction(board) == 1 and player == 1):
        return score[MIN_TOKEN]
    elif(verifyVictoryCondiction(board) == 0):
        return score["DRAW"]
    player = (player + 1)%2                     

    possibilities = getPossibleMoves(board)     
    bestValue = None
    for possibility in possibilities:           
        if (player == 0):                           
            board[possibility[0]][possibility[1]] = MAX_TOKEN   
        elif (player == 1):
            board[possibility[0]][possibility[1]] = MIN_TOKEN   
        value = minimax(board, player)                          
        board[possibility[0]][possibility[1]] = BLANKSPACE      

        if(bestValue is None):
            bestValue = value
        if(player == 0):                        
            if (value > bestValue):
                bestValue = value
        else:
            if (value < bestValue):             
                bestValue = value
    return bestValue                            

def minimaxWithABpruning(board, player, alpha, beta):          #Função chamada recursivamente, representando a busca em profundidade
    if(verifyVictoryCondiction(board) == 1 and player == 0):   #Se for alcançada Vitória ou Empate (nós que são folha), retorna um score associado ao estado terminal
        return score[MAX_TOKEN]                                #X = 1
    elif(verifyVictoryCondiction(board) == 1 and player == 1):
        return score[MIN_TOKEN]                                #O = -1
    elif(verifyVictoryCondiction(board) == 0):
        return score["DRAW"]                                   #DRAW = 0
    player = (player + 1)%2                                    #Troca o jogador quando a função é chamada novamente, representando a troca de profundidade

    possibilities = getPossibleMoves(board)                    #Obtém a lista dos possíveis movimentos partindo do estado "atual" (passado como argumento)
    if (player == 0):                                          #Poda pelo jogador X (MAX)
        bestValue = MIN
        for possibility in possibilities:
            board[possibility[0]][possibility[1]] = MAX_TOKEN
            value = minimaxWithABpruning(board, player, alpha, beta)
            board[possibility[0]][possibility[1]] = BLANKSPACE   
            bestValue = max(bestValue, value)
            alpha = max(alpha, bestValue)
            if (beta <= alpha):
                break
        return bestValue
    else:                                                       #Poda pelo jogador O (MIN)
        bestValue = MAX
        for possibility in possibilities:
            board[possibility[0]][possibility[1]] = MIN_TOKEN
            value = minimaxWithABpruning(board, player, alpha, beta)
            board[possibility[0]][possibility[1]] = BLANKSPACE 
            bestValue = min(bestValue, value)
            beta = min(beta, bestValue)
            if (beta <= alpha):
                break
        return bestValue
    
def automaticMove(board, player):               #Automatização do Minimax, para fazer com que um ou ambos os jogadores sejam a máquina
    possibilities = getPossibleMoves(board)
    bestValue = None
    bestMove = None
    print("Analyzing possibilities...")
    t1 = time.time()
    for possibility in possibilities:
        if (player == 0):
            board[possibility[0]][possibility[1]] = MAX_TOKEN
        elif (player == 1):
            board[possibility[0]][possibility[1]] = MIN_TOKEN
        #value = minimax(board, player)                         #Minimax puro
        value = minimaxWithABpruning(board, player, MIN, MAX)   #Minimax com Poda Alfa-Beta
        board[possibility[0]][possibility[1]] = BLANKSPACE
        print("Position: ", possibility, "Value:", value)       
        if(bestValue is None):
            bestValue = value
            bestMove = possibility
        elif(player == 0):
            if (value > bestValue):
                bestValue = value
                bestMove = possibility
        elif(player == 1):
            if (value < bestValue):
                bestValue = value
                bestMove = possibility
    tempoExec = time.time() - t1
    print("Choosed position: ", bestMove)
    print("Calculation time: {} seconds".format(tempoExec))
    return bestMove[0], bestMove[1]             #Retorna a linha e coluna da melhor possibilidade, para que a jogada seja feita
