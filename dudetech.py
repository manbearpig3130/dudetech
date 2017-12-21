import pygame
import random
import datetime
from Tkinter import *
# import threading

####################
#  INITIALIZATION  #
####################
pygame.init()
gamex = 800
gamey = 600
screen = pygame.display.set_mode((gamex, gamey))
logo = pygame.image.load('Dudeism32.png')
titleimg = pygame.image.load('title.jpg')
pygame.display.set_icon(logo)
clock = pygame.time.Clock()
pygame.display.set_caption('DudeTech')
random.seed(datetime.datetime.now())
defont = pygame.font.Font("MEGADETH.ttf", 22)
FPS = 60

#######################
#  COLOR DEFINITIONS  #
#######################
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
white = (255, 255, 255)
skin = (212, 232, 181)
dudely = (88, 66, 130)
purple = (83, 3, 120)
grey = (128, 128, 128)
dgreen = (38, 127, 0)

#######################
#  CLASS DEFINITIONS  #
#######################
class ModWindow():
    def __init__(self, ball):
        self.nums = None
        self.window = Tk()
        self.sizeValue = IntVar()
        self.speed1 = IntVar()
        self.speed2 = IntVar()
        self.r = IntVar()
        self.g = IntVar()
        self.b = IntVar()
        self.negx = IntVar()
        self.negy = IntVar()
        self.colorcheckboxvar = IntVar()
        self.colorcheckbox = Checkbutton(self.window, variable=self.colorcheckboxvar, selectcolor='blue', text='Cycle Colors')
        self.sizeslider = Scale(self.window, label='Size', from_=0, to=150, variable=self.sizeValue, length=150, orient=HORIZONTAL)
        self.speed1slider = Scale(self.window, label='X speed', from_=0, to=50, variable=self.speed1, length=150, orient=HORIZONTAL)
        self.speed2slider = Scale(self.window, label='Y speed', from_=0, to=50, variable=self.speed2, length=150, orient=HORIZONTAL)
        self.redslider = Scale(self.window, label='Red', from_=0, to=255, variable=self.r, length=150, orient=HORIZONTAL)
        self.greenslider = Scale(self.window, label='Green', from_=0, to=255, variable=self.g, length=150, orient=HORIZONTAL)
        self.blueslider = Scale(self.window, label='Blue', from_=0, to=255, variable=self.b, length=150, orient=HORIZONTAL)
        self.submit = Button(self.window, text="Done", command=self.submit)
        self.negxcheckbutton = Checkbutton(self.window, text="Negative X", variable=self.negx, selectcolor='blue')
        self.negycheckbutton = Checkbutton(self.window, text="Negative Y", variable=self.negy, selectcolor='blue')

        self.sizeslider.grid(column=0, row=0, columnspan=2)
        self.speed1slider.grid(column=0, row=1, columnspan=2)
        self.negxcheckbutton.grid(column=1, row=1)
        self.speed2slider.grid(column=0, row=2, columnspan=2)
        self.negycheckbutton.grid(column=1, row=2)
        self.redslider.grid(column=0, row=3, columnspan=2)
        self.greenslider.grid(column=0, row=4, columnspan=2)
        self.blueslider.grid(column=0, row=5, columnspan=2)
        self.colorcheckbox.grid(column=1, row=6)
        self.submit.grid(column=0, row=8)

        self.sizeslider.set(ball.radius * 2)
        self.speed1slider.set(abs(ball.speed[0]))
        self.speed2slider.set(abs(ball.speed[1]))
        self.redslider.set(ball.color[0])
        self.greenslider.set(ball.color[1])
        self.blueslider.set(ball.color[2])
        if ball.speed[0] < 0:
            self.negxcheckbutton.select()
        if ball.speed[1] < 0:
            self.negycheckbutton.select()
        if ball.colorchange == 1:
            self.colorcheckbox.select()

    def getnums(self):
        return self.nums

    def submit(self):
        self.nums = ([int(self.speed1slider.get()), int(self.speed2slider.get())],
                     [int(self.redslider.get()), int(self.greenslider.get()),
                      int(self.blueslider.get())], int(self.sizeslider.get()),
                     self.colorcheckboxvar.get())
        if self.negx.get() == 1:
            self.nums[0][0] = -self.nums[0][0]
        if self.negy.get() == 1:
            self.nums[0][1] = -self.nums[0][1]
        print self.nums
        self.window.destroy()

    def loop(self):
        self.window.mainloop()

