class Piece:
    alliance = None
    x_coord = None
    y_coord = None
    piecesMoves = list()
    traverse = list()
    fMove = True
    protected = False
    symbol = "0"

    def __init__(self, alliance, x, y):
        self.alliance = alliance
        self.x_coord = x
        self.y_coord = y

    def validMove(self, board):
        self.piecesMoves.clear()
        x_origin = self.x_coord
        y_origin = self.y_coord
        alliance = self.alliance
        symbol = self.symbol
        traverse = self.traverse
        append = self.piecesMoves.append
        x = x_origin
        y = y_origin
        s = set(range(8))

        if symbol != "P":
            i = traverse.pop()
            while True:
                x += i[0]
                y += i[1]
                if x not in s or y not in s or board[x][y].pieceOccupy.alliance == alliance:
                    pass
                elif board[x][y].pieceOccupy.symbol == "0":
                    append((x, y))
                    if symbol != "K" and symbol != "N":
                        continue
                elif board[x][y].pieceOccupy.alliance != alliance:
                    append((x, y))
                if traverse != list():
                    x = x_origin
                    y = y_origin
                    i = traverse.pop()
                else:
                    break