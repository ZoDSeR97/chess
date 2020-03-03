from pieces.piece import Piece
from rule.chessRule import checkPieces

class King(Piece):
    def __init__(self, alliance, x, y):
        super().__init__(alliance, x, y)

    def toString(self):
        return "K"

    def validMove(self, board):
        super().validMove(board)
        return self.piecesMoves