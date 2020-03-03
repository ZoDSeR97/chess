from rule.chessRule import checkPieces 

class Piece:
    alliance = None
    x_coord = None
    y_coord = None
    board = None
    piecesMoves = []
    fMove = True

    def __init__(self, alliance, x, y):
        self.alliance = alliance
        self.x_coord = x
        self.y_coord = y

    def toString(self):
        return "0"

    def validMove(self, board):
        self.board = board

class King(Piece):
    def __init__(self, alliance, x, y):
        super().__init__(alliance, x, y)

    def toString(self):
        return "K"

    def validMove(self, board):
        super().validMove(board)
        return self.piecesMoves

class Queen(Piece):
    def __init__(self, alliance, x, y):
        super().__init__(alliance, x, y)

    def toString(self):
        return "Q"

    def validMove(self, board):
        super().validMove(board)
        return self.piecesMoves

class Rook(Piece):
    def __init__(self, alliance, x, y):
        super().__init__(alliance, x, y)
    
    def toString(self):
        return "R"

    def validMove(self, board):
        super().validMove(board)
        return self.piecesMoves

class Bishop(Piece):
    def __init__(self, alliance, x, y):
        super().__init__(alliance, x, y)

    def toString(self):
        return "B"

    def validMove(self, board):
        super().validMove(board)

        return self.piecesMoves

class Knight(Piece):
    def __init__(self, alliance, x, y):
        super().__init__(alliance, x, y)

    def toString(self):
        return "N"

    def validMove(self, board):
        super().validMove(board)
        return self.piecesMoves

class Pawn(Piece):

    def __init__(self, alliance, x, y):
        super().__init__(alliance, x, y)
    
    def toString(self):
        return "P"

    def validMove(self, board):
        super().validMove(board)
        if self.alliance == "W":
            self.piecesMoves.append([self.x_coord-1, self.y_coord])
            if self.fMove is True:
                self.piecesMoves.append([self.x_coord-2, self.y_coord])
            if self.y_coord+1 <= 7 and self.board[self.x_coord-1][self.y_coord+1].pieceOccupy.toString() != "0":
                self.piecesMoves.append([self.x_coord-1, self.y_coord+1])
            if self.y_coord-1 >= 0 and self.board[self.x_coord-1][self.y_coord-1].pieceOccupy.toString() != "0":
                self.piecesMoves.append([self.x_coord-1, self.y_coord-1])
        else:
            self.piecesMoves.append([self.x_coord+1, self.y_coord])
            if self.fMove is True:
                self.piecesMoves.append([self.x_coord+2, self.y_coord])
            if self.y_coord+1 <= 7 and self.board[self.x_coord+1][self.y_coord+1].pieceOccupy.toString() != "0":
                self.piecesMoves.append([self.x_coord+1, self.y_coord+1])
            if self.y_coord-1 >= 0 and self.board[self.x_coord+1][self.y_coord-1].pieceOccupy.toString() != "0":
                self.piecesMoves.append([self.x_coord+1, self.y_coord-1])
        check = checkPieces(board, self.piecesMoves, self)
        check.Check()
        return check.moveList

class nullPiece(Piece):

    def __init__(self):
        pass

    def toString(self):
        return "0"
    
    def validMove(self, board):
        return []