class TripWindow:
    def __init__(self):
        self.twindow = Tk()
        self.nums = None
        self.twindow.wm_title("Config")
        self.anglevar = DoubleVar()
        self.anglebox = Entry(self.twindow, width=6)
        self.startbtn = Button(self.twindow, text="start", command=self.exit)
        self.angleslider = Scale(self.twindow, from_=85.0, to=95.0, label="angle", variable=self.anglevar, digits=5, resolution=-1, command=self.update)
        self.angleslider.grid(column=0, row=0, columnspan=2)
        self.startbtn.grid(column=0, row=3)
        self.angleslider.set(90.01)
        self.anglebox.grid(column=0, row=1)
        self.anglebox.insert(0, 89.95)
        self.errlabel = Label(self.twindow, text="Must be a number", fg='red')

    def update(self, number):
        self.anglebox.delete(0, END)
        self.anglebox.insert(0, str(number))

    def getnums(self):
        return self.nums

    def exit(self):
        print self.anglebox.get()
        print type(self.anglebox.get())
        try:
            if float(self.anglebox.get()):
                self.nums = float(self.anglebox.get())
                self.twindow.destroy()
        except ValueError:
            self.errlabel.grid(column=0, row=2, columnspan=2)

    def loop(self):
        self.twindow.mainloop()

class inputWindow:
    def __init__(self):
        self.nums = None
        self.window = Tk()
        self.window.wm_title("Config")
        self.numberofballs = IntVar()
        self.maxspeedvar = IntVar()
        self.maxsizevar = IntVar()
        self.minsizevar = IntVar()
        self.statsvar = IntVar()
        self.startbtn = Button(self.window, text="Start", command=self.exit)
        self.ballsentry = Entry(self.window, width=6)
        self.maxsizeentry = Entry(self.window, width=6)
        self.minsizeentry = Entry(self.window, width=6)
        self.speedentry = Entry(self.window, width=6)
        self.errorlabel = Label(self.window, text="Minimum size must be\nsmaller than maximum size", fg='red')
        self.valerrorlabel = Label(self.window, text="Input must be positive numbers", fg='red')
        self.controllabel = Label(self.window, text="Space: Grab all\nF1: Show stats", fg='green')
        self.infobox = Checkbutton(self.window, text="Show stats", variable=self.statsvar, selectcolor='blue')
        self.ballslider = Scale(self.window,
                                orient=HORIZONTAL,
                                label="Number of balls:",
                                from_=1,
                                to=1000,
                                variable=self.numberofballs,
                                length=150,
                                command=self.updateballs)
        self.maxspeedslider = Scale(self.window,
                                    orient=HORIZONTAL,
                                    label="Max speed:",
                                    from_=1,
                                    to=20,
                                    variable=self.maxspeedvar,
                                    length=150,
                                    command=self.updatespeed)
        self.maxsizeslider = Scale(self.window,
                                    orient=HORIZONTAL,
                                    label="Max size(px):",
                                    from_=1,
                                    to=150,
                                    variable=self.maxsizevar,
                                   length=150,
                                   command=self.updatemax)
        self.minsizeslider = Scale(self.window,
                                    orient=HORIZONTAL,
                                    label="Min size(px):",
                                    from_=1,
                                    to=150,
                                    variable=self.minsizevar,
                                    length=150,
                                    command=self.updatemin)
        self.startbtn.grid(column=0, row=9)
        self.ballslider.grid(column=0, row=0, columnspan=2)
        self.ballsentry.grid(column=2, row=0)
        self.maxspeedslider.grid(column=0, row=1, columnspan=2)
        self.speedentry.grid(column=2, row=1)
        self.maxsizeslider.grid(column=0, row=3, columnspan=2)
        self.maxsizeentry.grid(column=2, row=3)
        self.minsizeentry.grid(column=2, row=5)
        self.minsizeslider.grid(column=0, row=5, columnspan=2)
        self.infobox.grid(column=0, row=6, columnspan=2)
        self.controllabel.grid(column=0, row=7)
        self.ballslider.set(500)
        self.maxspeedslider.set(10)
        self.maxsizeslider.set(50)
        self.minsizeslider.set(20)

    def updateballs(self, value):
        self.ballsentry.delete(0, END)
        self.ballsentry.insert(0, str(value))

    def updatemax(self, value):
        self.maxsizeentry.delete(0, END)
        self.maxsizeentry.insert(0, str(value))

    def updatemin(self, value):
        self.minsizeentry.delete(0, END)
        self.minsizeentry.insert(0, str(value))

    def updatespeed(self, value):
        self.speedentry.delete(0, END)
        self.speedentry.insert(0, str(value))

    def loop(self):
        self.window.mainloop()

    def exit(self):
        try:

            if int(self.minsizeentry.get()) > int(self.maxsizeentry.get()):
                self.nums = None
                if self.valerrorlabel.winfo_ismapped():
                    self.valerrorlabel.grid_remove()
                self.errorlabel.grid(column=0, row=8, columnspan=3)
            elif int(self.ballsentry.get()) > 0 and int(self.minsizeentry.get()) > 0 and int(self.maxsizeentry.get()) > 0 \
                    and int(self.speedentry.get()) > 0:
                self.nums = [int(self.ballsentry.get()),
                             int(self.minsizeentry.get()),
                             int(self.maxsizeentry.get()),
                             int(self.speedentry.get()),
                             int(self.statsvar.get())]
                self.window.destroy()
            else:
                if self.errorlabel.winfo_ismapped():
                    self.errorlabel.grid_remove()
                self.valerrorlabel.grid(column=0, row=8, columnspan=3)
        except ValueError:
            if self.errorlabel.winfo_ismapped():
                self.errorlabel.grid_remove()
            self.valerrorlabel.grid(column=0, row=8, columnspan=3)

    def getnums(self):
        return self.nums

