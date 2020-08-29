###############################
###### Snack Time! ############
###### By Sarah Ahmed #########
###### May 1st, 2020 ##########
###############################

from tkinter import *
from time import *
from math import *
from random import *
tk = Tk()
backgroundColour = "#6c6c6c"
screen = Canvas(tk, width=600,height=600,background= backgroundColour)
screen.pack()
floor = screen.create_rectangle(0,510, 600,600, fill = "#525252", outline = "#525252")






#######################
#####POPCORN MACHINE###
#######################

#box
box = screen.create_rectangle(50,115, 250,450, fill = "#c61800", outline = "#c61800")
boxDetail1 = screen.create_rectangle(52,125, 248,130, fill = "#e5e4e4",
                                     width = 2.5, outline = "#f2b55b")
boxDetail2 = screen.create_rectangle(52,345, 248,350, fill = "#e5e4e4",
                                     width = 2.5, outline = "#f2b55b")
boxDetail3 = screen.create_rectangle(52,435, 248,440, fill = "#e5e4e4",
                                     width = 2.5, outline = "#f2b55b")
x1 = 58
x2 = 70
for boxKnob in range(8):
    screen.create_oval(x1,365, x2,375, fill = "#e5e4e4", outline = "#e5e4e4")
    x1 = x1 + 23
    x2 = x2 + 23

boxLeftLeg = screen.create_rectangle(50,450, 70,510, fill = "#c61800", outline = "#c61800")
boxRightLeg = screen.create_rectangle(235,450, 245,480, fill = "#c61800", outline = "#c61800")

#popcorn sign
sign = screen.create_rectangle(90,390, 210,420, fill = "#f2b55b",
                               outline = "#e5e4e4", width = 5)

text = screen.create_text(150, 405, text = "POPCORN", font = "Arial 17")

#handle
handle = screen.create_polygon(250,360, 300,360, 250,400, fill = "#c61800")
handleDetail = screen.create_rectangle(250,356, 300,360, fill = "black", outline = "black")

#roof/lid
roof = screen.create_rectangle(40,95, 260,110, fill = "#c61800", outline = "#c61800")

roofDetailA = []
for i in range(8):
    roofDetailA.append(0)

x1 = 47 
x2 = 60
x3 = 73
for roofDetail in range(8):
    roofDetailA[roofDetail] = screen.create_polygon(x1,95, x2,100, x3,95, fill = "#e5e4e4",
                          outline = "#f2b55b", width = 1)
    x1 = x1 + 26
    x2 = x2 + 26
    x3 = x3 + 26


#screen/interior
window = screen.create_rectangle(60,150, 240,335, fill = backgroundColour,
                                 outline = backgroundColour)
popcornPopper1 = screen.create_line(150,150, 150,180, fill = "#333333",
                                    width = 5)
popcornPopper2 = screen.create_oval(140,160, 160,180, fill = "#333333",
                                    outline = "#333333")
popcornPopper3 = screen.create_rectangle(120,175, 180,195, fill = "#333333",
                                         outline = "#333333")

#wheel
wheelOuter = screen.create_oval(200,430, 280,520, width = 5)
wheelLine1 = screen.create_line(200,475, 280,475, width = 5)
wheelLine2 = screen.create_line(240,430, 240,520, width = 5)
wheelLine3 = screen.create_line(212,442, 268,508, width = 5)
wheelLine4 = screen.create_line(212,508, 268,442, width = 5)
wheelInner = screen.create_oval(235,470, 245,480, fill = "darkorange1",
                                outline = "firebrick4", width = 5)







#########
###CAT###
#########

