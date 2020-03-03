from pieces.piece import Piece

class nullPiece(Piece):
    alliance = None
    x_coord = None
    y_coord = None

    def __init__(self):
        pass

    def toString(self):
        return "0"