class buttonImg:
    def __init__(self, xy, color, text):
        self.active = True
        self.text = text
        self.xpos = xy[0]
        self.ypos = xy[1]
        self.xy = xy
        self.color = color
        self.originalColor = color
        if self.color == "red":
            self.img = pygame.image.load("btnred.png")
        elif self.color == "green":
            self.img = pygame.image.load("btngreen.png")
        elif self.color == "blue":
            self.img = pygame.image.load("btnblue.png")
        elif self.color == "brown":
            self.img = pygame.image.load("btnbrown.png")
        elif self.color == "dgreen":
            self.img = pygame.image.load("btndgreen.png")
        self.size = self.img.get_rect()

        self.btntext = defont.render(text, True, skin)
        screen.blit(self.img, self.xy)
        screen.blit(self.btntext, [self.xy[0] - (self.btntext.get_rect()[2] / 2) + (self.size[2] / 2), self.xy[1] - (self.btntext.get_rect()[3] / 2) + (self.size[3] / 2)])

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def changeColor(self, color):
        self.color = color
        if self.color == "red":
            self.img = pygame.image.load("btnred.png")
        elif self.color == "green":
            self.img = pygame.image.load("btngreen.png")
        elif self.color == "blue":
            self.img = pygame.image.load("btnblue.png")
        elif self.color == "brown":
            self.img = pygame.image.load("btnbrown.png")
        elif self.color == "dgreen":
            self.img = pygame.image.load("btndgreen.png")
        self.update()

    def update(self):
        if self.active:
            screen.blit(self.img, self.xy)
            screen.blit(self.btntext, [self.xy[0] - (self.btntext.get_rect()[2] / 2) + (self.size[2] / 2), self.xy[1] - (self.btntext.get_rect()[3] / 2) + (self.size[3] / 2)])

    def hover(self):
        if pygame.mouse.get_pos()[0] > self.xy[0] and pygame.mouse.get_pos()[0] < self.xy[0] + self.size[2] and pygame.mouse.get_pos()[1] > self.xy[1] and pygame.mouse.get_pos()[1] < self.xy[1] + self.size[3]:
            return True
        else:
            return False

    def clicked(self):
        if pygame.mouse.get_pos()[0] > self.xy[0] and pygame.mouse.get_pos()[0] < self.xy[0] + self.size[2] and pygame.mouse.get_pos()[1] > self.xy[1] and pygame.mouse.get_pos()[1] < self.xy[1] + self.size[3] and pygame.mouse.get_pressed()[0]:
            return True
        else:
            return False

