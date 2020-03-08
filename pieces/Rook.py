from pieces.piece import Piece

class Rook(Piece):
    def __init__(self, alliance, x, y):
        super().__init__(alliance, x, y)
        self.symbol = "R"
        self.traverse = [[1, 0],[-1, 0], [0, 1], [0, -1]]
    
    def validMove(self, board):
        super().validMove(board)
        
        return self.piecesMoves