from pieces.piece import Piece
from rule.basicRule import checkPieces

class Rook(Piece):
    def __init__(self, alliance, x, y):
        super().__init__(alliance, x, y)
    
    def toString(self):
        return "R"

    def validMove(self, board):
        super().validMove(board)
        return self.piecesMoves