n = 1
for f in range(44):
    #head
    head = screen.create_oval(400 - n*f,180, 500- n*f,280, fill = "#323232", outline = "#323232")
    earLeft = screen.create_polygon(400- n*f,230, 410- n*f,160, 420- n*f,200, fill = "#323232",
                                    outline = "#323232")
    earRight = screen.create_polygon(480- n*f,230, 490- n*f,160, 500- n*f,230, fill = "#323232",
                                    outline = "#323232")

    leftWhisker1 = screen.create_line(420- n*f,230, 380- n*f,220, width = 3, fill = "#323232")
    leftWhisker2 = screen.create_line(420- n*f,230, 382- n*f,230, width = 3, fill = "#323232")
    leftWhisker3 = screen.create_line(420- n*f,230, 384- n*f,240, width = 3, fill = "#323232")


    rightWhisker1 = screen.create_line(480- n*f,230, 520- n*f,220, width = 3, fill = "#323232")
    rightWhisker2 = screen.create_line(480- n*f,230, 522- n*f,230, width = 3, fill = "#323232")
    rightWhisker3 = screen.create_line(480- n*f,230, 524- n*f,240, width = 3, fill = "#323232")
    hat = screen.create_rectangle(425- n*f,160, 475- n*f,190, fill = "#c11701", outline = "#c11701")

    #face
    leftEye = screen.create_oval(410- n*f,210, 435- n*f,235, fill = "#ececec", outline = "#ececec")
    rightEye = screen.create_oval(460- n*f,210, 485- n*f,235, fill = "#ececec", outline = "#ececec")
    mouth = screen.create_oval(435- n*f,235, 455- n*f,255, fill = "#878588", outline = "#878588")
    nose = screen.create_oval(440- n*f,240, 448- n*f,248, fill = "#141315", outline = "#141315")
    lips = screen.create_polygon(440- n*f,253, 444- n*f,248, 448- n*f,253, fill = "#141315", outline = "#141315")
    leftPupil = screen.create_oval(415- n*f,215, 427- n*f,227, fill = "#070707", outline = "#070707")
    rightPupil = screen.create_oval(465- n*f,215, 477- n*f,227, fill = "#070707", outline = "#070707")

    #torso
    leftArm = screen.create_line(420- n*f,290, 400- n*f,400, fill = "#323232", width = 10)
    rightArm = screen.create_line(480- n*f,290, 500- n*f,400, fill = "#323232", width = 10)
    shirt = screen.create_rectangle(420- n*f,280, 480- n*f,380, fill = "#c11701", outline = "#c11701")
    bottom = screen.create_rectangle(420- n*f,380, 480- n*f,420, fill = "#323232", outline = "#323232")
    buttonTL = screen.create_oval(425- n *f,310, 435-n*f,320, fill = "#e5e4e4", outline = "#e5e4e4")
    buttonBL = screen.create_oval(425- n *f,330, 435-n*f,340, fill = "#e5e4e4", outline = "#e5e4e4")
    buttonTR = screen.create_oval(445- n *f,310, 455-n*f,320, fill = "#e5e4e4", outline = "#e5e4e4")
    buttonBR = screen.create_oval(445- n *f,330, 455-n*f,340, fill = "#e5e4e4", outline = "#e5e4e4")


    #lower
    legLeft = screen.create_rectangle(420- n*f,380, 435- n*f,510, fill = "#323232", outline = "#323232")
    legRight = screen.create_rectangle(465- n*f,380, 480- n*f,510, fill = "#323232", outline = "#323232")
    tail = screen.create_line(470- n*f,400, 540- n*f,480, fill = "#323232", width = 10)

    screen.update()
    sleep(0.03)
    screen.delete(head, earLeft, earRight, leftWhisker1, leftWhisker2, leftWhisker3,
                  rightWhisker1, rightWhisker2, rightWhisker3, leftEye, rightEye, mouth, nose, lips, leftPupil, rightPupil
                  , leftArm, rightArm, shirt, bottom, legLeft, legRight, tail, hat, buttonTL, buttonBL, buttonTR, buttonBR)

f = 44
#head
head = screen.create_oval(400 - n*f,180, 500- n*f,280, fill = "#323232", outline = "#323232")
earLeft = screen.create_polygon(400- n*f,230, 410- n*f,160, 420- n*f,200, fill = "#323232",
                                outline = "#323232")
earRight = screen.create_polygon(480- n*f,230, 490- n*f,160, 500- n*f,230, fill = "#323232",
                                outline = "#323232")

