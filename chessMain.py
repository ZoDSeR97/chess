from board.chessBoard import Board
import pygame, os, sys

pygame.init()

black, white = (222, 184, 135), (255, 255, 255)

ui_width, ui_height = 600, 600

selectedPiece = None

screen = pygame.display.set_mode((ui_width, ui_height))

pygame.display.set_caption("ChessA")

clock = pygame.time.Clock()

allTiles = []
allPieces = []
flip = False

chessBoard = Board()
chessBoard.createBoard()

def square(x_coord, y_coord, width, height, color):
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
    allPieces.clear()
    x_coord = 0
    y_coord = 0
    width = 75
    height = 75

    if flip is False:
        order = range(8)
    else:
        print("Flip")
        order = reversed(range(8))
        print(order)

    if flip is True:
        print(allPieces)

    for rows in order:
        for cols in order:
            #print(rows, cols)
            if not chessBoard.board[rows][cols].pieceOccupy.toString() == "0":
                img = pygame.image.load("./art/" 
                        + chessBoard.board[rows][cols].pieceOccupy.alliance[0].upper()
                        + chessBoard.board[rows][cols].pieceOccupy.toString().upper()
                        + ".png")
                img = pygame.transform.scale(img,(width, height))
                allPieces.append([img, [x_coord, y_coord]])
                if flip is True:
                    print(allPieces)  
            x_coord += 75
        x_coord = 0
        y_coord += 75

gO = False

drawBoard()
drawPieces(False)

for img in allPieces:
    screen.blit(img[0], img[1])

drawBoard()
drawPieces(True)

for img in allPieces:
    screen.blit(img[0], img[1])

while not gO:
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            gO = True
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN and selectedPiece == None:
            #get UI coordinate
            x, y = pygame.mouse.get_pos()
                
            if event.type == pygame.MOUSEMOTION and not selectedPiece == None:
                #get UI coordinate
                x, y = pygame.mouse.get_pos()
                    
        elif event.type == pygame.MOUSEBUTTONUP and not selectedPiece == None:
            #get UI coordinate
            x, y = pygame.mouse.get_pos()    

    pygame.display.update()
    clock.tick(60)