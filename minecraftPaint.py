#---------Welcome to Minecraft Pixel Art-------------#
#-----  If you would like to load an image, please---#
#----- run it again as I cannot find a way to do it--#
#----- in a single run. This program is based off of-#
#------------the famous game "minecraft".------------#
#----------------Enjoy the program!------------------#
from pygame import *
from random import *
from glob import *
init()       
#mixer.music.load("songs/Epicsax.mp3")
#mixer.music.play()
screen = display.set_mode((1049,788)) 
background = image.load("Background/background2.jpg").convert() #Loads the main picture, which is the background.
pig = image.load("pig.png").convert_alpha()#--------------|
cow = image.load("cow.png").convert_alpha()#--------------|
sheep = image.load("sheep.png").convert_alpha()#----------|
creeper = image.load("creeper.png").convert_alpha()#------| These will load the stamp images.
zombie = image.load("zombie.png").convert_alpha()#--------|
steve = image.load("steve.png").convert_alpha()#----------|
canvasRect = Rect(0,237,699,549)
tool = ""
running = True
screen.blit(background,(0,0))
colour = (0,0,0)
#This function will get the name of the picture that was drawn into the canvasRect area.
def getName():
    ans = ""                    # final answer will be made one letter at a time.
    arialFont = font.SysFont("Times New Roman", 16)
    back = screen.copy()        #This line will copy the screen so once it's done it will replace it.
    textArea = Rect(5,5,200,25) # make changes here.
    
    pics = glob("*.bmp")+glob("*.jpg")+glob("*.png") #all the types of accessible picture formats.
    n = len(pics) 
    choiceArea = Rect(textArea.x,textArea.y+textArea.height,textArea.width,n*textArea.height)
    typing = True
    while typing:
        for e in event.get():
            if e.type == QUIT:
                event.post(e)   # puts QUIT back in event list so main quits
                return ""
            if e.type == KEYDOWN:
                if e.key == K_BACKSPACE:    #Tries to remove the last letter when the user uses the back space.
                    if len(ans)>0:
                        ans = ans[:-1]
                elif e.key == K_KP_ENTER or e.key == K_RETURN : 
                    typing = False
                elif e.key < 256:
                    ans += e.unicode       # add character to ans ; a counter       
        txtPic = arialFont.render(ans, True, (0,0,0))   #
        draw.rect(screen,(220,255,220),textArea)        # draw the text window and the text.
        draw.rect(screen,(0,0,0),textArea,2)            #
        screen.blit(txtPic,(textArea.x+3,textArea.y+2)) 
        
        display.flip()     
    screen.blit(back,(0,0))
    return ans
filename = ""

#~~~~Event Loop~~~~
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
        if e.type == MOUSEBUTTONDOWN:
            copy = screen.copy()
            ox,oy = mx,my

    
    mb = mouse.get_pressed()
    mx,my = mouse.get_pos()
    x,y = mouse.get_pos()
    print (x,y)
#~~~~Determining the tool~~~~
    if mb[0] == 1: #If they left click, continue.
        if Rect(698,234,92,82).collidepoint(x,y): #if then click in the pencil tool area, continue.
            tool = 'pencil' #Set tool to 'pencil'.
            print("pencil") #This tests if it works. You can see it in the python shell.
#The rest of this section do that same, it only runs if you click within the tool section, including the stamp section.
        elif Rect(698,316,92,82).collidepoint(x,y): 
            tool = 'eraser'
            print("eraser")
        elif Rect(698,400,92,41).collidepoint(x,y):
            tool = 'ellipsesFilled'
            print("ellipsesFilled")
        elif Rect(698,441,92,41).collidepoint(x,y):
            tool = 'ellipsesHollow'
            print("ellipsesHollow")
        elif Rect(698,482,92,41).collidepoint(x,y):
            tool = 'rectangleFilled'
            print("rectanglefilled")
        elif Rect(698,526,92,41).collidepoint(x,y):
            tool = 'rectangleHollow'
            print("rectangleHollow")
        elif Rect(698,565,92,82).collidepoint(x,y):
            tool = 'line'
            print("line")
        elif Rect(698,649,92,82).collidepoint(x,y):
            tool = 'save'
            print("save")
        elif Rect(698,718,92,82).collidepoint(x,y):
            tool = 'load'
            print("load")
        elif Rect(790,179,90,69).collidepoint(x,y):
            tool = 'text'
            print("text")
        elif Rect(504,0,180,114).collidepoint(x,y):
            tool = 'sheep'
            print ("Sheep")
        elif Rect(685,0,181,114).collidepoint(x,y):
            tool = 'cow'
            print ("cow")
        elif Rect(868,0,179,114).collidepoint(x,y):
            tool = 'pig'
            print ("pig")
        elif Rect(505,118,179,114).collidepoint(x,y):
            tool = 'zombie'
            print("zombie")
        elif Rect(686,118,180,114).collidepoint(x,y):
            tool = 'creeper'
            print("creeper")
        elif Rect(868,118,179,114).collidepoint(x,y):
            tool = 'steve'
            print("steve")
        elif Rect (792,719,91,68).collidepoint(x,y):
            tool = 'spraypaint'
            print ("spraypaint")
        elif Rect(796,450,250,169).collidepoint(x,y): # Determines the first colour. If they click within the colour scheme, continue.
            print(screen.get_at((x,y))) #Tests it out by printing the colour into the python shell.
            colour = screen.get_at((x,y)) #This sets a variable to what the first colour is set.
            print(colour) #tests to see if this variable works. Not needed unless you need to test something.
            draw.rect(screen,colour,(828,264,94,87)) #This is an extra part. Similar to microsoft paint, it will draw a rectangle that corresponds to the first colour.
    elif mb[2] == 1: #If they right click, continue.
        if Rect(796,450,250,169).collidepoint(x,y): #If they click within the colour scheme, continue. 
            print(screen.get_at((x,y))) #Test
            colour2 = screen.get_at((x,y)) #sets the second variable for the right-clicked colour.
            print(colour2) #Test
            draw.rect(screen,colour2,(921,348,94,86)) #draws the rectangle that corresponds to the second colour.
