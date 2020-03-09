from pieces.piece import Piece

class King(Piece):
    def __init__(self, alliance, x, y):
        super().__init__(alliance, x, y)
        self.symbol = "K"

    def validMove(self, board):
        #list of increment x and y for valid move
        self.traverse = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]
        super().validMove(board)

        return self.piecesMoves