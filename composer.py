import pygame, math

####################################
####################################

screen = pygame.display.set_mode((800, 600))

def init(data):
    data.background = [255, 255, 255]
    data.drawing = False
    data.lastPos = (0, 0)
    data.color = (0, 0, 0)
    data.radius = 10

def roundline(srf, color, start, end, radius=1): #taken from stack overflow
    screen = pygame.display.set_mode(size)
    
def drawUI(screen, data):
    data.textCanvas = pygame.Surface(screen.get_size())
    data.textCanvas.fill((0, 0, 0))
    
    data.white = (250, 250, 250)
    data.lightGray = (200, 200, 200)
    data.black = (0, 0, 0)
    data.brown1 = (215, 160, 87)
    data.brown2 = (180, 128, 60)
    data.brown3 = (165, 120, 55)
    data.brown4 = (145, 100, 43)
    data.pink = (255, 153, 153)
    data.darkPink = (245, 102, 102)
    data.easelPlankW = 20
    data.easelPlankH = 80
    data.easelBottomH = 60
    
    #draw easel
    data.easelMidPlankPoints = (data.width/2-(data.easelPlankW/2), 0, 
        data.easelPlankW, data.easelPlankH)
    data.easelLPlankPoints = [(170, data.easelPlankH), (data.width/2-
        (data.easelPlankW/2), data.easelPlankH/4),
        (data.width/2-(data.easelPlankW/2), data.easelPlankH/4+data.easelPlankW), 
        (230, data.easelPlankH)]
    data.easelRPlankPoints = [(data.width/2+(data.easelPlankW/2),
    data.easelPlankH/4), (630,data.easelPlankH), 
    (570,data.easelPlankH),(data.width/2+(data.easelPlankW/2),data.easelPlankH/4
        +data.easelPlankW)] 
    data.easelBottom = (0, data.height-data.easelBottomH, data.width,
                                                            data.easelBottomH)
    pygame.draw.rect(data.textCanvas, data.black, (0, 0, 800, 600), 0)
    pygame.draw.polygon(data.textCanvas,data.lightGray,[(0, data.easelPlankH), (30,
        data.easelPlankH-20), (770, data.easelPlankH-20), (data.width, 
        data.easelPlankH)], 0)
    pygame.draw.rect(data.textCanvas, data.brown1, data.easelMidPlankPoints, 0)
    pygame.draw.polygon(data.textCanvas, data.brown3, data.easelLPlankPoints, 0)
    pygame.draw.polygon(data.textCanvas, data.brown3, data.easelRPlankPoints, 0)
    pygame.draw.rect(data.textCanvas, data.white, (0, data.easelPlankH, data.width, 
                data.height-data.easelPlankH))
    
    #draw toolbar 
    data.eraserPoints = [(170,580), (200,550), (230,550), (200,580)] 
    data.eraserPoints2 = [(170, 580), (200, 580), (230, 550), (230, 560), 
                    (200, 590), (170, 590)]
    pygame.draw.rect(data.textCanvas, data.brown4, data.easelBottom, 0)
    #draw color picker
    #data.pickerColor = (data.red, data.green, data.blue)
    pygame.draw.rect(data.textCanvas, data.black, (70, data.height
        -data.easelBottomH+5, 50, 50), 0)
    #draw eraser
    pygame.draw.polygon(data.textCanvas, data.pink, data.eraserPoints, 0)
    pygame.draw.polygon(data.textCanvas, data.darkPink, data.eraserPoints2, 0)
    #draw audio button
    pygame.draw.polygon(data.textCanvas, data.black, [(613,570), (650,545),
                    (650,595)], 0)
    pygame.draw.ellipse(data.textCanvas, data.black, (640, 545, 25, 50), 0)
    pygame.draw.rect(data.textCanvas, data.black, (613,558,20,27), 0)
    pygame.draw.arc(data.textCanvas, data.black, (665,560,10,20), -1*math.pi/2,
                        math.pi/2, 3)
    pygame.draw.arc(data.textCanvas, data.black, (665,560,10,20), -1*math.pi/2,
                        math.pi/2, 3)
    pygame.draw.arc(data.textCanvas, data.black, (675,555,12,30), -1*math.pi/2,
                        math.pi/2, 3)
    #draw title
    titleFont = pygame.font.SysFont('avenir', 32, True)
    title = titleFont.render('c o m p o s e r', True, data.white)
    data.textCanvas.blit(title, (280, 545))
    #draw exit button
    pygame.draw.rect(data.textCanvas, data.black, (740, data.height
        -data.easelBottomH+10, 40, 40), 2)
    pygame.draw.line(data.textCanvas, data.black, (745, data.height
        -data.easelBottomH+15), (775, data.height
        -data.easelBottomH+45), 3)
    pygame.draw.line(data.textCanvas, data.black, (775, data.height
        -data.easelBottomH+15), (745, data.height
        -data.easelBottomH+45), 3)
    screen.blit(data.textCanvas, (0,0))
    pygame.display.flip()
