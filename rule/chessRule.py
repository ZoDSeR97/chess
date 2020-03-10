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
        x = self.piece.x_coord
        y = self.piece.y_coord

        pieceLeft = self.board[dict[alliance]][y-1].pieceOccupy
        attLeft = self.board[dict[alliance] + incre[alliance]][y-1].pieceOccupy

        pieceRight = self.board[dict[alliance]][y+1].pieceOccupy
        attRight = self.board[dict[alliance] + incre[alliance]][y+1].pieceOccupy
        
        if x == dict[alliance]:
            #look on the left side
            if pieceLeft.symbol == "P" and pieceLeft.alliance != alliance:
                if pieceLeft.passP is True and attLeft.symbol == "0":
                        append((x + incre[alliance], y-1))
            #look on the right side                
            if pieceRight.symbol == "P" and pieceRight.alliance != alliance:
                if pieceRight.passP is True and attRight.symbol == "0":
                    append((x + incre[alliance], y+1))