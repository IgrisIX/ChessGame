from Classes import *

class Game:
    def __init__(self):
        self.turn = WHITE
        self.choose = False
        self.chosenPiece = None
        self.chessBoard = ChessBoard()

    def choose(self, x, y):
        if self.choose is False:
            if self.chessBoard.grid[x][y] is not None and self.chessBoard.grid[x][y].color == self.turn:
                self.choose = True
                self.chosenPiece = self.chessBoard.grid[x][y]
            else: 
                pass
        elif self.choose is True:
            if [x, y] in self.chosenPiece.possibleMove:
                self.chessBoard.chosenPiece.update_position(x, y)
                self.choose = False
                self.chosenPiece = None
                if self.turn == WHITE: 
                    self.turn = BLACK
                else:
                    self.turn = WHITE
            else:
                self.choose = False
                self.chosenPiece = None

        else: 
            raise Exception("something not considered in choose")