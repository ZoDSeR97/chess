from pieces.piece import Piece

class Bishop(Piece):
    def __init__(self, alliance, x, y):
        super().__init__(alliance, x, y)
        self.symbol = "B"
        
    def validMove(self, board):
        self.traverse = [[1, 1], [1, -1], [-1, 1], [-1, -1]]
        super().validMove(board)
        
        return self.piecesMoves