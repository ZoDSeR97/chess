import pygame

class Text:
    hovered = False
    title = False
    fSize = 0
    def __init__(self, text, pos,screen, title, size):
        self.text = text
        self.pos = pos
        self.title = title
        self.fSize = size
        self.set_rect()
        self.draw(screen)

    def draw(self,screen):
        self.set_rend()
        screen.blit(self.rend, self.rect)

    def set_rend(self):
        title_font = pygame.font.Font("C:\Windows\Fonts\Ebrima.ttf", self.fSize)
        self.rend = title_font.render(self.text, True, self.get_color())
    
    def get_color(self):
        if self.hovered:
            return (255, 0, 0)
        elif self.title:
            return (255, 255, 255)
        else:
            return (0, 0, 0)

    def set_rect(self):
        self.set_rend()
        self.rect = self.rend.get_rect()
        self.rect.topleft = self.pos

class titlePage:
    def __init__(self, text):
        self.title = text

    def modeSelect(self, screen, clock):
        black, white = (0, 0, 0), (255, 255, 255)
        box_length = 240
        box_height = 35
        count = 0
        gameTypes = list()
        traverse = [(50, 415), (50, 465), (320, 415), (320, 465), (180, 515)]
        nameList = ["Vs. P2 (Flip)", "Vs. P2 (No Flip)", "Vs. DumbBot", "Vs. ComplexBot", "Exit"]
        # background initial
        img = pygame.image.load("./art/intro.jpg")
        img = pygame.transform.scale(img, (600, 600))
        screen.blit(img, (0, 0))
        Text(self.title, (60, 20),screen, True, 75)

        # selection box
        # pygame.draw.rect(screen, black, [125, 35, 145, 210])
        for i in traverse:
            pygame.draw.rect(screen, black, [i[0], i[1], box_length, box_height])
            pygame.draw.rect(screen, white, [i[0] + 1, i[1] + 1, box_length - 2, box_height - 2])
            if count == 4:
                gameTypes.append(Text(nameList[count], (i[0] + 95, i[1] - 5), screen, False, 30))
            elif count%2 != 0:
                gameTypes.append(Text(nameList[count], (i[0] + 20, i[1] - 5), screen, False, 30))
            else:
                gameTypes.append(Text(nameList[count], (i[0] + 40, i[1] - 5), screen, False, 30))
            count += 1

        while True:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # get UI coordinate
                    cols, rows = pygame.mouse.get_pos()
                    # print(cols, rows)
                    if traverse[0][0] < cols < traverse[0][0] + 240 and traverse[0][1] < rows < traverse[0][1] + 30:
                        return "P2F"
                    if traverse[1][0] < cols < traverse[1][0] + 240 and traverse[1][1] < rows < traverse[1][1] + 30:
                        return "P2"
                    if traverse[2][0] < cols < traverse[2][0] + 240 and traverse[2][1] < rows < traverse[2][1] + 30:
                        return "DB"
                    if traverse[3][0] < cols < traverse[3][0] + 240 and traverse[3][1] < rows < traverse[3][1] + 30:
                        return "CB"
                    if traverse[4][0] < cols < traverse[4][0] + 240 and traverse[4][1] < rows < traverse[4][1] + 30:
                        return "Quit"

            # gameDisplay.fill(white)
            for gameType in gameTypes:
                if gameType.rect.collidepoint(pygame.mouse.get_pos()):
                    gameType.hovered = True
                else:
                    gameType.hovered = False
                gameType.draw(screen)
                pygame.display.update()
            # pygame.display.update()
            clock.tick(15)
    ### End Title part ###
    