leftWhisker1 = screen.create_line(420- n*f,230, 380- n*f,220, width = 3, fill = "#323232")
leftWhisker2 = screen.create_line(420- n*f,230, 382- n*f,230, width = 3, fill = "#323232")
leftWhisker3 = screen.create_line(420- n*f,230, 384- n*f,240, width = 3, fill = "#323232")


rightWhisker1 = screen.create_line(480- n*f,230, 520- n*f,220, width = 3, fill = "#323232")
rightWhisker2 = screen.create_line(480- n*f,230, 522- n*f,230, width = 3, fill = "#323232")
rightWhisker3 = screen.create_line(480- n*f,230, 524- n*f,240, width = 3, fill = "#323232")
hat = screen.create_rectangle(425- n*f,160, 475- n*f,190, fill = "#c11701", outline = "#c11701")

#face
leftEye = screen.create_oval(410- n*f,210, 435- n*f,235, fill = "#ececec", outline = "#ececec")
rightEye = screen.create_oval(460- n*f,210, 485- n*f,235, fill = "#ececec", outline = "#ececec")
mouth = screen.create_oval(435- n*f,235, 455- n*f,255, fill = "#878588", outline = "#878588")
nose = screen.create_oval(440- n*f,240, 448- n*f,248, fill = "#141315", outline = "#141315")
lips = screen.create_polygon(440- n*f,253, 444- n*f,248, 448- n*f,253, fill = "#141315", outline = "#141315")
leftPupil = screen.create_oval(415- n*f,215, 427- n*f,227, fill = "#070707", outline = "#070707")
rightPupil = screen.create_oval(465- n*f,215, 477- n*f,227, fill = "#070707", outline = "#070707")

#torso
leftArm = screen.create_line(420- n*f,290, 400- n*f,400, fill = "#323232", width = 10)
rightArm = screen.create_line(480- n*f,290, 500- n*f,400, fill = "#323232", width = 10)
shirt = screen.create_rectangle(420- n*f,280, 480- n*f,380, fill = "#c11701", outline = "#c11701")
bottom = screen.create_rectangle(420- n*f,380, 480- n*f,420, fill = "#323232", outline = "#323232")
buttonTL = screen.create_oval(425- n *f,310, 435-n*f,320, fill = "#e5e4e4", outline = "#e5e4e4")
buttonBL = screen.create_oval(425- n *f,330, 435-n*f,340, fill = "#e5e4e4", outline = "#e5e4e4")
buttonTR = screen.create_oval(445- n *f,310, 455-n*f,320, fill = "#e5e4e4", outline = "#e5e4e4")
buttonBR = screen.create_oval(445- n *f,330, 455-n*f,340, fill = "#e5e4e4", outline = "#e5e4e4")

#lower
legLeft = screen.create_rectangle(420- n*f,380, 435- n*f,510, fill = "#323232", outline = "#323232")
legRight = screen.create_rectangle(465- n*f,380, 480- n*f,510, fill = "#323232", outline = "#323232")
tail = screen.create_line(470- n*f,400, 540- n*f,480, fill = "#323232", width = 10)        


#arm moving to turn on machine
screen.delete(leftArm)

leftArm2 = screen.create_line(420-n*f,290, 295,350, fill = "#323232", width = 10)












#####################
###GRADUAL POPCORN###
#####################

numGradual = 25

#####LEFT SIDE GRADUAL#####
numFirstLeft = numGradual

#gradual popping left side
firstLeft = []
xLeft = []
yLeft = []
launchGradual = []
xLeftSpeeds = []
yUpSpeeds = []
sizes = []


#colour
popcornColours = "#fbfbfb"

#filling the gradual popping arrays of the left side
for i in range(numFirstLeft):
    xLeft.append(130)
    yLeft.append(170)
    firstLeft.append(0)
    launchGradual.append(randint(0,numFirstLeft))
    xLeftSpeeds.append(uniform(-0.8, -0.75))
    yUpSpeeds.append(uniform(2.5, 3))
    sizes.append(randint(4, 7))