def mousePressed(event, data):
    pass

def keyPressed(event, data):
    pass

def timerFired(data):
    pass

def redrawAll(screen, data):
    drawUI(screen, data)
    
# Modified from 112 website
def make2dList(rows, cols, value=0):
    a=[]
    for row in range(rows): a += [[value]*cols]
    return a

# From lab11
def db(*args):
    dbOn = False
    if (dbOn): print(args)

# This function takes the text, the center of the text, font, and color, and 
# draw the text on the screen.
def drawText(screen, data, text, x, y, font, color=[0, 0, 0]):
    textSurf = font.render(text, True, color)
    textRect = textSurf.get_rect()
    textRect.center = (x, y)
    screen.blit(textSurf, textRect)

def drawButton(screen, data, x, y, w, h, text, cX, cY, font, textColor):
    pygame.draw.rect(screen, data.buttonColor, [x, y, w, h])
    pygame.draw.rect(screen, data.white, [x, y, w, h], 8)
    pygame.draw.rect(screen, data.black, [x, y, w, h], 4)
    drawText(screen, data, text, cX, cY, font, textColor)

####################################
# use the run function as-is
####################################

def run(width=300, height=300):
    def redrawAllWrapper(screen, data):
        screen.fill(data.background)
        row, col = 0, 0
        color = [255, 255, 255]
        redrawAll(screen, data)
        pygame.display.flip()

    def mousePressedWrapper(event, screen, data):
        mousePressed(event, data)
        redrawAllWrapper(screen, data)

    def keyPressedWrapper(event, screen, data):
        keyPressed(event, data)
        redrawAllWrapper(screen, data)

    def timerFiredWrapper(screen, data):
        timerFired(data)
        redrawAllWrapper(screen, data)
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            return
        elif (event.type == pygame.MOUSEBUTTONDOWN or event.type == 
                    pygame.MOUSEBUTTONUP or event.type == pygame.MOUSEMOTION):
            mousePressedWrapper(event, screen, data)
        elif event.type == pygame.KEYUP:
            keyPressedWrapper(event, screen, data)
        # pause, then call timerFired again
        pygame.time.delay(data.timerDelay)
        timerFiredWrapper(screen, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    # create the screen
    pygame.init()
    init(data)
    if not pygame.font.get_init(): pygame.font.init()
    screen = pygame.display.set_mode([data.width, data.height])
    pygame.display.set_caption("COMPOSER")
    pygame.event.set_blocked(pygame.MOUSEMOTION)
    redrawAllWrapper(screen, data)
    # set up events
    # timerFiredWrapper(screen, data)
    while True:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            break
        elif (event.type == pygame.MOUSEBUTTONDOWN or event.type == 
                    pygame.MOUSEBUTTONUP or event.type == pygame.MOUSEMOTION):
            mousePressedWrapper(event, screen, data)
        elif event.type == pygame.KEYUP:
            keyPressedWrapper(event, screen, data)
    # and launch the app
    print("bye!")
    pygame.quit()
    
run(800, 600)
