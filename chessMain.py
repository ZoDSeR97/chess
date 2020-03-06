from board.chessBoard import Board
from pieces.nullPiece import nullPiece
import pygame, os, sys, time

pygame.init()

black, white = (222, 184, 135), (255, 255, 255)

ui_width, ui_height = 600, 600

selectedPiece = None

screen = pygame.display.set_mode((ui_width, ui_height))
screen = pygame.display.get_surface()
#screen.blit(pygame.transform.flip(screen, False, True), dest=(0, 0))

pygame.display.set_caption("ChessA")

clock = pygame.time.Clock()

allTiles = []
allPieces = []
currentPieces = []
wPieces= []
bPieces= []

pieceMove = []
currentAlliance = "W"

chessBoard = Board()
chessBoard.createBoard()

flip = False

x_origin = None
y_origin = None

def switchSide():
    global flip
    global wPieces
    global bPieces
    flip = not flip
    drawBoard()
    drawPieces(flip)
    if flip is False:
        for i in wPieces:
            if chessBoard.board[(int)(i[0]/75)][(int)(i[1]/75)].pieceOccupy.toString() == "P":
                chessBoard.board[(int)(i[0]/75)][(int)(i[1]/75)].pieceOccupy.passP = False
    else:
        for i in bPieces:
            if chessBoard.board[(int)((525-i[0])/75)][(int)((525-i[1])/75)].pieceOccupy.toString() == "P":
                chessBoard.board[(int)((525-i[0])/75)][(int)((525-i[1])/75)].pieceOccupy.passP = False

def Move(x, y):
    global x_origin
    global y_origin
    print("Move from [", x_origin, ",", y_origin, "] to [", x, ",", y, "]")
    if selectedPiece.toString() == "P":

        if selectedPiece.x_coord +2 == x or selectedPiece.x_coord -2 == x:
            selectedPiece.passP = True

        if selectedPiece.alliance == "B" and y != y_origin:
            if chessBoard.board[x-1][y].pieceOccupy.toString() == "P":
                if chessBoard.board[x-1][y].pieceOccupy.passP == True:
                    chessBoard.updateBoard(x-1, y, nullPiece())

        if selectedPiece.alliance == "W" and y != y_origin:
            if chessBoard.board[x+1][y].pieceOccupy.toString() == "P":
                print(chessBoard.board[x+1][y].pieceOccupy.passP)
                if chessBoard.board[x+1][y].pieceOccupy.passP == True:
                    chessBoard.updateBoard(x+1, y, nullPiece())

    selectedPiece.x_coord = x
    selectedPiece.y_coord = y
    selectedPiece.fMove = False
    chessBoard.updateBoard(x, y, selectedPiece)
    chessBoard.updateBoard(x_origin, y_origin, nullPiece())


def square(x_coord, y_coord, width, height, color):
    global allTiles
    pygame.draw.rect(screen, color, [x_coord, y_coord, width, height])
    allTiles.append([color, [x_coord, y_coord, width, height]])

def drawBoard():
    x_coord = 0
    y_coord = 0
    color = 0
    width = 75
    height = 75

    for _ in range(8):
        for _ in range(8):
            if color % 2 == 0:
                square(x_coord, y_coord, width, height, white)
                x_coord += 75
            else:
                square(x_coord, y_coord, width, height, black)
                x_coord += 75
            color += 1
        color += 1
        x_coord = 0
        y_coord += 75

def drawPieces(flip):
    global currentAlliance
    global allPieces
    global wPieces
    global bPieces
    allPieces.clear()
    wPieces.clear()
    bPieces.clear()
    x_coord = 0
    y_coord = 0
    width = 75
    height = 75

    if flip is False:
        currentAlliance = "W"
        for rows in range(8):
            for cols in range(8):
                if not chessBoard.board[rows][cols].pieceOccupy.toString() == "0":
                    img = pygame.image.load("./art/" 
                            + chessBoard.board[rows][cols].pieceOccupy.alliance[0].upper()
                            + chessBoard.board[rows][cols].pieceOccupy.toString().upper()
                            + ".png")
                    img = pygame.transform.scale(img, (width, height))
                    if(chessBoard.board[rows][cols].pieceOccupy.alliance[0].upper() == "W"):
                        wPieces.append([y_coord, x_coord])
                    else:
                        bPieces.append([y_coord, x_coord])
                    allPieces.append([[y_coord, x_coord], img]) 
                x_coord += 75
            x_coord = 0
            y_coord += 75
    else:
        currentAlliance = "B"
        for rows in reversed(range(8)):
            for cols in reversed(range(8)):
                if not chessBoard.board[rows][cols].pieceOccupy.toString() == "0":
                    img = pygame.image.load("./art/" 
                            + chessBoard.board[rows][cols].pieceOccupy.alliance[0].upper()
                            + chessBoard.board[rows][cols].pieceOccupy.toString().upper()
                            + ".png")
                    img = pygame.transform.scale(img, (width, height))
                    if(chessBoard.board[rows][cols].pieceOccupy.alliance[0].upper() == "W"):
                        wPieces.append([y_coord, x_coord])
                    else:
                        bPieces.append([y_coord, x_coord])
                    allPieces.append([[y_coord, x_coord], img])
                x_coord += 75
            x_coord = 0
            y_coord += 75

    for img in allPieces:
        screen.blit(img[1], (img[0][1],img[0][0]))

gO = False

drawBoard()
drawPieces(flip)
currentPieces = wPieces

while not gO:

    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            gO = True
            pygame.quit()
            quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            #get UI coordinate
            cols, rows = pygame.mouse.get_pos()
            bRows = (int)(rows/75)
            bCols = (int)(cols/75)
            if currentAlliance == "B":
                bRows = (int)((600-rows)/75)
                bCols = (int)((600-cols)/75)
            if chessBoard.board[bRows][bCols].pieceOccupy.alliance == currentAlliance:
                pieceMove.clear()
                selectedPiece = chessBoard.board[bRows][bCols].pieceOccupy
                x_origin = bRows
                y_origin = bCols
                print(selectedPiece, "at coordination: [", bRows, ", ", bCols, "]")
                pieceMove = selectedPiece.validMove(chessBoard.board)
                print("validMoves:", pieceMove)
                drawBoard()
                drawPieces(flip)
                for j in pieceMove:
                    x = j[0]*75
                    y = j[1]*75
                    if(currentAlliance == "B"):
                        x = 525 - x
                        y = 525 - y
                    img = pygame.image.load("./art/green_circle_neg.png")
                    img = pygame.transform.scale(img, (75, 75))
                    screen.blit(img, (y, x))
            elif selectedPiece != None and [bRows, bCols] in pieceMove:
                Move(bRows, bCols)
                switchSide()
                
        if event.type == pygame.MOUSEMOTION and not selectedPiece == None and pygame.mouse.get_pressed() == (1, 0, 0):
            #get UI coordinate
            cols, rows = pygame.mouse.get_pos()
            
        if event.type == pygame.MOUSEBUTTONUP and not selectedPiece == None and pygame.mouse.get_pressed() == (1, 0, 0):
            #get UI coordinate
            cols, rows = pygame.mouse.get_pos()
    
    pygame.display.update()
    clock.tick(60)