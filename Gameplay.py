from Classes import *

class Game:
    def __init__(self):
        self.turn = WHITE
        self.choose = False
        self.chosenPiece = None
        self.chessBoard = ChessBoard()
        self.gameOver = False

    def choose_move(self, x, y):
        if self.choose is False:
            if self.chessBoard.grid[x][y] is not None and self.chessBoard.grid[x][y].color == self.turn:
                self.choose = True
                self.chosenPiece = self.chessBoard.grid[x][y]
        elif self.choose is True:
            if [x, y] in self.chosenPiece.possibleMove:
                if isinstance(self.chessBoard.grid[x][y], King):
                    self.gameOver = True
                self.chessBoard.grid[self.chosenPiece.x][self.chosenPiece.y].update_position(x, y)
                self.choose = False
                self.chosenPiece = None
                self.chessBoard.update_all_possible_move()
                if self.turn == WHITE: 
                    self.turn = BLACK
                else:
                    self.turn = WHITE
            else:
                self.choose = False
                self.chosenPiece = None

        else: 
            raise Exception("something not considered in choose")

    def restart(self):
        self.turn = WHITE
        self.choose = False
        self.chosenPiece = None
        self.chessBoard = ChessBoard()
        self.gameOver = False