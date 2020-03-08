from pieces.piece import Piece

class Rook(Piece):
    def __init__(self, alliance, x, y):
        super().__init__(alliance, x, y)
        self.symbol = "R"
    
    def validMove(self, board):
        self.traverse =[[1, 0],[-1, 0], [0, 1], [0, -1]]

        super().validMove(board)
        
        return self.piecesMoves