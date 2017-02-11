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

    #Color picker stuff
    data.cMax, data.cStep = 255, 5  # Max value for colors, the step of the
    # rainbow bar
    data.margin = 10
    data.r, data.g, data.b = data.cMax, 0, 0
    # The rgb values for the color bar
    data.red, data.green, data.blue = data.cMax, 0, 0
    # The rgb values for the actual color
    data.cBar, data.gCirc = data.margin, [data.cMax * 2 + data.margin, data.margin]
    # The location on the rainbow bar (y) and gradient square (x, y)
    data.barWidth, data.barLength = 40, data.cMax * 12 / data.cStep - data.margin
    data.colorBar = []  # List of all the colors in rgb list form
    data.colorPicker = False # If they color picker button is pressed.
    makeColorBar(data)

# def roundline(srf, color, start, end, radius=1): #taken from stack overflow
# 	dx = end[0]-start[0]
#     dy = end[1]-start[1]
#     distance = max(abs(dx), abs(dy))
#     for i in range(distance):
#         x = int(start[0]+float(i)/distance*dx)
#         y = int(start[1]+float(i)/distance*dy)
#         pygame.draw.circle(srf, color, (x, y), radius)

def mousePressed(event, data):
    if data.colorPicker:
            # If within the rainbow bar, change the bar rgb values
        x, y = event.pos
        if x > data.margin * 2 + data.cMax * 2 and y < data.barLength + data.margin:
            data.cBar = y
            data.r = data.colorBar[data.cBar/2][0]
            data.g = data.colorBar[data.cBar/2][1]
            data.b = data.colorBar[data.cBar/2][2]
        # If within the gradient square, update the location in the square
        elif (x > data.margin and x < data.margin + data.cMax * 2 and
            y > data.margin and y < data.margin + data.cMax * 2):
            data.gCirc[0], data.gCirc[1] = x, y
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
    if data.colorPicker:
        drawGradientSquare(screen, data)
        drawColorBar(screen, data)
        drawColor(screen, data)

    
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

# This function makes the list of all the colors on the rainbow bar
def makeColorBar(data):
    red, green, blue = data.cMax, 0, 0
    for i in range(data.barLength):
        if red == data.cMax and green < data.cMax and blue == 0:
            green += data.cStep
        elif green == data.cMax and red > 0:
            red -= data.cStep
        elif green == data.cMax and blue < data.cMax:
            blue += data.cStep
        elif blue == data.cMax and green > 0:
            green -= data.cStep
        elif blue == data.cMax and red < data.cMax:
            red += data.cStep
        else:
            blue -= data.cStep
        data.colorBar.append([red, green, blue])

# This function draws a rainbow bar down the right side of the screen
def drawColorBar(screen, data):
    for i in range(data.barLength):
        color = (data.colorBar[i/2][0],
            data.colorBar[i/2][1], data.colorBar[i/2][2])
        pygame.draw.line(screen, color, [data.cMax * 2 + data.margin * 2,
            i + data.margin],[data.cMax * 2 + data.margin * 2 + data.barWidth, i + data.margin])
    pygame.draw.rect(screen, [0, 0, 0], [data.margin * 2 + data.cMax * 2,
        data.cBar-3,data.barWidth,6])

# This function sets the color to be displayed based on where the circle is
def setColor(data):
    cx, cy = data.gCirc[0] - data.margin, data.gCirc[1] - data.margin
    r1, g1, b1 = data.cMax - cy / 2, data.cMax - cy / 2, data.cMax - cy / 2
    dry, dgy = float(data.r) / (data.cMax), float(data.g) / (data.cMax)
    dby = float(data.b) / (data.cMax)
    r2, g2, b2 = data.r - dry * cy / 2, data.g - dgy * cy / 2, data.b - dby * cy / 2
    data.red, data.green, data.blue = colorBlender([r1,g1,b1], [r2,g2,b2],
        data.cMax * 2 - 2, cx - 1)
            
# This function uses the colorBlender() function to draw a gradient square of
# the entered values
def drawGradientSquare(screen, data):
    for y in range(data.cMax * 2):
        dry, dgy = float(data.r) / (data.cMax), float(data.g) / (data.cMax), 
        dby = float(data.b) / (data.cMax)
        r2, g2, b2 = data.r - dry * y/2, data.g - dgy * y/2, data.b - dby * y/2
        if r2 < 0: r2 = 0
        if g2 < 0: g2 = 0
        if b2 < 0: b2 = 0
        for x in range(data.cMax * 2):
            r1, g1, b1 = data.cMax - y/2, data.cMax - y/2, data.cMax - y/2  
            rN, gN, bN = colorBlender([r1, g1, b1], [r2, g2, b2], data.cMax-2,x/2)
            color = [rN, gN, bN]
            pygame.draw.line(screen, color, [x + data.margin, y + data.margin], 
                [x + data.margin + 1, y + data.margin])
        cx, cy = data.gCirc[0], data.gCirc[1]
        pygame.draw.ellipse(screen, [0, 0, 0], [cx - 2, cy - 2, 4, 4])
        setColor(data)

# This function returns the nth midpoint between the two entered rgb color lists
# Modified from homework 1
def colorBlender(rgb1, rgb2, midpoints, n):
    if n < 0 or n > midpoints + 1:
        return None

    r1, g1, b1 = rgb1[0], rgb1[1], rgb1[2]
    r2, g2, b2 = rgb2[0], rgb2[1], rgb2[2]
    
    midIntR = abs(r1 - r2) / float(midpoints + 1) * n
    midIntG = abs(g1 - g2) / float(midpoints + 1) * n
    midIntB = abs(b1 - b2) / float(midpoints + 1) * n
    
    if r1 > r2:
        midR = r1 - midIntR
        
    else:
        midR = r1 + midIntR
        
    if g1 > g2:
        midG = g1 - midIntG
        
    else:
        midG = g1 + midIntG
        
    if b1 > b2:
        midB = b1 - midIntB
        
    else:
        midB = b1 + midIntB

    return midR, midG, midB

# This function draws the selected color at the bottom of the screen
def drawColor(screen, data):
    # if data.red > 255: data.red = 255
    # if data.green > 255: data.green = 255
    # if data.blue > 255: data.blue = 255
    color = [data.red, data.green, data.blue]
    pygame.draw.rect(screen, color, [data.margin,
        data.cMax * 2 + data.margin * 2, data.cMax * 2, (data.height - (data.margin * 3 + 
                (data.cMax * 2))) / 2])
    print(data.red, data.green, data.blue)

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
