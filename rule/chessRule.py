class Rule:
    board = None
    moveList = []
    piece = None
    removeList = []
    def __init__(self, board, piecesMoves, piece):
        self.board = board
        self.moveList = piecesMoves
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
        append = self.moveList.append
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
                        append((dict[alliance] + incre[alliance], y-1))
            #look on the right side                
            if y < 7 and pieceRight.symbol == "P" and pieceRight.alliance != alliance:
                if pieceRight.passP is True and attRight.symbol == "0":
                    append((dict[alliance] + incre[alliance], y+1))

class inCheck(Rule):
    def __init__(self, board, moveList, piece):
        super().__init__(board, moveList, piece)

    def Checking(self):
        pa = {"W": [[-1, 1], [-1, -1]], "B": [[1, 1], [1, -1]]}
        dict = {
            "Q": [[1, 1], [1, -1], [-1, 1], [-1, -1], [1, 0], [-1, 0], [0, 1], [0, -1]],
            "N": [[2, 1], [2, -1], [1, 2], [-1, 2], [-2, 1], [-2, -1], [1, -2], [-1, -2]],
            "R": [[1, 0], [-1, 0], [0, 1], [0, -1]],
            "B": [[1, 1], [1, -1], [-1, 1], [-1, -1]],
        }
        piece = self.piece
        board = self.board
        x = piece.x_coord
        y = piece.y_coord
        alliance = piece.alliance
        symbol = piece.symbol
        if symbol != "P":
            traverse = dict[symbol]
        else:
            traverse = pa[alliance]
        moveList = set()
        add = moveList.add
        clear = moveList.clear
        s = set(range(8))

        i = traverse.pop()
        while True:
            x += i[0]
            y += i[1]
            if x not in s or y not in s or board[x][y].pieceOccupy.alliance == alliance:
                pass
            elif board[x][y].pieceOccupy.symbol == "0":
                if symbol != "K" and symbol != "N" and symbol != "P":
                    add((x, y))
                    continue
            elif board[x][y].pieceOccupy.alliance != alliance and board[x][y].pieceOccupy.symbol == "K":
                add((x, y))
                break
            if traverse != list():
                x = piece.x_coord
                y = piece.y_coord
                i = traverse.pop()
                clear()
            else:
                break
        return moveList

class Stale(Rule):
    pieces = []
    pastBoard = []
    repetition = 0
    opPieces = []
    allPieces = []
    alliance = "W"
    def __init__(self, board, wPieces, bPieces, allPieces):
        self.board = board
        self.pieces = wPieces
        self.opPieces = bPieces
        self.allPieces = allPieces
        self.updatePast()
    
    def updatePast(self):
        self.pastBoard.clear()
        for i in self.allPieces:
            self.pastBoard.append(i)
    
    def repetitionCheck(self):
        if set(self.pastBoard) == set(self.allPieces):
            self.repetition += 1
            print("Repetition", self.repetition)
            if self.repetition == 3:
                print("Desperate Stale")
                return True
        else:
            print("repetition False")
            self.repetition = 0
            self.updatePast()
            return self.staleCase1()
    
    def staleCase1(self):
        K1 = False
        K2 = False
        QP = False
        N = False
        bishop1Color = None
        bishop2Color = None
        if len(self.pieces) == 1 and len(self.opPieces) == 1:
            rows = (int)(self.pieces[0][0]/75)
            cols = (int)(self.pieces[1][1]/75)
            if self.board[rows][cols].pieceOccupy.toString() == "K":
                rows = (int)(self.pieces[0][0]/75)
                cols = (int)(self.pieces[1][1]/75)
                if self.board[rows][cols].pieceOccupy.toString() == "K":
                    print("Two King Dance Stale")
                    return True

        elif len(self.pieces) < 3 and len(self.opPieces) < 3:
            for i in self.pieces:
                rows = (int)(i[0][0]/75)
                cols = (int)(i[0][1]/75)
                if self.board[rows][cols].pieceOccupy.toString() == "K":
                    K1 = True
                elif self.board[rows][cols].pieceOccupy.toString() == "N":
                    N = True
                elif self.board[rows][cols].pieceOccupy.toString() == "B":
                    if (rows+cols)%2 == 0:
                        bishop1Color = "W"
                    else: 
                        bishop1Color = "B"
                else:
                    QP = True
                    break

            if K1 and (not QP or bishop1Color is None or not N):
                for j in self.opPieces:
                    rows = (int)(j[0][0]/75)
                    cols = (int)(j[0][1]/75)
                    if self.board[rows][cols].pieceOccupy.toString() == "K":
                        K1 = True
                    elif self.board[rows][cols].pieceOccupy.toString() == "N":
                        N = True
                    elif self.board[rows][cols].pieceOccupy.toString() == "B":
                        if (rows+cols)%2 == 0:
                            bishop2Color = "W"
                        else: 
                            bishop2Color = "B"
                    else:
                        QP = True
                        break
        
        if K1 and K2 and QP:
            print("Stale by case")
            return True
        elif K1 and K2 and (bishop1Color is not None or bishop2Color is not None or N):
            if bishop1Color is not None and bishop2Color is not None and bishop1Color == bishop2Color:
                print("Stale by case: same bishop")
                return True
            elif bishop1Color is None and bishop2Color is None and N:
                print("Stale by case: 1v2")
                return True
            elif (bishop1Color is None or bishop2Color is None) and not N:
                print("Stale by case: 1v2")
                return True
        else:
            return self.staleCase2()

    #tempory not working as intended supposely one condition need to fullfill
    def staleCase2(self):
        dict = {"W": self.pieces, "B": self.opPieces}
        count = 0
        for i in dict[self.alliance]:
            rows = (int)(i[0][0]/75)
            cols = (int)(i[0][1]/75)
            if not self.board[rows][cols].pieceOccupy.validMove:
                count += 1
            elif count == len(self.pieces):
                return True
            else:
                return False