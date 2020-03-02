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

pieceMove = []
currentAlliance = "W"

chessBoard = Board()
chessBoard.createBoard()

flip = False

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
        for rows in range(8):
            for cols in range(8):
                if not chessBoard.board[rows][cols].pieceOccupy.toString() == "0":
                    img = pygame.image.load("./art/" 
                            + chessBoard.board[rows][cols].pieceOccupy.alliance[0].upper()
                            + chessBoard.board[rows][cols].pieceOccupy.toString().upper()
                            + ".png")
                    img = pygame.transform.scale(img, (width, height))
                    allPieces.append([[y_coord, x_coord], img]) 
                x_coord += 75
            x_coord = 0
            y_coord += 75
    else:
        for rows in reversed(range(8)):
            for cols in reversed(range(8)):
                if not chessBoard.board[rows][cols].pieceOccupy.toString() == "0":
                    img = pygame.image.load("./art/" 
                            + chessBoard.board[rows][cols].pieceOccupy.alliance[0].upper()
                            + chessBoard.board[rows][cols].pieceOccupy.toString().upper()
                            + ".png")
                    img = pygame.transform.scale(img, (width, height))
                    allPieces.append([[y_coord, x_coord], img])
                x_coord += 75
            x_coord = 0
            y_coord += 75

    for img in allPieces:
        screen.blit(img[1], (img[0][1],img[0][0]))

gO = False

drawBoard()
drawPieces(flip)

while not gO:
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            gO = True
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN and selectedPiece == None:
            #get UI coordinate
            cols, rows = pygame.mouse.get_pos()

            for i in allPieces:
                if i[0][0] < rows < i[0][0]+75 and i[0][1] < cols < i[0][1]+75:
                    if chessBoard.board[(int)(i[0][0]/75)][(int)(i[0][1]/75)].pieceOccupy.alliance == currentAlliance:
                        print("True")
                        print((int)(i[0][0]/75), (int)(i[0][1]/75))
                        selectedPiece = chessBoard.board[(int)(i[0][0]/75)][(int)(i[0][1]/75)].pieceOccupy
                        print(selectedPiece)
                        pieceMove = selectedPiece.validMove(chessBoard.board)
                        print(pieceMove)
                        for j in pieceMove:
                            img = pygame.image.load("./art/green_circle_neg.png")
                            img = pygame.transform.scale(img, (75, 75))
                            screen.blit(img, (j[1]*75, j[0]*75))
                
        if event.type == pygame.MOUSEMOTION and not selectedPiece == None and pygame.mouse.get_pressed() == (1, 0, 0):
            #get UI coordinate
            x, y = pygame.mouse.get_pos()
                    
        if event.type == pygame.MOUSEBUTTONUP and not selectedPiece == None and pygame.mouse.get_pressed() == (1, 0, 0):
            #get UI coordinate
            x, y = pygame.mouse.get_pos()
            
        if event.type == pygame.MOUSEBUTTONDOWN and not selectedPiece == None:
            #get UI coordinate
            x, y = pygame.mouse.get_pos()
        '''
        drawBoard()
        drawPieces(flip)
        '''
    pygame.display.update()
    clock.tick(60)