#####RIGHT SIDE GRADUAL#####
numFirstRight = numGradual

#gradual popping right side
firstRight = []
xRight = []
yRight = []
launchGradual = []
xRightSpeeds = []
yUpSpeeds = []
sizes = []

#filling the gradual popping arrays of the right side
for i in range(numFirstRight):
    xRight.append(170)
    yRight.append(170)
    firstRight.append(0)
    launchGradual.append(randint(0, numGradual))
    xRightSpeeds.append(uniform(0.8, 2))
    yUpSpeeds.append(uniform(2, 4))
    sizes.append(randint(4, 7))

pop = 0

### ANIMATION OF POPCORN GRADUALLY POPPING ###
for f in range(100):
    for i in range(0, numGradual):
        if f >= launchGradual[i]:
            #LEFT SIDE ANIMATION
            xLeft[i] = xLeftSpeeds[i]*pop + xLeft[i]
            yLeft[i] = 0.25*pop**2 - (yUpSpeeds[i]*pop) + yLeft[i]
            firstLeft[i] = screen.create_oval(xLeft[i], yLeft[i], xLeft[i] + sizes[i],
                                yLeft[i] + sizes[i], fill = popcornColours,
                                outline = popcornColours)
            pop = pop + 1

            if yLeft[i] <= 155 or yLeft[i] >= 325 or xLeft[i] <= 65 or pop > 22:
                xLeft[i] = 130
                yLeft[i] = 170

            #RIGHT SIDE ANIMATION
            xRight[i] = xRightSpeeds[i]*pop + xRight[i]
            yRight[i] = 0.25*pop**2 - (yUpSpeeds[i]*pop) + yRight[i]
            firstRight[i] = screen.create_oval(xRight[i], yRight[i], xRight[i] + 5,
                                yRight[i] + 5, fill = popcornColours,
                                outline = popcornColours)
            pop = pop + 1
            if pop > 30:
                pop = 0
                xRight[i] = 170
                yRight[i] = 170

            if yRight[i] + sizes[i] >= 325:
                xRight[i] = 170
                yRight[i] = 170

            if xRight[i] + sizes[i] <= 235:
                xRight[i] = 170
                yRight[i] = 170

            #FILLING UP ANIMATION
            if f > 50:
                fillPopcorn = []
                xFill = []
                yFill = []
                for i in range(1):
                    xFill.append(randint(65,235))
                    yFill.append(randint(150,330))
                    fillPopcorn.append(0)
                for i in range(1):
                    fillPopcorn[i] = screen.create_oval(xFill[i], yFill[i], xFill[i] + 6,
                                                        yFill[i] + 6, fill = popcornColours,
                                                        outline = popcornColours)
            
    screen.update()
    sleep(0.03)
        
    for i in range(0, numGradual):
        screen.delete(firstLeft[i], firstRight[i])












#######################
###EXPLOSION POPCORN###
#######################

###ARM###
#arm back to original position
screen.delete(leftArm2)
f =44
leftArm = screen.create_line(420- n*f,290, 400- n*f,400, fill = "#323232", width = 10)


###TOP DOOR OPENING###
# deleting the old roof
screen.delete(roof, roofDetailA[0], roofDetailA[1], roofDetailA[2],
              roofDetailA[3], roofDetailA[4], roofDetailA[5], roofDetailA[6],
              roofDetailA[7])

#redrawing the new roof
roof = screen.create_polygon(30,95, 30,110, 250,85, 250,70, fill = "#c61800", outline = "#c61800")
x1 = 30
y1 = 95
x2 = 43
y2 = 100
x3 = 56
y3 = 93
for roofDetail in range(8):
    roofDetailA = screen.create_polygon(x1,y1, x2,y2, x3,y3, fill = "#e5e4e4",
                          outline = "#f2b55b", width = 1)
    x1 = x1 + 26
    x2 = x2 + 26
    x3 = x3 + 26
    y1 = y1 - 3
    y2 = y2 - 3
    y3 = y3 - 3