#------Stamps------
    if tool == 'pig': #If they click the pig stamp, continue.
        if Rect(0,236,698,549).collidepoint(x,y):
            if mb[0] == 1: #If they left click, continue.
                screen.blit(copy,(0,0)) #This line will copy the screen so once it's done it will replace it. Needed if you need to hold the button to drag the stamp.
                screen.set_clip(canvasRect) #It will allow the program to not allow any stamps to go over the canvas.
                screen.blit(pig,(mx-100,my-106)) #adds the picture, the coords shows where exactly the mouse will be when they click.
#Same for the rest of the stamps.
    if tool == 'cow':
        if Rect(0,236,698,549).collidepoint(x,y):
            if mb[0] == 1:
                screen.blit(copy,(0,0))
                screen.set_clip(canvasRect)
                screen.blit(cow,(mx-85,my-100))
    if tool == 'sheep':
        if Rect(0,236,698,549).collidepoint(x,y):
            if mb[0] == 1:
                screen.blit(copy,(0,0))
                screen.set_clip(canvasRect)
                screen.blit(sheep,(mx-100,my-100))
    if tool == 'creeper':
        if Rect(0,236,698,549).collidepoint(x,y):
            if mb[0] == 1:
                screen.blit(copy,(0,0))
                screen.set_clip(canvasRect)
                screen.blit(creeper,(mx-93,my-130))
    if tool == 'zombie':
        if Rect(0,236,698,549).collidepoint(x,y):
            if mb[0] == 1:
                screen.blit(copy,(0,0))
                screen.set_clip(canvasRect)
                screen.blit(zombie,(mx-75,my-126))
    if tool == 'steve':
        if Rect(0,236,698,549).collidepoint(x,y):
            if mb[0] == 1:
                screen.blit(copy,(0,0))
                screen.set_clip(canvasRect)
                screen.blit(steve,(mx-86,my-110))
#~~~~~~SprayPaint~~~~~~~
    if tool == 'spraypaint': #If they click within the tool area, continue.
        if mb[0] == 1: #If they left click, continue.
            for i in range (200): # This can determine the speed of the spray. The lower the number, the slower. 
                x = randint(mx-30,mx+30) #sets variables to be where ever, as long as less than or equal to 30.
                y = randint(my-30,my+30)
                dist =(((mx - x)**2 + (my - y)**2)**0.5) #distance formula.
                if Rect(0,236,698,549).collidepoint(x,y): #If the click within the canvas, continue.
                    if dist <=30: #If the distance is within 30, draw the circle(s).
                        draw.circle(screen,colour,(x,y),0)
        if mb[2] == 1 : #Same but with the second colour
            for i in range (200):
                x = randint(mx-30,mx+30)
                y = randint(my-30,my+30)
                dist =(((mx - x)**2 + (my - y)**2)**0.5)
                if Rect(0,236,698,549).collidepoint(x,y):
                    if dist <=30:
                        draw.circle(screen,colour2,(x,y),0)
#~~~~~~Pencil~~~~~~~both colours
    if tool == 'pencil':#If they click within the tool area, continue.
        if mb[0] == 1:
            if Rect(0,236,698,549).collidepoint(x,y):
                draw.line(screen,colour,(mx,my),(omx,omy),1) #draws a line from oldx and oldy to mx and my (the newest ones). It does this until the user stops.
        if mb[2] == 1:
            if Rect(0,236,698,549).collidepoint(x,y):
                draw.line(screen,colour2,(mx,my),(omx,omy),1)