class ball:
    def __init__(self, xy, diameter, color, speed):
        self.colorchange = True
        self.xy = xy
        self.x = xy[0]
        self.y = xy[1]
        self.diameter = diameter
        self.radius = diameter / 2
        self.color = color
        self.speed = speed
        self.colorChangeAmount = (abs(self.speed[0]) + abs(self.speed[1])) / 2
        self.grabbed = False
        self.colorFlag = [random.randint(0, 1), random.randint(0, 1), random.randint(0, 1)]
        self.circle = pygame.draw.circle(screen, self.color, self.xy, self.radius)

    def rightclick(self):
        if pygame.mouse.get_pos()[0] > self.xy[0] - self.radius and pygame.mouse.get_pos()[0] < self.xy[0] + self.radius:
            if pygame.mouse.get_pos()[1] > self.xy[1] - self.radius and pygame.mouse.get_pos()[1] < self.xy[1] + self.radius:
                if pygame.mouse.get_pressed()[2]:
                    m = ModWindow(self)
                    m.loop()
                    self.mnums = m.getnums()
                    if self.mnums:
                        self.modify(self.mnums[0], self.mnums[1], self.mnums[2], self.mnums[3])

    def modify(self, speed, color, size, colormode):
        if colormode == 1:
            self.colorchange = True
        else:
            self.colorchange = False
        self.speed = speed
        self.color = color
        self.radius = size / 2
        self.update()

    def grabbed(self):
        self.xy[0] = pygame.mouse.get_pos()[0]
        self.xy[1] = pygame.mouse.get_pos()[1]
        return True

    def changeColorIncrement(self, number):
        self.colorChangeAmount = number

    def update(self):
        self.circle = pygame.draw.circle(screen, self.color, self.xy, self.radius)

    def move(self):
        self.xy[0] += self.speed[0]
        self.xy[1] += self.speed[1]

    def clicked(self):
        if pygame.mouse.get_pressed()[0] and pygame.mouse.get_pos()[0] > self.xy[0] - self.radius and pygame.mouse.get_pos()[0] < self.xy[0] + self.radius and pygame.mouse.get_pos()[1] > self.xy[1] - self.radius and pygame.mouse.get_pos()[1] < self.xy[1] + self.radius:
            return True
        else:
            return False

    def bounce(self):
        if self.xy[0] - self.radius < 1 and self.speed[0] < 0 or self.xy[0] + self.radius > 799 and self.speed[0] > 0:
            self.speed[0] = -self.speed[0]
        if self.xy[1] - self.radius < 1 and self.speed[1] < 0 or self.xy[1] + self.radius > 599 and self.speed[1] > 0:
            self.speed[1] = -self.speed[1]
    
    def colormode(self):
        # put this in main loop for cool colors
        # checks if it'll go outta range
        for inc in range(3):
            if self.colorFlag[inc]:
                if self.color[inc] + self.colorChangeAmount > 255:
                    self.colorFlag[inc] = 0
                    self.color[inc] = 255
            elif not self.colorFlag[inc]:
                if self.color[inc] - self.colorChangeAmount < 0:
                    self.colorFlag[inc] = 1
                    self.color[inc] = 0

            if self.colorFlag[inc]:
                self.color[inc] += self.colorChangeAmount
                # print self.color[inc] + self.colorChangeAmount

            else:
                self.color[inc] -= self.colorChangeAmount
                # print self.color[inc] - self.colorChangeAmount
                
class button:
    def __init__(self, xy, size, color, text):
        self.text = text
        self.xpos = xy[0]
        self.ypos = xy[1]
        self.xy = xy
        self.xsize = size[0]
        self.ysize = size[1]
        self.size = size
        self.color = color
        self.originalColor = color
        self.box = pygame.draw.rect(screen, self.color, [self.xpos, self.ypos, self.xsize, self.ysize])
        self.btntext = defont.render(text, True, white)
        screen.blit(self.btntext, [self.xy[0] - (self.btntext.get_rect()[2] / 2) + (self.size[0] / 2), self.xy[1] - (self.btntext.get_rect()[3] / 2) + (self.size[1] / 2)])

    def changeColor(self, color):
        self.color = color
        self.update()

    def mouseOver(self):
        if pygame.mouse.get_pos()[0] > self.xpos and pygame.mouse.get_pos()[0] < self.xpos + self.xsize:
            if pygame.mouse.get_pos()[1] > self.ypos and pygame.mouse.get_pos()[1] < self.ypos + self.ysize:
                self.color = blue
            else:
                self.color = self.originalColor
        else:
                self.color = self.originalColor

    def update(self):
        self.box = pygame.draw.rect(screen, self.color, [self.xpos, self.ypos, self.xsize, self.ysize])
        screen.blit(self.btntext, [self.xy[0] - (self.btntext.get_rect()[2] / 2) + (self.size[0] / 2), self.xy[1] - (self.btntext.get_rect()[3] / 2) + (self.size[1] / 2)])

    def clicked(self):
        if pygame.mouse.get_pressed()[0] and pygame.mouse.get_pos()[0] > self.xpos and pygame.mouse.get_pos()[0] < self.xpos + self.xsize:
            if pygame.mouse.get_pressed()[0] and pygame.mouse.get_pos()[1] > self.ypos and pygame.mouse.get_pos()[1] < self.ypos + self.ysize:
                self.color = red
        else:
            self.color = self.originalColor
            
