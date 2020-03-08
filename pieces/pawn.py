from pieces.piece import Piece
from rule.chessRule import checkPieces
from rule.chessRule import enPassant

class Pawn(Piece):
    passP = False

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
        enP = enPassant(board, check.moveList, self)
        enP.Check()
        return check.moveList