###PREPARING TO FEAST###
#opening mouth
openMouth = screen.create_oval(370,230, 440,275, fill = "#db8988", outline = "#db8988")
teethL = screen.create_polygon(385,235, 387,240, 389,232, fill = "#f4f4f4", outline = "#f4f4f4")
teethR = screen.create_polygon(425,233, 427,240, 429,235, fill = "#f4f4f4", outline = "#f4f4f4")

#closing eyes
screen.delete(leftEye, leftPupil, rightEye, rightPupil)
happyEyeLL = screen.create_line(410 - n*f,225, 422 - n*f,205, fill = "#070707", width = 6)
happyEyeLR = screen.create_line(422 - n*f,205, 435-n*f,225, fill = "#070707", width = 6)
happyEyeRL = screen.create_line(460 - n*f,225, 472 - n*f,205, fill = "#070707", width = 6)
happyEyeRR = screen.create_line(472 - n*f,205, 485-n*f,225, fill = "#070707", width = 6)


###POPCORN FLYING OUT###
numOut = 150

#empty arrays
outPopcorn = []
xOut = []
yOut = []
launchOut = []
xOutSpeeds = []
yOutSpeeds = []
sizesOut = []

#filling the arrays
for i in range(numOut):
    xOut.append(randint(100, 250))
    yOut.append(115)
    launchOut.append(randint(0, numOut))
    xOutSpeeds.append(uniform(3, 5))
    yOutSpeeds.append(uniform(2, 4))
    sizesOut.append(randint(5,8))
    outPopcorn.append(0)

#animation
numEaten = 0
pop = 0
for f in range(120):
    #expression changes to distressed
    if f == 80:
        screen.delete(happyEyeLL, happyEyeLR, happyEyeRR, happyEyeRL)
        eyeCloseLT = screen.create_line(366,205, 391,217, fill = "#070707", width = 6)
        eyeCloseLB = screen.create_line(366,230, 391,215, fill = "#070707", width = 6)
        eyeCloseRT = screen.create_line(416,217, 441,205, fill = "#070707", width = 6)
        eyeCloseRB = screen.create_line(416,215, 441,230, fill = "#070707", width = 6)

     #popcorn launches out of machine   
    for i in range(0, numOut):
        if f >= launchOut[i]:
            xOut[i] = xOutSpeeds[i]*pop + xOut[i]
            yOut[i] = 0.25*pop**2 - (yOutSpeeds[i]*pop) + yOut[i]

            outPopcorn[i] = screen.create_oval(xOut[i], yOut[i], xOut[i] + sizesOut[i],
                                yOut[i] + sizesOut[i], fill = popcornColours,
                                outline = popcornColours)
            pop = pop + 1

            #popcorn is recycled until otherwise noted
            if f <= 105:
                if yOut[i] >= 600:
                    xOut[i] = 150
                    yOut[i] = 115
                    pop = 0

            #if popcorn lands in cats mouth, expand stomach, arms, tail and buttons
            if 370 < xOut[i] < 440 and 230 < yOut[i] < 275:
                xOut[i] = 150
                yOut[i] = 115
                numEaten = numEaten + 1

                x1 = 376
                x2 = 436
                y2 = 420
                xLeftArm = 356
                xRightArm = 456
                xTail = 496
                x1ButtonTBL = 381
                y2ButtonTT = 320
                x1ButtonTBR = 401
                y2ButtonBB = 340
                x2ButtonTBL = 391
                y1ButtonTT = 310
                y1ButtonBB = 330
                x2ButtonTBR = 411
                
                if x1 >= 305:
                    x1 = x1 - numEaten
                    x2 = x2 + numEaten
                    y2 = y2 + numEaten
                    xLeftArm = xLeftArm - numEaten
                    xRightArm = xRightArm + numEaten
                    xTail = xTail + numEaten
                    x1ButtonTBL = x1ButtonTBL - numEaten*0.2
                    x2ButtonTBL = x2ButtonTBL - numEaten*0.2
                    x1ButtonTBR = x1ButtonTBR + numEaten*0.2
                    x2ButtonTBR = x2ButtonTBR +numEaten*0.2
                else:
                    y2 = y2 + numEaten
                    xLeftArm = xLeftArm - numEaten
                    xRightArm = xRightArm + numEaten
                    xTail = xTail + numEaten

                leftArmA = screen.create_line(376,290, xLeftArm,400, fill = "#323232", width = 10)
                rightArmA = screen.create_line(436, 290, xRightArm,400, fill = "#323232", width = 10)
                shirt = screen.create_rectangle(x1, 280, x2,380, fill = "#c11701", outline = "#c11701")
                bottom = screen.create_rectangle(x1,380, x2,y2, fill = "#323232", outline = "#323232")
                tailA = screen.create_line(426,400, xTail,480, fill = "#323232", width = 10)

                buttonTL = screen.create_oval(x1ButtonTBL,y1ButtonTT, x2ButtonTBL,y2ButtonTT, fill = "#e5e4e4", outline = "#e5e4e4")
                buttonBL = screen.create_oval(x1ButtonTBL,y1ButtonBB, x2ButtonTBL,y2ButtonBB, fill = "#e5e4e4", outline = "#e5e4e4")
                buttonTR = screen.create_oval(x1ButtonTBR,y1ButtonTT, x2ButtonTBR,y2ButtonTT, fill = "#e5e4e4", outline = "#e5e4e4")
                buttonBR = screen.create_oval(x1ButtonTBR,y1ButtonBB, x2ButtonTBR,y2ButtonBB, fill = "#e5e4e4", outline = "#e5e4e4")

    
    screen.update()
    sleep(0.03)

    for i in range(0, numOut):
        screen.delete(outPopcorn[i])    



