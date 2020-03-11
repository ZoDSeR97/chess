class Rule:
    board = None
    moveList = []
    piece = None
    removeList = set()
    def __init__(self, board, piecesMoves, piece):
        self.board = board
        self.moveList = set(piecesMoves)
        self.piece = piece
    
    def Check(self):
        self.removeList.clear()

class enPassant(Rule):
    # Precondition for the attack square to be added
    #   first condition pawn need to be at a specific row that depend on the alliance
    #   second condition the opponent pawn move 2 square on their first move and endup right next to opponent pawn
    #
    # Postcondition for removing the attack square that was added
    #   when player did not take oppotunity

    def __init__(self, board, moveList, piece):
        super().__init__(board, moveList, piece)

    def checkPawn(self):
        dict = {"W": 3, "B": 4}
        incre = {"W": -1, "B": 1}
        alliance = self.piece.alliance
        add = self.moveList.add
        y = self.piece.y_coord
        if y > 0:
            pieceLeft = self.board[dict[alliance]][y-1].pieceOccupy
            attLeft = self.board[dict[alliance] + incre[alliance]][y-1].pieceOccupy
        if y < 7:
            pieceRight = self.board[dict[alliance]][y+1].pieceOccupy
            attRight = self.board[dict[alliance] + incre[alliance]][y+1].pieceOccupy
        
        if self.piece.x_coord == dict[alliance]:
            #look on the left side
            if y > 0 and pieceLeft.symbol == "P" and pieceLeft.alliance != alliance:
                if pieceLeft.passP is True and attLeft.symbol == "0":
                        add((dict[alliance] + incre[alliance], y-1))
            #look on the right side                
            elif y < 7 and pieceRight.symbol == "P" and pieceRight.alliance != alliance:
                if pieceRight.passP is True and attRight.symbol == "0":
                    add((dict[alliance] + incre[alliance], y+1))

class checkKing(Rule):
    def __init__(self, board, piece):
        super().__init__(board, piece)
        self.Check(piece, board)

    def Check(self, piece, board):
        pa = {"W": [[-1, 1], [-1, -1]], "B": [[1, 1], [1, -1]]}
        dict = {
            "Q": [[1, 1], [1, -1], [-1, 1], [-1, -1], [1, 0], [-1, 0], [0, 1], [0, -1]],
            "N": [[2, 1], [2, -1], [1, 2], [-1, 2], [-2, 1], [-2, -1], [1, -2], [-1, -2]],
            "R": [[1, 0],[-1, 0], [0, 1], [0, -1]],
            "B": [[1, 1], [1, -1], [-1, 1], [-1, -1]],
        }
        x = piece.x_coord
        y = piece.y_coord
        alliance = piece.alliance
        symbol = piece.symbol
        if symbol != "P":
            traverse = dict[symbol]
        else:
            traverse = pa[alliance]
        add = self.moveList.add
        clear = self.moveList.clear
        s = set(range(8))

        i = traverse.pop()
        while True:
            x += i[0]
            y += i[1]
            if x not in s or y not in s or board[x][y].pieceOccupy.alliance == alliance:
                #move that lead to another ally need to be remove
                clear()
                pass
            elif board[x][y].pieceOccupy.symbol == "0":
                if symbol != "K" and symbol != "N":
                    #reserve moves that lead to someWhere
                    append((x, y))
                    continue
            elif board[x][y].pieceOccupy.alliance != alliance and board[x][y].pieceOccupy.symbol == "K":
                add((x, y))
                break
            if traverse != list():
                x = piece.x_coord
                y = piece.y_coord
                i = traverse.pop()
            else:
                break
        return self.moveList