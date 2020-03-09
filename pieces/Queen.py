from pieces.piece import Piece

class Queen(Piece):
    def __init__(self, alliance, x, y):
        super().__init__(alliance, x, y)
        self.symbol = "Q"

    def validMove(self, board):
        self.traverse = [[1, 1], [1, -1], [-1, 1], [-1, -1], [1, 0], [-1, 0], [0, 1], [0, -1]]
        super().validMove(board)

        return self.piecesMoves