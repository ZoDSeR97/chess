class Rule:
    board = None
    moveList = []
    piece = None
    def __init__(self, board, piecesMoves, piece):
        self.board = board
        self.moveList = piecesMoves
        self.piece = piece

class checkPieces(Rule):
    def __init__(self, board, moveList, piece):
        super().__init__(board, moveList, piece)

    def Check(self):
        for i in self.moveList:
            if self.board[i[0]][i[1]].pieceOccupy.toString() != "0":
                if self.board[i[0]][i[1]].pieceOccupy.alliance == self.piece.alliance:
                    self.moveList.remove([i[0], i[1]])
                if self.piece.toString() != "N" or self.piece.toString() != "K":
                    for j in self.moveList:
                        if j[1] < i[1] < self.piece.y_coord or j[1] > i[1] > self.piece.y_coord:
                            self.moveList.remove(j)
                        elif (j[0] < i[0] < self.piece.x_coord or j[0] > i[0] > self.piece.x_coord) and j[1] == i[1] == self.piece.y_coord:
                            self.moveList.remove(j)
                if self.piece.toString() == "P":
                    if self.piece.alliance == "W" and i[0] < self.piece.x_coord and i[1] == self.piece.y_coord:
                        self.moveList.remove(i)
                    elif self.piece.alliance == "B" and i[0] > self.piece.x_coord and i[1] == self.piece.y_coord:
                        self.moveList.remove(i)
        return self.moveList

class enPassant(Rule):

    def __init__(self, board, moveList, piece):
        super().__init__(board, moveList, piece)

    def Check(self):
        if self.piece.alliance == "W" and self.piece.x_coord == 3:

            if self.board[self.piece.x_coord][self.piece.y_coord-1].pieceOccupy.toString() == "P":
                if self.board[self.piece.x_coord][self.piece.y_coord-1].pieceOccupy.passP is True:
                    if self.board[self.piece.x_coord][self.piece.y_coord-1].pieceOccupy.alliance == "B":
                        if self.board[self.piece.x_coord-1][self.piece.y_coord-1].pieceOccupy.toString() == "0":
                            self.moveList.append([self.piece.x_coord-1, self.piece.y_coord-1])
                            
            if self.board[self.piece.x_coord][self.piece.y_coord+1].pieceOccupy.toString() == "P":
                if self.board[self.piece.x_coord][self.piece.y_coord+1].pieceOccupy.passP is True:
                    if self.board[self.piece.x_coord][self.piece.y_coord+1].pieceOccupy.alliance == "B":
                        if self.board[self.piece.x_coord-1][self.piece.y_coord+1].pieceOccupy.toString() == "0":
                            self.moveList.append([self.piece.x_coord-1, self.piece.y_coord+1])
                            
        if self.piece.alliance == "B" and self.piece.x_coord == 4:

            if self.board[self.piece.x_coord][self.piece.y_coord-1].pieceOccupy.toString() == "P":
                if self.board[self.piece.x_coord][self.piece.y_coord-1].pieceOccupy.passP is True:
                    if self.board[self.piece.x_coord][self.piece.y_coord-1].pieceOccupy.alliance == "W":
                        if self.board[self.piece.x_coord+1][self.piece.y_coord-1].pieceOccupy.toString() == "0":
                            self.moveList.append([self.piece.x_coord+1, self.piece.y_coord-1])

            if self.board[self.piece.x_coord][self.piece.y_coord+1].pieceOccupy.toString() == "P":
                if self.board[self.piece.x_coord][self.piece.y_coord+1].pieceOccupy.passP is True:
                    if self.board[self.piece.x_coord][self.piece.y_coord+1].pieceOccupy.alliance == "W":
                        if self.board[self.piece.x_coord+1][self.piece.y_coord+1].pieceOccupy.toString() == "0":
                            self.moveList.append([self.piece.x_coord+1, self.piece.y_coord+1])