########################
#### POST - POPCORN ####
########################

###BLINKING IN SURPRISE###
screen.delete(openMouth, teethL, teethR, eyeCloseLT, eyeCloseLB, eyeCloseRT, eyeCloseRB)

#redrawing the original expression
f = 44
leftEye = screen.create_oval(410- n*f,210, 435- n*f,235, fill = "#ececec", outline = "#ececec")
rightEye = screen.create_oval(460- n*f,210, 485- n*f,235, fill = "#ececec", outline = "#ececec")
mouth = screen.create_oval(435- n*f,235, 455- n*f,255, fill = "#878588", outline = "#878588")
nose = screen.create_oval(440- n*f,240, 448- n*f,248, fill = "#141315", outline = "#141315")
lips = screen.create_polygon(440- n*f,253, 444- n*f,248, 448- n*f,253, fill = "#141315", outline = "#141315")
leftPupil = screen.create_oval(417- n*f,215, 429- n*f,227, fill = "#070707", outline = "#070707")
rightPupil = screen.create_oval(467- n*f,215, 479- n*f,227, fill = "#070707", outline = "#070707")

#blinking
f = 44
for blink in range(3):
    screen.update()
    sleep(0.5)
    screen.delete(leftEye, leftPupil, rightEye, rightPupil)

    eyeCloseLT = screen.create_line(410- n*f,205, 435- n*f,217, fill = "#070707", width = 6)
    eyeCloseLB = screen.create_line(410- n*f,230, 435- n*f,215, fill = "#070707", width = 6)
    eyeCloseRT = screen.create_line(460- n*f,217, 485- n*f,205, fill = "#070707", width = 6)
    eyeCloseRB = screen.create_line(460- n*f,215, 485- n*f,230, fill = "#070707", width = 6)

    screen.update()
    sleep(0.5)
    screen.delete(eyeCloseLT, eyeCloseLB, eyeCloseRT, eyeCloseRB)
    
    leftEye = screen.create_oval(410- n*f,210, 435- n*f,235, fill = "#ececec", outline = "#ececec")
    rightEye = screen.create_oval(460- n*f,210, 485- n*f,235, fill = "#ececec", outline = "#ececec")
    leftPupil = screen.create_oval(417- n*f,215, 429- n*f,227, fill = "#070707", outline = "#070707")
    rightPupil = screen.create_oval(467- n*f,215, 479- n*f,227, fill = "#070707", outline = "#070707")
