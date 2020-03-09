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
        if self.piece.alliance == "W" and self.piece.x_coord == 3:

            if self.board[self.piece.x_coord][self.piece.y_coord-1].pieceOccupy.symbol == "P":
                if self.board[self.piece.x_coord][self.piece.y_coord-1].pieceOccupy.passP is True:
                    if self.board[self.piece.x_coord][self.piece.y_coord-1].pieceOccupy.alliance == "B":
                        if self.board[self.piece.x_coord-1][self.piece.y_coord-1].pieceOccupy.symbol == "0":
                            self.moveList.append([self.piece.x_coord-1, self.piece.y_coord-1])
                            
            if self.board[self.piece.x_coord][self.piece.y_coord+1].pieceOccupy.symbol == "P":
                if self.board[self.piece.x_coord][self.piece.y_coord+1].pieceOccupy.passP is True:
                    if self.board[self.piece.x_coord][self.piece.y_coord+1].pieceOccupy.alliance == "B":
                        if self.board[self.piece.x_coord-1][self.piece.y_coord+1].pieceOccupy.symbol == "0":
                            self.moveList.append([self.piece.x_coord-1, self.piece.y_coord+1])
                            
        if self.piece.alliance == "B" and self.piece.x_coord == 4:

            if self.board[self.piece.x_coord][self.piece.y_coord-1].pieceOccupy.symbol == "P":
                if self.board[self.piece.x_coord][self.piece.y_coord-1].pieceOccupy.passP is True:
                    if self.board[self.piece.x_coord][self.piece.y_coord-1].pieceOccupy.alliance == "W":
                        if self.board[self.piece.x_coord+1][self.piece.y_coord-1].pieceOccupy.symbol == "0":
                            self.moveList.append([self.piece.x_coord+1, self.piece.y_coord-1])

            if self.board[self.piece.x_coord][self.piece.y_coord+1].pieceOccupy.symbol == "P":
                if self.board[self.piece.x_coord][self.piece.y_coord+1].pieceOccupy.passP is True:
                    if self.board[self.piece.x_coord][self.piece.y_coord+1].pieceOccupy.alliance == "W":
                        if self.board[self.piece.x_coord+1][self.piece.y_coord+1].pieceOccupy.symbol == "0":
                            self.moveList.append([self.piece.x_coord+1, self.piece.y_coord+1])