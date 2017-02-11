import pygame

####################################
####################################

screen = pygame.display.set_mode((800, 600))

def init(data):
    data.background = (255, 255, 255)
    data.drawing = False
    data.pos = (0, 0)
    data.cells = dict()
    data.color = (0, 0, 0)
    data.radius = 10
    data.click = False

# def roundline(srf, color, start, end, radius=1): #taken from stack overflow
# 	dx = end[0]-start[0]
#     dy = end[1]-start[1]
#     distance = max(abs(dx), abs(dy))
#     for i in range(distance):
#         x = int(start[0]+float(i)/distance*dx)
#         y = int(start[1]+float(i)/distance*dy)
#         pygame.draw.circle(srf, color, (x, y), radius)
<<<<<<< HEAD

=======
>>>>>>> origin/master
def roundline(srf, color, start, end, radius=1): #taken from stack overflow
    screen = pygame.display.set_mode(size)

def mousePressed(event, data):
    if event.type == pygame.MOUSEBUTTONDOWN: 
        data.click = True
    if event.type == pygame.MOUSEBUTTONUP: 
        data.click = False
    if event.type == pygame.MOUSEMOTION:
        if data.click == True:
            data.pos = event.pos
            data.cells[data.pos] = data.color

def keyPressed(event, data):
    pass

def timerFired(data):
    pass

def redrawAll(screen, data):
    draw(screen, data)
    
# Modified from 112 website
def make2dList(rows, cols, value=0):
    a=[]
    for row in range(rows): a += [[value]*cols]
    return a

# From lab11
def db(*args):
    dbOn = False
    if (dbOn): print(args)

def draw(screen, data):
    for loc in data.cells:
        pygame.draw.circle(screen, data.cells[loc], loc, data.radius)

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
run(1000, 700)
