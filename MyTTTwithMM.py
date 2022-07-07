#Jogo da Velha com algoritmo Minimax e Poda Alfa-Beta!  #   
                                                        #
#Um trabalho de:                                        #
#Gabriel Dal Belo Gomes Santos                          #
#Henrique Tornelli Duarte                               #
#Vitor Teixeira                                         #
                                                        #
#########################################################
from TTT import * 
from MM import automaticMove

board, amounts = createBoard()                           #função responsável por criar o tabuleiro de acordo com a especificação do usuário, e retorna não só ele...
                                                         #... como também a a quantidade de X, O e espaços em branco.
player = None                                            #variável que associa um valor á cada jogador. 0 = X, 1 = O.
if (amounts["X"] == amounts["O"]):                       
    if (verifyVictoryCondiction(board) == 1):
        player = 1
    else:
        player = 0
else:
    if (verifyVictoryCondiction(board) == 1):
        player = 0
    else:
        player = 1

while (verifyVictoryCondiction(board) == -1):            # -1 = Condição de Vitória ainda não alcançada. 1 = Vitória, 0 = Empate.
    printBoard(board)                                    
    selectedPosition = None                              
    if (player == 0):                                    #vez do X, que em uma malha vazia, é o primeiro a jogar. Consequentemente, será nosso MAX.
        print("Vez de:", dictionary["X"])
        #Nas duas linhas seguintes, apenas uma deve permanecer comentada. Em caso de troca, comentar a outra. O mesmo vale dentro do próximo "elif"
        selectedPosition = automaticMove(board, player) #função usada quando se quer que um jogador seja a máquina.
        #selectedPosition = getSelectedPosition(board)    #função usada quando se quer que o jogador seja o usuário.
    elif (player == 1):                                  #Vez do O, nosso MIN.
        print("Vez de:", dictionary["O"])
        selectedPosition = automaticMove(board, player)  
        #selectedPosition = getSelectedPosition(board)
    doMove(board, selectedPosition[0], selectedPosition[1], player)     #selectedPosition[0] = linha, selectedPosition[1] = coluna.
    if (verifyVictoryCondiction(board) == -1):           #Enquanto não for alcançada a Vitória ou o Empate, realizará a troca de jogador após uma jogada.
        player = (player + 1)%2                          #Macete para trocar o jogador. O resultado uma vez será 1, na outra 0, e assim por diante.
    
printBoard(board)                                        #Após verifyVictoryCondiction retornar 1 ou 0, printa o tabuleiro e o resultado.
if (verifyVictoryCondiction(board) == 0):                #Em caso de empate.
    print("EMPATE")
elif (player == 0):                                     
    print("Vencedor:", dictionary["X"])                        #Em caso de X ser vitorioso.
else:
    print("Vencedor:", dictionary["O"])                        #Em caso de O ser vitorioso.
