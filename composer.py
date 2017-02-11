import pygame

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
    
    
def mousePressed(event, data):
    pass

def keyPressed(event, data):
    pass

def timerFired(data):
    pass

def redrawAll(screen, data):
    pass
    
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

run(1000, 700)
