class Piece:
    alliance = None
    x_coord = None
    y_coord = None
    board = None
    piecesMoves = []
    traverse = []
    fMove = True
    protected = False
    symbol = "0"

    def __init__(self, alliance, x, y):
        self.alliance = alliance
        self.x_coord = x
        self.y_coord = y

    def validMove(self, board):
        self.board = board
        self.piecesMoves.clear()
        x = self.x_coord
        y = self.y_coord

        if self.symbol != "P":
            i = self.traverse.pop()
            while True:
                x += i[0]
                y += i[1]
                if x not in range(8) or y not in range(8) or self.board[x][y].pieceOccupy.alliance == self.alliance:
                    pass
                elif self.board[x][y].pieceOccupy.symbol == "0":
                    self.piecesMoves.append([x, y])
                    if self.symbol != "K" and self.symbol != "N":
                        continue
                elif self.board[x][y].pieceOccupy.alliance != self.alliance:
                    self.piecesMoves.append([x, y])
                if self.traverse != list():
                    x = self.x_coord
                    y = self.y_coord
                    i = self.traverse.pop()
                else:
                    break