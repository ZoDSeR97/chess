from pieces.piece import Piece
from rule.chessRule import enPassant

class Pawn(Piece):
    passP = False

    def __init__(self, alliance, x, y):
        super().__init__(alliance, x, y)
        self.symbol = "P"

    def validMove(self, board):
        super().validMove(board)

        traverse = {"W": -1, "B": 1}

        x = self.x_coord + traverse[self.alliance]

        if x in range(8) and self.board[x][self.y_coord].pieceOccupy.symbol == "0":
            self.piecesMoves.append([x, self.y_coord])

        if self.y_coord+1 < 8 and self.board[x][self.y_coord+1].pieceOccupy.symbol != "0":
            if self.board[x][self.y_coord+1].pieceOccupy.alliance != self.alliance:
                self.piecesMoves.append([x, self.y_coord+1])

        if self.y_coord-1 >= 0 and self.board[x][self.y_coord-1].pieceOccupy.symbol != "0":
            if self.board[x][self.y_coord+1].pieceOccupy.alliance != self.alliance:
                self.piecesMoves.append([x, self.y_coord-1])

        if self.fMove is True and self.board[x+traverse[self.alliance]][self.y_coord].pieceOccupy.symbol == "0":
            self.piecesMoves.append([x+traverse[self.alliance], self.y_coord])

        enP = enPassant(self.board, self.piecesMoves, self)
        enP.Check()
        
        return self.piecesMoves