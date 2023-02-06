WHITE = "white"
BLACK = "black"

class ChessPieces:
    def __init__(self, name, x, y, color, board):
        self.name = name
        self.x = x
        self.y = y
        self.color = color
        self.board = board

    def check_destination(self, x, y):
        if x > 7 or x < 0 or y > 7 or y < 0:
            return "out"
        elif self.board.grid[x][y] is None:
            return "empty"
        elif self.board.grid[x][y].color != self.color:
            return "enemy"
        elif self.board.grid[x][y].color == self.color:
            return "same"
        else:
            raise Exception("Something wrong and not considered in check_destination")


class Pawn(ChessPieces):
    def __init__(self, name, x, y, color, board):
        super().__init__(name, x, y, color, board)
        self.possibleMove = []

    def update_position(self, x, y):
        self.board.grid[self.x][self.y] = None
        self.board.grid[x][y] = self
        self.x = x
        self.y = y
        self.possibleMove.clear()
        if self.color == "white" and y < 7:
            self.possibleMove.append([x, y + 1])
            if x > 0 and self.board.grid[x - 1][y + 1] is not None:
                self.possibleMove.append([x - 1, y + 1])
            if x < 7 and self.board.grid[x + 1][y + 1] is not None:
                self.possibleMove.append([x + 1, y + 1])
        elif self.color == "black" and y > 0:
            self.possibleMove.append([x, y - 1])
            if x > 0 and self.board.grid[x - 1][y - 1] is not None:
                self.possibleMove.append([x - 1, y - 1])
            if x < 7 and self.board.grid[x + 1][y - 1] is not None:
                self.possibleMove.append([x + 1, y - 1])
        else:
            raise Exception("Something wrong and not considered in Pawn update_position")


class Bishop(ChessPieces):
    def __init__(self, name, x, y, color, board):
        super().__init__(name, x, y, color, board)
        self.possibleMove = []

    def update_position(self, x, y):
        self.board.grid[self.x][self.y] = None
        self.board.grid[x][y] = self
        self.x = x
        self.y = y
        self.possibleMove.clear()
        for direction in [[1, 1], [-1, 1], [1, -1], [-1, -1]]:
            for i in range(1, 8):
                targetX = x + (i * direction[0])
                targetY = y + (i * direction[1])
                if self.check_destination(targetX, targetY) == "empty" or \
                        self.check_destination(targetX, targetY) == "enemy":
                    self.possibleMove.append([targetX, targetY])
                else:
                    break


class Knight(ChessPieces):
    def __init__(self, name, x, y, color, board):
        super().__init__(name, x, y, color, board)
        self.possibleMove = []

    def update_position(self, x, y):
        self.board.grid[self.x][self.y] = None
        self.board.grid[x][y] = self
        self.x = x
        self.y = y
        self.possibleMove.clear()
        for direction in [[1, 2], [1, -2], [-1, 2], [-1, -2]]:
            targetX = x + direction[0]
            targetY = y + direction[1]
            if self.check_destination(targetX, targetY) == "empty" or \
                    self.check_destination(targetX, targetY) == "enemy":
                self.possibleMove.append([targetX, targetY])
            else:
                break
            # Opposite move for knight
            targetX = x + direction[1]
            targetY = y + direction[0]
            if self.check_destination(targetX, targetY) == "empty" or \
                    self.check_destination(targetX, targetY) == "enemy":
                self.possibleMove.append([targetX, targetY])
            else:
                break


class Rook(ChessPieces):
    def __init__(self, name, x, y, color, board):
        super().__init__(name, x, y, color, board)
        self.possibleMove = []

    def update_position(self, x, y):
        self.board.grid[self.x][self.y] = None
        self.board.grid[x][y] = self
        self.x = x
        self.y = y
        self.possibleMove.clear()
        for direction in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            for i in range(1, 8):
                targetX = x + (i * direction[0])
                targetY = y + (i * direction[1])
                if self.check_destination(targetX, targetY) == "empty" or \
                        self.check_destination(targetX, targetY) == "enemy":
                    self.possibleMove.append([targetX, targetY])
                else:
                    break


