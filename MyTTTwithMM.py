#TicTacToe with MiniMax Algotithm and Alfa-Beta Pruning!#   
                                                        #
#Made by:                                               #
#Gabriel Dal Belo Gomes Santos                          #
#Henrique Tornelli Duarte                               #
#Vitor Teixeira                                         #
                                                        #
#########################################################
from TTT import * 
from MM import automaticMove

board, amounts = createBoard()
player = None                                            # 0 = X, 1 = 0
if (amounts["X"] == amounts["O"]):
    player = 0                                               
else:
    player = 1

while (verifyVictoryCondiction(board) == -1):            # -1 = Condição de Vitória ainda não alcançada. 1 = Vitória, 0 = Empate.
    printBoard(board)                                    
    selectedPosition = None                              
    if (player == 0):                                    #Vez do X, que é o primeiro a jogar, e também será nosso MAX.
        print("Turn:", MAX_TOKEN)
        selectedPosition = automaticMove(board, player)  #usada quando se quer que o respectivo jogador seja a máquina.
        #selectedPosition = getSelectedPosition(board)   #usada quando se quer que o respectivo jogador seja o usuário.
    elif (player == 1):                                  #Vez do O, nosso MIN.
        print("Turn:", MIN_TOKEN)
        selectedPosition = automaticMove(board, player)  
        #selectedPosition = getSelectedPosition(board)
    doMove(board, selectedPosition[0], selectedPosition[1], player)     #selectedPosition[0] = linha, selectedPosition[1] = coluna.
    if (verifyVictoryCondiction(board) == -1):
        player = (player + 1)%2                          #Macete para trocar o jogador. O resultado uma vez será 1, na outra 0, e assim por diante.
    
printBoard(board)                                        #Após verifyVictoryCondiction retornar 1 ou 0, printa o tabuleiro e o resultado
if (verifyVictoryCondiction(board) == 0):               
    print("Winner: DRAW")
elif (player == 0):                                     
    print("Winner:", MAX_TOKEN)                         
else:
    print("Winner:", MIN_TOKEN)