class Drone:
    def __init__(self, xpos, ypos, width, height, speed):
        self.speed = speed
        self.xpos = xpos
        self.ypos = ypos
        self.width = width
        self.height = height
        self.item = pygame.draw.rect(screen, blue, [self.xpos, self.ypos, self.width, self.height])
        pygame.display.update()

    def move(self):
        if self.isInside():
            if pygame.mouse.get_pos()[0] > self.xpos:
                self.xpos += self.speed
                self.update()
            elif pygame.mouse.get_pos()[0] < self.xpos:
                self.xpos -= self.speed
                self.update()
            if pygame.mouse.get_pos()[1] > self.ypos:
                self.ypos += self.speed
                self.update()
            elif pygame.mouse.get_pos()[1] < self.ypos:
                self.ypos -= self.speed
                self.update()

    def update(self):
        self.item = pygame.draw.rect(screen, blue, [self.xpos, self.ypos, self.width, self.height])

    def isInside(self):
        if self.xpos >= 0 and self.xpos <= screen.get_width() - self.width + self.speed and self.ypos >= 0 and self.ypos <= 600 - self.height + self.speed:
            return True
        else:
            return False

##################
#  Player class  #
##################
class Player:
    def __init__(self, xpos, ypos, speed, image):
        self.xpos = xpos
        self.ypos = ypos
        self.speed = speed
        self.life = 3
        self.img = pygame.image.load(image).convert()
        self.imgrect = self.img.get_rect()
        
        self.width = self.imgrect[0]
        self.height = self.imgrect[1]
        screen.blit(self.img, self.imgrect)

    def moveleft(self):
        self.xpos = self.xpos - self.speed

    def moveright(self):
        self.xpos = self.xpos + self.speed

    def update(self):
        screen.blit(self.img, self.imgrect)

    def die(self):
        self.life -= 1
        return self.life

    #def fire(self):
        #bullet = Bullet
        
class BowlingBall:
    def __init__(self):
        self.bowlingballimg = pygame.image.load('Dudeism.png')
        self.size = self.bowlingballimg.get_rect()
        self.angle = 90
        self.pos = [400 - (self.size[2]/2), 0]

    def rotate(self, amount):
        self.bowlingballimg = rot_center(self.bowlingballimg, amount)
        screen.blit(self.bowlingballimg, self.pos)

    def update(self):
        screen.blit(self.bowlingballimg, self.pos)
#class Bullet(color, speed, size, pos)
# FUNCTION DEFINITIONS

def text(msg, color, tx, ty):
    scrtext = defont.render(msg, True, color)
    screen.blit(scrtext, [tx, ty])
