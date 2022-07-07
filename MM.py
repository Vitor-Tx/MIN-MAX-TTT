#Algoritmo Minimax com Poda Alfa-Beta                   #   
                                                        #
#Made by:                                               #
#Gabriel Dal Belo Gomes Santos                          #
#Henrique Tornelli Duarte                               #
#Vitor Teixeira                                         #
                                                        #
#########################################################

from TTT import dictionary, verifyVictoryCondiction
import time

MAX = 10000
MIN = -10000

def getPossibleMoves(board):    #Obtém uma lista dos espaços em branco(posições), que representam as possíveis jogadas
    positions = []
    for i in range(3):
        for j in range(3):
            if (board[i][j] == dictionary["W"]):
                positions.append([i, j])
    return positions

def minimax(board, player, depth):
    if(verifyVictoryCondiction(board) == 1 and player == 0):   
        return (10 - depth)                                      
    elif(verifyVictoryCondiction(board) == 1 and player == 1):
        return (depth - 10)    
    elif(verifyVictoryCondiction(board) == 0):
        return 0
    depth += 1
    player = (player + 1)%2                     

    possibilities = getPossibleMoves(board)     
    bestValue = None
    for possibility in possibilities:           
        if (player == 0):                           
            board[possibility[0]][possibility[1]] = dictionary["X"]  
        elif (player == 1):
            board[possibility[0]][possibility[1]] = dictionary["O"]  
        value = minimax(board, player, depth)                          
        board[possibility[0]][possibility[1]] = dictionary["W"]    

        if(bestValue is None):
            bestValue = value
        if(player == 0):                        
            if (value > bestValue):
                bestValue = value
        else:
            if (value < bestValue):             
                bestValue = value
    return bestValue                            

def minimaxWithABpruning(board, player, depth, alpha, beta):   #Função chamada recursivamente, representando a busca em profundidade.
    if(verifyVictoryCondiction(board) == 1 and player == 0):   #Se for alcançada Vitória ou Empate (nós que são folha), retorna um score associado ao estado terminal.
        return (10 - depth)                                    #X = 1
    elif(verifyVictoryCondiction(board) == 1 and player == 1):
        return (depth - 10)                                    #O = -1
    elif(verifyVictoryCondiction(board) == 0):
        return 0                                               #DRAW = 0
    player = (player + 1)%2                                    #Troca o jogador quando a função é chamada novamente, representando a próxima jogada.
    depth += 1

    possibilities = getPossibleMoves(board)                    #Obtém a lista dos possíveis movimentos partindo do estado "atual" (passado como argumento).
    if (player == 0):                                          #Poda pelo jogador X (MAX).
        bestValue = MIN
        for possibility in possibilities:
            board[possibility[0]][possibility[1]] = dictionary["X"]
            value = minimaxWithABpruning(board, player, depth, alpha, beta)
            board[possibility[0]][possibility[1]] = dictionary["W"]  
            bestValue = max(bestValue, value)
            alpha = max(alpha, bestValue)
            if (beta <= alpha):
                break
        return bestValue
    else:                                                       #Poda pelo jogador O (MIN).
        bestValue = MAX
        for possibility in possibilities:
            board[possibility[0]][possibility[1]] = dictionary["O"]
            value = minimaxWithABpruning(board, player, depth, alpha, beta)
            board[possibility[0]][possibility[1]] = dictionary["W"]
            bestValue = min(bestValue, value)
            beta = min(beta, bestValue)
            if (beta <= alpha):
                break
        return bestValue

def automaticMove(board, player):               #Automatização do Minimax, para fazer com que um ou ambos os jogadores sejam a máquina.
    bestMove = None
    depth = 0
    print("Analizando possíveis movimentos...")
    t1 = time.time()
    possibilities = getPossibleMoves(board)                    #Obtém a lista dos possíveis movimentos partindo do estado "atual" (passado como argumento).
    if (player == 0):                                          #Poda pelo jogador X (MAX).
        bestValue = MIN
        for possibility in possibilities:
            board[possibility[0]][possibility[1]] = dictionary["X"]
            value = minimaxWithABpruning(board, player, depth, MIN, MAX)
            #value = minimax(board, player, depth)
            board[possibility[0]][possibility[1]] = dictionary["W"]
            print("Posição: ", possibility, "Valor:", value)
            if(bestValue is None):
                bestValue = value
                bestMove = possibility
            elif (value > bestValue):
                bestValue = value
                bestMove = possibility
        tempoExec = time.time() - t1
        print("Posição escolhida: ", bestMove)
        print("Tempo de execução: {} segundos".format(tempoExec))
        return bestMove[0], bestMove[1]
    else:                                                       #Poda pelo jogador O (MIN).
        bestValue = MAX
        for possibility in possibilities:
            board[possibility[0]][possibility[1]] = dictionary["O"]
            value = minimaxWithABpruning(board, player, depth, MIN, MAX)
            #value = minimax(board, player, depth)
            board[possibility[0]][possibility[1]] = dictionary["W"]
            print("Posição: ", possibility, "Valor:", value)
            if(bestValue is None):
                bestValue = value
                bestMove = possibility
            elif (value < bestValue):
                bestValue = value
                bestMove = possibility
        tempoExec = time.time() - t1
        print("Posição escolhida: ", bestMove)
        print("Tempo de execução: {} segundos".format(tempoExec))
        return bestMove[0], bestMove[1]
