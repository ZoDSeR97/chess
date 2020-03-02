from pieces.piece import Piece
from rule.basicRule import checkPieces

class Bishop(Piece):
    def __init__(self, alliance, x, y):
        super().__init__(alliance, x, y)

    def toString(self):
        return "B"

    def validMove(self, board):
        super().validMove(board)

        return self.piecesMoves