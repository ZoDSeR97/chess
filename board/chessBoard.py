from pieces.nullPiece import nullPiece
from pieces.Pawn import Pawn
from pieces.King import King
from pieces.Knight import Knight
from pieces.Queen import Queen
from pieces.Bishop import Bishop
from pieces.Rook import Rook

class Tile:
    pieceOccupy = None
    score = None

    def __init__(self, piece):
        self.pieceOccupy = piece
        self.updateScore()

    def updateScore(self):
        piece = self.pieceOccupy
        if piece.symbol != "0":
            self.score = piece.value*((piece.x_coord)/7+(piece.y_coord))
        else:
            self.score = 0

class Board:
    #Using list comprehension to populate board
    board = [[Tile(nullPiece()) for i in range(8)] for j in range(8)]

    def __init__(self):
        self.createBoard(self.board)

    def createBoard(self, board):
        #populate Pawn
        for cols in range(8):
            board[1][cols] = Tile(Pawn("B", 1, cols))
            board[6][cols] = Tile(Pawn("W", 6, cols))

        #populate King
        board[0][4] = Tile(King("B", 0, 4))
        board[7][4] = Tile(King("W", 7, 4))

        #populate Queen
        board[0][3] = Tile(Queen("B", 0, 3))
        board[7][3] = Tile(Queen("W", 7, 3))

        #populate Rook
        board[0][0] = Tile(Rook("B", 0, 0))
        board[0][7] = Tile(Rook("B", 0, 7))

        board[7][0] = Tile(Rook("W", 7, 0))
        board[7][7] = Tile(Rook("W", 7, 7))

        #populate Bishop
        board[0][2] = Tile(Bishop("B", 0, 2))
        board[0][5] = Tile(Bishop("B", 0, 5))

        board[7][2] = Tile(Bishop("W", 7, 2))
        board[7][5] = Tile(Bishop("W", 7, 5))

        #populate Knight
        self.board[0][1] = Tile(Knight("B", 0, 1))
        self.board[0][6] = Tile(Knight("B", 0, 6))

        self.board[7][1] = Tile(Knight("W", 7, 1))
        self.board[7][6] = Tile(Knight("W", 7, 6))
    
    def printBoard(self):
        count = 0
        for rows in range(8):
            for cols in range(8):
                print('|', end=self.board[rows][cols].pieceOccupy.symbol)
                count += 1
                if count == 8:
                    print('|', end='\n')
                    count = 0
    
    def updateBoard(self, x, y, piece):
        self.board[x][y] = Tile(piece)

    def promotePawn(self, x, y, alliance, symbol):
        dict = {"Q": Queen(alliance, x, y), 
                "B": Bishop(alliance, x, y), 
                "R": Rook(alliance, x, y), 
                "N": Knight(alliance, x, y)}
        self.board[x][y] = Tile(dict[symbol])