class Queen(ChessPieces):
    def __init__(self, name, x, y, color, board):
        super().__init__(name, x, y, color, board)
        self.possibleMove = []

    def update_position(self, x, y):
        self.board.grid[self.x][self.y] = None
        self.board.grid[x][y] = self
        self.x = x
        self.y = y
        self.possibleMove.clear()
        for direction in [[0, 1], [1, 0], [0, -1], [-1, 0], [1, 1], [-1, 1], [1, -1], [-1, -1]]:
            for i in range(1, 8):
                targetX = x + (i * direction[0])
                targetY = y + (i * direction[1])
                if self.check_destination(targetX, targetY) == "empty" or \
                        self.check_destination(targetX, targetY) == "enemy":
                    self.possibleMove.append([targetX, targetY])
                else:
                    break


class King(ChessPieces):
    def __init__(self, name, x, y, color, board):
        super().__init__(name, x, y, color, board)
        self.possibleMove = []

    def update_position(self, x, y):
        self.board.grid[self.x][self.y] = None
        self.board.grid[x][y] = self
        self.x = x
        self.y = y
        self.possibleMove.clear()
        for direction in [[0, 1], [1, 0], [0, -1], [-1, 0], [1, 1], [-1, 1], [1, -1], [-1, -1]]:
            targetX = x + direction[0]
            targetY = y + direction[1]
            if self.check_destination(targetX, targetY) == "empty" or \
                    self.check_destination(targetX, targetY) == "enemy":
                self.possibleMove.append([targetX, targetY])
            else:
                break


class ChessBoard:
    def __init__(self):
        self.size = 8
        self.grid = [
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None]
        ]
        whiteTeam = [King("whiteKing", 4, 0, "white", self),
                          Queen("whiteQueen", 3, 0, "white", self),
                          Rook("whiteRook1", 0, 0, "white", self),
                          Rook("whiteRook2", 7, 0, "white", self),
                          Bishop("whiteBishop1", 2, 0, "white", self),
                          Bishop("whiteBishop2", 5, 0, "white", self),
                          Knight("whiteKnight1", 1, 0, "white", self),
                          Knight("whiteKnight2", 6, 0, "white", self),
                          Pawn("whitePawn1", 0, 1, "white", self),
                          Pawn("whitePawn2", 1, 1, "white", self),
                          Pawn("whitePawn3", 2, 1, "white", self),
                          Pawn("whitePawn4", 3, 1, "white", self),
                          Pawn("whitePawn5", 4, 1, "white", self),
                          Pawn("whitePawn6", 5, 1, "white", self),
                          Pawn("whitePawn7", 6, 1, "white", self),
                          Pawn("whitePawn8", 7, 1, "white", self)]
        blackTeam = [King("blackKing", 4, 7, "black", self),
                          Queen("blackQueen", 3, 7, "black", self),
                          Rook("blackRook1", 0, 7, "black", self),
                          Rook("blackRook2", 7, 7, "black", self),
                          Bishop("blackBishop1", 2, 7, "black", self),
                          Bishop("blackBishop2", 5, 7, "black", self),
                          Knight("blackKnight1", 1, 7, "black", self),
                          Knight("blackKnight2", 6, 7, "black", self),
                          Pawn("blackPawn1", 0, 6, "black", self),
                          Pawn("blackPawn1", 1, 6, "black", self),
                          Pawn("blackPawn1", 2, 6, "black", self),
                          Pawn("blackPawn1", 3, 6, "black", self),
                          Pawn("blackPawn1", 4, 6, "black", self),
                          Pawn("blackPawn1", 5, 6, "black", self),
                          Pawn("blackPawn1", 6, 6, "black", self),
                          Pawn("blackPawn1", 7, 6, "black", self)]
        for pieces in whiteTeam:
            self.grid[pieces.x][pieces.y] = pieces
        for pieces in blackTeam:
            self.grid[pieces.x][pieces.y] = pieces
        for i in range(8):
            for j in range(8):
                if self.grid[i][j] is not None:
                    self.grid[i][j].update_position(i, j)
