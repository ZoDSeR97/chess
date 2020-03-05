class Rule:
    board = None
    moveList = []
    piece = None
    removeList = []
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
                    self.removeList.append(i)
                elif self.piece.toString() == "P":
                    if self.piece.alliance == "W" and i[0] < self.piece.x_coord and i[1] == self.piece.y_coord:
                        self.removeList.append(i)
                    elif self.piece.alliance == "B" and i[0] > self.piece.x_coord and i[1] == self.piece.y_coord:
                        self.removeList.append(i)
                if self.piece.toString() != "N" and self.piece.toString() != "K" or len(self.removeList) == len(self.moveList):
                    for j in self.moveList:
                        if j in self.removeList:
                            continue
                        if j[0] == i[0] == self.piece.x_coord:
                            if i[1] < self.piece.y_coord and j[1] > i[1]:
                                self.removeList.append(j)
                            if i[1] > self.piece.y_coord and j[1] < i[1]:
                                self.removeList.append(j)
                        elif j[1] == i[1] == self.piece.y_coord:
                            if i[0] < self.piece.y_coord and j[0] > i[0]:
                                self.removeList.append(j)
                            if i[0] > self.piece.y_coord and j[0] < i[0]:
                                self.removeList.append(j)
                        elif j[0] > i[0] and j[1] != self.piece.y_coord:
                            self.removeList.append(j)
                        elif j[0] < i[0] and j[1] != self.piece.y_coord:
                            self.removeList.append(j)
        self.moveList = [i for i in self.moveList if i not in self.removeList]
        self.removeList.clear()

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