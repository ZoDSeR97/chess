from pieces.piece import Piece
from rule.chessRule import enPassant

class Pawn(Piece):
    passP = False

    def __init__(self, alliance, x, y):
        super().__init__(alliance, x, y)
        self.symbol = "P"

    def validMove(self, board):
        super().validMove(board)
        s = set(range(8))
        alliance = self.alliance
        append = self.piecesMoves.append

        #Generalize alliance by using dict
        traverse = {"W": -1, "B": 1}

        x = self.x_coord + traverse[alliance]

        if x in s and board[x][self.y_coord].pieceOccupy.symbol == "0":
            append((x, self.y_coord))

        if self.y_coord+1 < 8 and board[x][self.y_coord+1].pieceOccupy.symbol != "0":
            if board[x][self.y_coord+1].pieceOccupy.alliance != alliance:
                append((x, self.y_coord+1))

        if self.y_coord-1 >= 0 and board[x][self.y_coord-1].pieceOccupy.symbol != "0":
            if board[x][self.y_coord+1].pieceOccupy.alliance != alliance:
                append((x, self.y_coord-1))

        if self.fMove is True and board[x+traverse[self.alliance]][self.y_coord].pieceOccupy.symbol == "0":
            append((x+traverse[self.alliance], self.y_coord))

        enP = enPassant(board, self.piecesMoves, self)
        enP.checkPawn()
        
        return self.piecesMoves