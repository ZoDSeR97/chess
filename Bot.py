import random
from pieces.nullPiece import nullPiece

class Bot:
    chessBoard = None
    pieces = list()
    pieceMove = None
    def __init__(self, board, pieces):
        self.chessBoard = board
        self.pieces = pieces

    def Move(self, selectedPiece, x, y):
        chessBoard = self.chessBoard
        chessBoard = self.chessBoard
        x_origin = selectedPiece.x_coord
        y_origin = selectedPiece.y_coord
        moves = 0

        if chessBoard.board[x][y].pieceOccupy.symbol != "0":
            moves = 0
        else:
            moves = 1

        if selectedPiece.symbol == "P":
            moves = 0

            if selectedPiece.x_coord +2 == x or selectedPiece.x_coord -2 == x:
                selectedPiece.passP = True

            if selectedPiece.alliance == "B" and y != y_origin:
                if chessBoard.board[x-1][y].pieceOccupy.symbol == "P":
                    if chessBoard.board[x-1][y].pieceOccupy.passP == True:
                        chessBoard.updateBoard(x-1, y, nullPiece())

            if selectedPiece.alliance == "W" and y != y_origin:
                if chessBoard.board[x+1][y].pieceOccupy.symbol == "P":
                    if chessBoard.board[x+1][y].pieceOccupy.passP == True:
                        chessBoard.updateBoard(x+1, y, nullPiece())

        selectedPiece.x_coord = x
        selectedPiece.y_coord = y
        selectedPiece.fMove = False
        chessBoard.updateBoard(x, y, selectedPiece)
        chessBoard.updateBoard(x_origin, y_origin, nullPiece())

        return moves

class randomBot(Bot):
    def __init__(self, board, pieces):
        super().__init__(board, pieces)
    
    def randomMoves(self):
        pieces = self.pieces
        chessBoard = self.chessBoard
        chosenMove = None
        removeList = set()
        pieceMove = set()
        count = 0
        moves = 0
        while pieces:
            chosenPiece = random.choice(pieces)
            rows = chosenPiece[0]
            cols = chosenPiece[1]
            selectedPiece = chessBoard.board[rows][cols].pieceOccupy
            pieceMove = selectedPiece.validMove(chessBoard.board)
            if pieceMove == list():
                removeList.add((rows, cols))
                count += 1
                if count == 3:
                    pieces = [i for i in pieces if i not in removeList]
                    count = 0
                    removeList.clear()
                    if pieces == set():
                        break
                selectedPiece = None
                continue
            else:
                chosenMove = random.choice(pieceMove)
                print("Bot selected", selectedPiece, "at coordination: [", selectedPiece.x_coord, ", ", selectedPiece.y_coord, "]")
                moves = super().Move(selectedPiece, chosenMove[0], chosenMove[1])
                break
        return selectedPiece, moves

class complexBot(Bot):
    def __init__(self, board, pieces):
        super().__init__(board, pieces)