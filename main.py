from Classes import *

if __name__ == '__main__':
    gameOver = False
    game = ChessBoard()
    gameMode = input("Choose game mode ('pvp' or 'pvc' or 'cvc'): ")
    if gameMode == "pvp":
        player1 = input("Player 1 (White) name: ")
        player2 = input("Player 2 (Black) name: ")
    turn = 0
    while not gameOver:
        if turn % 2 == 0:
            move = input("Player 1 move: ")
        elif turn % 2 == 1:
            move = input("Player 2 move: ")


        turn += 1


