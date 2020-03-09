from pieces.piece import Piece

class Knight(Piece):
    def __init__(self, alliance, x, y):
        super().__init__(alliance, x, y)
        self.symbol = "N"

    def validMove(self, board):
        #list of increment x and y for valid move
        self.traverse = [[2, 1], [2, -1], [1, 2], [-1, 2], [-2, 1], [-2, -1], [1, -2], [-1, -2]]
        super().validMove(board)

        return self.piecesMoves