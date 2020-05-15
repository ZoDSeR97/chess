from board.chessBoard import Board
from pieces.nullPiece import nullPiece
from rule.chessRule import inCheck
from rule.chessRule import Stale
from userInterface import titlePage
from Bot import randomBot
import pygame, os, sys, time, random

pygame.init()

black, white = (222, 184, 135), (255, 255, 255)

selectedPiece = None
playerAlliance = None
stalemate = None
passPawn = None
x_origin = None
y_origin = None
check = None
screen = None
mode = None

flip = False
gO = False
inCheck = False

count = 0
moves = {"W": 0, "B": 0}

allPieces = []
currentPieces = []
wPieces = []
bPieces = []
pieceMove = set()
reqMove = set()
checkingMove = set()
chessBoard = Board()

pygame.display.set_caption("Pygame Chess")

clock = pygame.time.Clock()

currentAlliance = "W"
wKing = chessBoard.board[7][4].pieceOccupy
bKing = chessBoard.board[0][4].pieceOccupy

#Draw every board tile O(n^2) but offer more board color variation
def drawBoard():
    x_coord = 0
    y_coord = 0
    color = 0
    width = 75
    height = 75

    for _ in range(8):
        for _ in range(8):
            if color % 2 == 0:
                pygame.draw.rect(screen, white, [x_coord, y_coord, width, height])
                x_coord += 75
            else:
                pygame.draw.rect(screen, black, [x_coord, y_coord, width, height])
                x_coord += 75
            color += 1
        color += 1
        x_coord = 0
        y_coord += 75

#Blitting all pieces available O(n^2)
def drawPieces(flip):
    global allPieces
    global wPieces
    global bPieces
    allPieces.clear()
    wPieces.clear()
    bPieces.clear()
    traverse = [i for i in range(8)]
    x_coord = 0
    y_coord = 0

    if flip is True:
        #resverse bliting = flip the board
        traverse.reverse()

    for rows in traverse:
        for cols in traverse:
            if chessBoard.board[rows][cols].pieceOccupy.symbol != "0":
                img = pygame.image.load("./art/" 
                        + chessBoard.board[rows][cols].pieceOccupy.alliance[0].upper()
                        + chessBoard.board[rows][cols].pieceOccupy.symbol.upper()
                        + ".png")
                img = pygame.transform.scale(img, (75, 75))
                if chessBoard.board[rows][cols].pieceOccupy.alliance[0].upper() == "W":
                    wPieces.append((rows, cols))
                else:
                    bPieces.append((rows, cols))
                allPieces.append([(y_coord, x_coord), img]) 
            x_coord += 75
        x_coord = 0
        y_coord += 75     

    for img in allPieces:
        screen.blit(img[1], (img[0][1],img[0][0]))

def switchSide():
    global flip
    global selectedPiece
    global pieceMove
    global passPawn
    global currentAlliance
    global currentPieces
    global gO

    if moves[currentAlliance] == 50:
        print("50 Shade of Stale")
        gO = True
        pass

    if mode == "P2F":
        flip = not flip

    if passPawn is not None:
        passPawn.passP = False
        passPawn = None

    drawBoard()
    drawPieces(flip)
    if selectedPiece.symbol == "P" and selectedPiece.passP is True:
        passPawn = selectedPiece
    
    if currentAlliance == "W":
        currentAlliance = "B"
        currentPieces = bPieces
    else:
        currentAlliance = "W"
        currentPieces = wPieces
    pieceMove.clear()

#piece move from A to B, Null will move to A
def Move(x, y):
    global x_origin
    global y_origin
    global selectedPiece
    global chessBoard
    global count
    global moves

    if chessBoard.board[x][y].pieceOccupy.symbol != "0":
        moves[currentAlliance] = 0
    else:
        moves[currentAlliance] += 1

    if selectedPiece.symbol == "P":
        moves[selectedPiece.alliance] = 0

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
    count += 1
    print(moves)
    switchSide()

def prepGame(mode):
    global playerAlliance
    global stalemate
    global currentPieces
    global wPieces

    if mode == "DB" or mode == "CB":
        Alliance = ["W", "B"]
        playerAlliance = random.choice(Alliance)
        drawBoard()
        drawPieces(False)
        currentPieces = wPieces
        stalemate = Stale(chessBoard.board, wPieces, bPieces, allPieces)
    else:
        drawBoard()
        drawPieces(False)
        currentPieces = wPieces
        stalemate = Stale(chessBoard.board, wPieces, bPieces, allPieces)

def main():
    global gO
    global selectedPiece
    global pieceMove
    global x_origin
    global y_origin

    while not gO:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                gO = True
                pygame.quit()
                quit()

            if mode == "DB" and currentAlliance != playerAlliance:
                selectedPiece, move = randomBot(chessBoard, currentPieces).randomMoves()
                if move != 0:
                    moves[currentAlliance] += move
                else:
                    moves[currentAlliance] = 0
                if selectedPiece is None:
                    gO = True
                    break
                print(moves)
                switchSide()
                continue

            if event.type == pygame.MOUSEBUTTONDOWN:
                #get UI coordinate
                cols, rows = pygame.mouse.get_pos()

                #convert into board coordinate
                bRows = (int)(rows/75)
                bCols = (int)(cols/75)
                if currentAlliance == "B" and mode == "P2F":
                    bRows = (int)((600-rows)/75)
                    bCols = (int)((600-cols)/75)

                if chessBoard.board[bRows][bCols].pieceOccupy.alliance == currentAlliance:
                    #clear pieceMove to get new valid move of new selectedPiece
                    pieceMove.clear()
                    selectedPiece = chessBoard.board[bRows][bCols].pieceOccupy

                    #keep origin to erase piece into null at the board
                    x_origin = bRows
                    y_origin = bCols

                    #convert into set to check whether an element in a set (faster than using list) 
                    pieceMove = set(selectedPiece.validMove(chessBoard.board))

                    #refresh the board remove previous valid move blit
                    drawBoard()
                    drawPieces(flip)

                    if pieceMove is not set():
                        #bliting valid move onto the board
                        for j in pieceMove:
                            y = j[0]*75
                            x = j[1]*75
                            if currentAlliance == "B" and mode == "P2F":
                                y = 525 - y
                                x = 525 - x
                            img = pygame.image.load("./art/green_circle_neg.png")
                            img = pygame.transform.scale(img, (75, 75))
                            screen.blit(img, (x, y))
                elif selectedPiece != None and (bRows, bCols) in pieceMove:
                    Move(bRows, bCols)
                    
            if event.type == pygame.MOUSEMOTION and not selectedPiece == None and pygame.mouse.get_pressed() == (1, 0, 0):
                #get UI coordinate
                cols, rows = pygame.mouse.get_pos()
                
            if event.type == pygame.MOUSEBUTTONUP and not selectedPiece == None and pygame.mouse.get_pressed() == (1, 0, 0):
                #get UI coordinate
                cols, rows = pygame.mouse.get_pos()
        
        pygame.display.update()
        clock.tick(60)

while True:
    screen = pygame.display.set_mode((600, 600))
    flip = False
    passPawn = None
    check = None
    selectedPiece = None
    count = 0
    moves = {"W": 0, "B": 0}
    chessBoard = Board()
    currentAlliance = "W"
    title = titlePage("Pygame Chess")
    mode = title.modeSelect(screen, clock)
    if mode == "Quit":
        pygame.quit()
        break
    screen = pygame.display.set_mode((1000, 600))
    prepGame(mode)
    gO = False
    main()