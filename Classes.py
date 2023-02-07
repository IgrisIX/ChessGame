WHITE = "white"
BLACK = "black"

class ChessPieces:
    def __init__(self, name, x, y, color, board, icon):
        self.name = name
        self.x = x
        self.y = y
        self.color = color
        self.board = board
        self.icon = icon

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

    def update_position(self, x, y):
        self.board.grid[self.x][self.y] = None
        self.board.grid[x][y] = self
        self.x = x
        self.y = y


class Pawn(ChessPieces):
    def __init__(self, name, x, y, color, board, icon):
        super().__init__(name, x, y, color, board, icon)
        self.possibleMove = []
    
    def update_possible_move(self):
        self.possibleMove.clear()
        if self.color == "white" and self.y < 7:
            self.possibleMove.append([self.x, self.y + 1])
            if self.x > 0 and self.board.grid[self.x - 1][self.y + 1] is not None:
                self.possibleMove.append([self.x - 1, self.y + 1])
            if self.x < 7 and self.board.grid[self.x + 1][self.y + 1] is not None:
                self.possibleMove.append([self.x + 1, self.y + 1])
        elif self.color == "black" and self.y > 0:
            self.possibleMove.append([self.x, self.y - 1])
            if self.x > 0 and self.board.grid[self.x - 1][self.y - 1] is not None:
                self.possibleMove.append([self.x - 1, self.y - 1])
            if self.x < 7 and self.board.grid[self.x + 1][self.y - 1] is not None:
                self.possibleMove.append([self.x + 1, self.y - 1])
        else:
            raise Exception("Something wrong and not considered in Pawn update_position")



class Bishop(ChessPieces):
    def __init__(self, name, x, y, color, board, icon):
        super().__init__(name, x, y, color, board, icon)
        self.possibleMove = []

    def update_possible_move(self):
        self.possibleMove.clear()
        for direction in [[1, 1], [-1, 1], [1, -1], [-1, -1]]:
            for i in range(1, 8):
                targetX = self.x + (i * direction[0])
                targetY = self.y + (i * direction[1])
                if self.check_destination(targetX, targetY) == "empty" or \
                        self.check_destination(targetX, targetY) == "enemy":
                    self.possibleMove.append([targetX, targetY])
                else:
                    break


class Knight(ChessPieces):
    def __init__(self, name, x, y, color, board, icon):
        super().__init__(name, x, y, color, board, icon)
        self.possibleMove = []

    def update_possible_move(self):
        self.possibleMove.clear()
        for direction in [[1, 2], [1, -2], [-1, 2], [-1, -2], [2, 1], [-2, 1], [2, -1], [-2, -1]]:
            targetX = self.x + direction[0]
            targetY = self.y + direction[1]
            if self.check_destination(targetX, targetY) == "empty" or \
                    self.check_destination(targetX, targetY) == "enemy":
                self.possibleMove.append([targetX, targetY])
            else:
                break


class Rook(ChessPieces):
    def __init__(self, name, x, y, color, board, icon):
        super().__init__(name, x, y, color, board, icon)
        self.possibleMove = []

    def update_possible_move(self):
        self.possibleMove.clear()
        for direction in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            for i in range(1, 8):
                targetX = self.x + (i * direction[0])
                targetY = self.y + (i * direction[1])
                if self.check_destination(targetX, targetY) == "empty" or \
                        self.check_destination(targetX, targetY) == "enemy":
                    self.possibleMove.append([targetX, targetY])
                else:
                    break


class Queen(ChessPieces):
    def __init__(self, name, x, y, color, board, icon):
        super().__init__(name, x, y, color, board, icon)
        self.possibleMove = []

    def update_possible_move(self):
        self.possibleMove.clear()
        for direction in [[0, 1], [1, 0], [0, -1], [-1, 0], [1, 1], [-1, 1], [1, -1], [-1, -1]]:
            for i in range(1, 8):
                targetX = self.x + (i * direction[0])
                targetY = self.y + (i * direction[1])
                if self.check_destination(targetX, targetY) == "empty" or \
                        self.check_destination(targetX, targetY) == "enemy":
                    self.possibleMove.append([targetX, targetY])
                else:
                    break


