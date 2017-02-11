import pygame, math
import copy

####################################
####################################

screen = pygame.display.set_mode((800, 600))

def init(data):
    data.background = (255, 255, 255)
    data.drawing = False
    data.pos = (0, 0)
    data.cells = dict()
    data.radius = 10
    data.click = False
    data.buttonColor = (0,0,0)
    data.cpButton = (70, 545, 50, 50)
    data.colorArr = []

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
    data.barWidth, data.barLength = 40, data.cMax * 12 // data.cStep - data.margin
    data.colorBar = []  # List of all the colors in rgb list form
    data.colorPicker = False # If they color picker button is pressed.
    makeColorBar(data)
    
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
    data.easelBottom2 = (0, data.height-data.easelBottomH-10, data.width, 10)
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
    pygame.draw.rect(data.textCanvas, data.brown3, data.easelBottom, 0)
    pygame.draw.rect(data.textCanvas, data.brown4, data.easelBottom2, 0)
    #draw color picker
    data.pickerColor = (data.red, data.green, data.blue)
    pygame.draw.rect(data.textCanvas, data.pickerColor, (70, data.height
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
    x, y = event.pos
    a, b, w, h = data.cpButton
    if data.colorPicker and event.type == pygame.MOUSEBUTTONDOWN:
            # If within the rainbow bar, change the bar rgb values
        if x > data.margin * 2 + data.cMax * 2 and y < data.barLength + data.margin:
            data.cBar = y
            data.r = data.colorBar[data.cBar//2][0]
            data.g = data.colorBar[data.cBar//2][1]
            data.b = data.colorBar[data.cBar//2][2]
        # If within the gradient square, update the location in the square
        elif (x > data.margin and x < data.margin + data.cMax * 2 and
            y > data.margin and y < data.margin + data.cMax * 2):
            data.gCirc[0], data.gCirc[1] = x, y
    if event.type == pygame.MOUSEBUTTONDOWN: 
        data.click = True
        if x >= a and x <= (a+w) and y >= b and y <= (b+h):
            if not data.colorPicker: data.colorPicker = True
            elif data.colorPicker: data.colorPicker = False
    if event.type == pygame.MOUSEBUTTONUP: 
        data.click = False
    if event.type == pygame.MOUSEMOTION:
        if data.click == True:
            data.pos = event.pos
            data.cells[data.pos] = (data.red, data.green, data.blue)

def keyPressed(event, data):
    pass

def timerFired(data):
    pass

def redrawAll(screen, data):
    x,y,w,h = data.cpButton
    drawButton(screen, data, x,y,w,h)
    if data.colorPicker:
        drawColorPicker(screen, data)
    else: 
        drawUI(screen, data)
        draw(screen, data)

def drawColorPicker(screen, data):
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

def rgbToHSL(r, g, b):
    red = r/255
    green = g/255
    blue = b/255
    cmaximum = max(red, green, blue)
    cminimum = min(red, green, blue)
    delta = cmaximum - cminimum
    l = (cmaximum + cminimum)/2
    if delta == 0:
        s = 0
        h = 0
    else:
        if max(red, green, blue) == red: 
            h = (green-blue)/(cmaximum-cminimum)
        elif max(red, green, blue) == green:
            h = 2.0 + (blue - red)/(cmaximum-cminimum)
        else:
            h = 4.0 + (red - green)/(cmaximum-cminimum)
        if h < 0: h += 360
        h *= 60
        if l < 0.5:
            s = (cmaximum-cminimum)/(cmaximum+cminimum)
        else: s = (cmaximum-cminimum)/(2.0-cmaximum-cminimum)
# def roundline(screen, color, start, end, radius):
#     dx = end[0]-start[0]
#     dy = end[1]-start[1]
#     distance = max(abs(dx), abs(dy))
#     for i in range(distance):
#         x = int(start[0]+float(i)/distance*dx)
#         y = int(start[1]+float(i)/distance*dy)
#         pygame.draw.circle(screen, color, (x, y), radius)

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

def drawButton(screen, data, x, y, w, h):
    pygame.draw.rect(screen, data.buttonColor, [x, y, w, h])
    # pygame.draw.rect(screen, data.white, [x, y, w, h], 8)
    # pygame.draw.rect(screen, data.black, [x, y, w, h], 4)
    # drawText(screen, data, text, cX, cY, font, textColor)

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
        color = (data.colorBar[i//2][0],
            data.colorBar[i//2][1], data.colorBar[i//2][2])
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
            r1, g1, b1 = data.cMax - y//2, data.cMax - y//2, data.cMax - y//2  
            rN, gN, bN = colorBlender([r1, g1, b1], [r2, g2, b2], data.cMax-2,x//2)
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

def getColors(screen, data):
    colorArr = []
    for x in range(data.width):
        colColor = []
        for y in range(data.height):
            colColor.append(screen.get_at(x, y))
        colorArr.append(copy.copy(colColor))
    data.colorArr = copy.copy(colorArr)

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
    
run(800, 600)
