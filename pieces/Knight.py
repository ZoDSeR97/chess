from pieces.piece import Piece

class Knight(Piece):
    def __init__(self, alliance, x, y):
        super().__init__(alliance, x, y)
        self.symbol = "N"
        self.traverse = [[2, 1], [2, -1], [1, 2], [-1, 2], [-2, 1], [-2, -1], [1, -2], [-1, -2]]

    def validMove(self, board):
        super().validMove(board)

        return self.piecesMoves