class King(ChessPieces):
    def __init__(self, name, x, y, color, board, icon):
        super().__init__(name, x, y, color, board, icon)
        self.possibleMove = []

    def update_possible_move(self):
        self.possibleMove.clear()
        for direction in [[0, 1], [1, 0], [0, -1], [-1, 0], [1, 1], [-1, 1], [1, -1], [-1, -1]]:
            targetX = self.x + direction[0]
            targetY = self.y + direction[1]
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
        whiteTeam = [King("whiteKing", 4, 0, "white", self, "white_king"),
                          Queen("whiteQueen", 3, 0, "white", self, "white_queen"),
                          Rook("whiteRook1", 0, 0, "white", self, "white_rook"),
                          Rook("whiteRook2", 7, 0, "white", self, "white_rook"),
                          Bishop("whiteBishop1", 2, 0, "white", self, "white_bishop"),
                          Bishop("whiteBishop2", 5, 0, "white", self, "white_bishop"),
                          Knight("whiteKnight1", 1, 0, "white", self, "white_knight"),
                          Knight("whiteKnight2", 6, 0, "white", self, "white_knight"),
                          Pawn("whitePawn1", 0, 1, "white", self, "white_pawn"),
                          Pawn("whitePawn2", 1, 1, "white", self, "white_pawn"),
                          Pawn("whitePawn3", 2, 1, "white", self, "white_pawn"),
                          Pawn("whitePawn4", 3, 1, "white", self, "white_pawn"),
                          Pawn("whitePawn5", 4, 1, "white", self, "white_pawn"),
                          Pawn("whitePawn6", 5, 1, "white", self, "white_pawn"),
                          Pawn("whitePawn7", 6, 1, "white", self, "white_pawn"),
                          Pawn("whitePawn8", 7, 1, "white", self, "white_pawn")]
        blackTeam = [King("blackKing", 4, 7, "black", self, "pink_king"),
                          Queen("blackQueen", 3, 7, "black", self, "pink_queen"),
                          Rook("blackRook1", 0, 7, "black", self, "pink_rook"),
                          Rook("blackRook2", 7, 7, "black", self, "pink_rook"),
                          Bishop("blackBishop1", 2, 7, "black", self, "pink_bishop"),
                          Bishop("blackBishop2", 5, 7, "black", self, "pink_bishop"),
                          Knight("blackKnight1", 1, 7, "black", self, "pink_knight"),
                          Knight("blackKnight2", 6, 7, "black", self, "pink_knight"),
                          Pawn("blackPawn1", 0, 6, "black", self, "pink_pawn"),
                          Pawn("blackPawn1", 1, 6, "black", self, "pink_pawn"),
                          Pawn("blackPawn1", 2, 6, "black", self, "pink_pawn"),
                          Pawn("blackPawn1", 3, 6, "black", self, "pink_pawn"),
                          Pawn("blackPawn1", 4, 6, "black", self, "pink_pawn"),
                          Pawn("blackPawn1", 5, 6, "black", self, "pink_pawn"),
                          Pawn("blackPawn1", 6, 6, "black", self, "pink_pawn"),
                          Pawn("blackPawn1", 7, 6, "black", self, "pink_pawn")]
        for pieces in whiteTeam:
            self.grid[pieces.x][pieces.y] = pieces
        for pieces in blackTeam:
            self.grid[pieces.x][pieces.y] = pieces
        self.update_all_possible_move()

    def update_all_possible_move(self):
        for i in range(8):
            for j in range(8):
                if self.grid[i][j] is not None:
                    self.grid[i][j].update_possible_move()