#~~~~~~Eraser~~~~~~~ Draws thick white lines, acting as an eraser.
    if tool == 'eraser':#If they click within the tool area, continue.
        if mb[0] == 1:
            if Rect(0,236,698,549).collidepoint(x,y):
                screen.set_clip(canvasRect)
                draw.line(screen,(255,255,255),(mx,my),(omx,omy),15)
#~~~~~~~LINE~~~~~~~~~both colours
    if tool == 'line':#If they click within the tool area, continue.
        if mb[0] == 1:
            if Rect(0,236,698,549).collidepoint(x,y):
                screen.blit(copy ,(0,0))
                draw.line(screen,colour,(ox,oy),(mx,my)) #draws a line from oldx and oldy to mx and my (the newest ones). It does this only once until the user stops.
        if mb[2] == 1:
            if Rect(0,236,698,549).collidepoint(x,y):
                screen.blit(copy ,(0,0))
                draw.line(screen,colour2,(ox,oy),(mx,my))
#------RectangleHollow-----both colours
    if tool == 'rectangleHollow':#If they click within the tool area, continue.
        if mb[0] == 1:
            if Rect(0,236,698,549).collidepoint(x,y):
                screen.blit(copy, (0,0))
                draw.rect(screen, colour, (ox,oy,mx-ox,my-oy),1) #draws a rectangle that corresponds to the areas where the user picks.
        if mb[2] == 1:
            if Rect(0,236,698,549).collidepoint(x,y):
                screen.blit(copy, (0,0))
                draw.rect(screen, colour2, (ox,oy,mx-ox,my-oy),1)
#------RectangleFilled-----both colours
    if tool == 'rectangleFilled':#If they click within the tool area, continue.
        if mb[0] == 1:
            if Rect(0,236,698,549).collidepoint(x,y):
                screen.blit(copy, (0,0))
                draw.rect(screen, colour, (ox,oy,mx-ox,my-oy)) #same as the hollow one, but it is filled, meaning there is no 4th part inside the brackets.
        if mb[2] == 1:
            if Rect(0,236,698,549).collidepoint(x,y):
                screen.blit(copy, (0,0))
                draw.rect(screen, colour2, (ox,oy,mx-ox,my-oy))
#------ellipses------ both colours
    if tool == 'ellipsesFilled':#If they click within the tool area, continue.
        if mb[0] == 1:
            if Rect(0,236,698,549).collidepoint(x,y):
                screen.blit(copy, (0,0))
                rect = Rect(ox,oy,mx-ox,my-oy) 
                rect.normalize()#correct negative sizes
                draw.ellipse(screen, colour,rect) #draws ellipses that correspond to where the user's coordinated are chosen.
        if mb[2] == 1:
            if Rect(0,236,698,549).collidepoint(x,y):
                screen.blit(copy, (0,0))
                rect = Rect(ox,oy,mx-ox,my-oy)
                rect.normalize()#corrects negative sizes
                draw.ellipse(screen,colour2,rect)
    if tool == 'ellipsesHollow':#If they click within the tool area, continue.
        if mb[0] == 1:
            if Rect(0,236,698,549).collidepoint(x,y):
                screen.blit(copy, (0,0))
                rect = Rect(ox,oy,mx-ox,my-oy)
                rect.normalize()#corrects negative sizes
                try:
                    draw.ellipse(screen, colour, rect, 1) #The "try:" will attempt to draw the ellipse
                except: pass #If the try fails, the except:pass will power through the code. Basically ignores the error.
                #The exception method is similar to an if and else method, yet can only be used in a very specific situation such as this one.
        if mb[2] == 1:
            if Rect(0,236,698,549).collidepoint(x,y):
                screen.blit(copy, (0,0))
                rect = Rect(ox,oy,mx-ox,my-oy)
                rect.normalize() #correct negative sizes
                try:
                    draw.ellipse(screen, colour2, rect, 1) #Same as before.
                except: pass
#------Save----------
    if tool == 'save':#If they click within the tool area, continue.
        txt = getName() #turns what the function returned into a variable
        image.save(screen.subsurface(canvasRect), "savedImages/"+txt) #saves the image to the folder.
        tool = "" #Lets it do it only once.
#------Load----------
    if tool == 'load':#If they click within the tool area, continue.
            filename = getName()
            file = image.load("savedImages/"+filename)
            w,h = file.get_width(), file.get_height() #gets the width and height or the image the user wants to load up.
            if w >= canvasRect[2] and h >= canvasRect[3]: #If it is too big, the following lines will scale it to be smaller.
                file = transform.scale(file, (canvasRect[2], canvasRect[3])) #When it's scaled, it will set the variable to a new w and h
            screen.blit(file, (canvasRect[0],canvasRect[1])) #puts the image into the canvas.
            tool = "" #Lets it do it only once.
    omx,omy = mx,my #oldx and oldy 
    display.flip() 
quit()