def rot_center(image, angle):
    """rotate an image while keeping its center and size"""
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image
def dudeballs(numballs, minsize, maxsize, maxspeed, showstats):
    grabbedBall = list()
    graball = False
    addballbutton = buttonImg([30, 530], 'green', "+ Add Ball")
    removeballbutton = buttonImg([addballbutton.xy[0] + 180, addballbutton.xy[1]], 'red', "- Remove Ball")

    for b in range(numballs):
        grabbedBall.append(None)

    # creation of ball objects
    balls = list()
    screen.fill(black)
    for i in range(numballs):
        xb = random.randint(1, 799)
        yb = random.randint(1, 599)
        randsize = random.randint(minsize, maxsize)
        randSpeed = [random.randint(-maxspeed, maxspeed), random.randint(-maxspeed, maxspeed)]
        while randSpeed == [0, 0]:
            randSpeed = [random.randint(-maxspeed, maxspeed), random.randint(-maxspeed, maxspeed)]
        balls.append(None)
        balls[i] = ball([xb, yb], randsize, [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)], randSpeed)
        print "Generated ball " + str(i)
        pygame.display.update()

    over = False
    # MAIN GAME LOOP
    while not over:
        # Handle user events first of all
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    over = True
                if event.key == pygame.K_F1:
                    if not showstats:
                        showstats = True
                    else:
                        showstats = False
                if event.key == pygame.K_SPACE:
                    graball = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    graball = False

        screen.fill(black)

        for x in range(numballs):
            balls[x].move()
            balls[x].bounce()
            if balls[x].colorchange:
                balls[x].colormode()
            balls[x].rightclick()
            balls[x].update()

            # if ball is clicked
            if balls[x].clicked():
                balls[x].grabbed = True
                grabbedBall[x] = balls[x]
            else:
                balls[x].grabbed = False
            if grabbedBall[x] and pygame.mouse.get_pressed()[0] or grabbedBall[x] and graball:
                grabbedBall[x].xy[0] = pygame.mouse.get_pos()[0]
                grabbedBall[x].xy[1] = pygame.mouse.get_pos()[1]
            else:
                grabbedBall[x] = None
            if graball:
                balls[x].grabbed = True
                grabbedBall[x] = balls[x]

        # PRINT STATS
        if showstats:
            text('Balls: ' + str(numballs), white, 10, 10)
            text('Ball pos: ' + str(balls[0].xy), white, 10, 30)
            text('Ball rgb: ' + str(balls[0].color), white, 10, 50)
            text('Ball speed: ' + str(balls[0].speed), white, 10, 70)
            text('Ball size: ' + str(balls[0].radius), white, 10, 90)
            text('Grabbed: ' + str(balls[0].grabbed), white, 10, 110)
            text('Cursor Pos: ' + str(pygame.mouse.get_pos()), white, 10, 130)
            text('Mouse1: ' + str(pygame.mouse.get_pressed()), white, 10, 150)
            text('all grabbed: ' + str(graball), white, 10, 170)
            addballbutton.update()
            removeballbutton.update()
            if addballbutton.hover():
                addballbutton.changeColor("dgreen")
                if addballbutton.clicked():
                    print 'click click'
                    numballs += 1
                    balls.append(None)
                    grabbedBall.append(None)
                    balls[-1] = ball([400, 300], 150, [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)], [0, 0])
            else:
                addballbutton.changeColor("green")

            if removeballbutton.hover():
                removeballbutton.changeColor("dgreen")
                if removeballbutton.clicked():
                    if numballs > 1:
                        print len(balls)
                        balls.pop
                        numballs -= 1
                        grabbedBall.pop()

            else:
                removeballbutton.changeColor("red")
        pygame.display.update()
        clock.tick(FPS)
def trip(angle):
    done = False
    bowl = BowlingBall()
    stats = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True
                if event.key == pygame.K_F1:
                    if stats:
                        stats = False
                        print stats
                    else:
                        stats = True
                        print stats

        screen.fill(white)
        bowl.rotate(angle)
        if stats:
            text('Value: ' + str(angle), black, 10, 10)
        bowl.update()
        pygame.display.update()
def menu():
    begin = False
    startbtn = buttonImg([100, 250], "brown", 'Play Ball')
    tripbtn = buttonImg([startbtn.xy[0], startbtn.xy[1] + 60], "brown", 'Trip Out')
    exitbtn = buttonImg([startbtn.xy[0], startbtn.xy[1] + 120], "red", 'Exit')
    while not begin:
        screen.blit(titleimg, [0, 0])
        startbtn.update()
        tripbtn.update()
        exitbtn.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    trip()

        if startbtn.hover():
            startbtn.changeColor("dgreen")
            if startbtn.clicked():
                w = inputWindow()
                w.loop()
                print w.getnums()
                if w.getnums():
                    dudeballs(w.getnums()[0], w.getnums()[1], w.getnums()[2], w.getnums()[3], w.getnums()[4])
        else:
            startbtn.changeColor("brown")

        if tripbtn.hover():
            tripbtn.changeColor("dgreen")
            if tripbtn.clicked():
                tw = TripWindow()
                tw.loop()
                if tw.getnums():
                    trip(tw.getnums())
        else:
            tripbtn.changeColor("brown")

        if exitbtn.hover():
            exitbtn.changeColor("dgreen")
            if exitbtn.clicked():
                pygame.quit()
                quit()
        else:
            exitbtn.changeColor("red")

        pygame.display.update()
        clock.tick(FPS)
menu()
#t = threading.Thread(target=menu)
#t.start()

# If DudeTech reaches a point where it is dynamically sized, it becomes DudeTech Evolved.
# make tk windows start in middle of screen
# create fields on window so button at bottom can be centered properly
# threading for live modification support!
# entry boxes for mod window
# improve add/remove ball buttons, 1 click 1 ball
