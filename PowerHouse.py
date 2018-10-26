import pygame
import os
import time
from Bricks import Brick
from BricksPositions import *
from Texts import *
from Constants import *

#Makes the 'PyGame' window of a specific size: (display_x, display_y)
gameDisplay = pygame.display.set_mode((display_x, display_y))

#Opens the 'PyGame' window at a specific position on the screen
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" %(window_posi_x, window_posi_y)
os.environ['SDL_VIDEO_CENTERED'] = '0'

#Setting Game Caption and the Game Icon
pygame.display.set_caption('Smokin\' Ball')
icon = pygame.image.load('Icon.png')
pygame.display.set_icon(icon)

#To control the 'Frames Per Second' of the game
clock = pygame.time.Clock()

#To control the 'held' keys, by repeating the event by the amount of delay and interval time mentioned
pygame.key.set_repeat(1,30)       

#Initialising Font type and their size
pygame.font.init()
font = pygame.font.SysFont("comicsansms", 20)
smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)

#Defining a class to make 'Buttons'
class Buttons:
    def __init__ (self, message, x, y, width, height, inactive_colour, active_colour, action = None):
        self.message = message
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.inactive_colour = inactive_colour
        self.active_colour = active_colour
        self.action = action

    def createButton(self):
        cursor = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        #To check if cursor is poinitng to the button
        if (self.x < cursor[0] < (self.x + self.width)) and (self.y < cursor[1] < (self.y + self.height)):
            pygame.draw.rect(gameDisplay, self.active_colour, (self.x, self.y, self.width, self.height))
            
            #To check if the button is being "Left Clicked" on a particular action
            if click[0] == 1 and self.action != None:
                if self.action == "Exit":
                    pygame.quit()
                    quit()

                elif self.action == "Play":
                    gameLoop()

                elif self.action == "Guidance":
                    info_screen()
                
                if self.action == "Back":
                    start_screen()
        
        else:
            pygame.draw.rect(gameDisplay, self.inactive_colour, (self.x, self.y, self.width, self.height))  #Shaping the "Button" as a Rectangle
         
        button_message (self.message, black, self.x, self.y, self.width, self.height)

#To print messages on the screen
def screen_message(text, colour, y_displace = 0, size = "small"):
    text1 = Texts(text, colour, size)
    textSurface, textRect = text1.text_objects()
    textRect.center = (display_x / 2) , (display_y / 2) + y_displace
    gameDisplay.blit(textSurface, textRect) 

#To print messages on the button
def button_message(text, colour, button_x, button_y, button_width, button_height, size = "small"):
    text1 = Texts(text, colour, size)
    textSurface, textRect = text1.text_objects()
    textRect.center = (button_x + (button_width / 2)), (button_y + (button_height / 2))
    gameDisplay.blit(textSurface, textRect)

#Defining the "Start Screen"
def start_screen():
    
    start = True
    
    while start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(black)
        
        screen_message("Smokin\' Ball!", red, -150, "large")
        screen_message("Are you ready to smash?", white, 50, "medium")

        #Creating 'Buttons' on the Start Screen
        button1 = Buttons("Play", 100, 500, 100, 50, royalblue, blue, action = "Play")
        button1.createButton()
        button2 = Buttons("Guidance", 350, 500, 100, 50, royalblue, blue, action = "Guidance")
        button2.createButton()
        button3 = Buttons("Exit", 600, 500, 100, 50, royalblue, blue, action = "Exit")
        button3.createButton()

        pygame.display.update()
        clock.tick(20)
    
#Defining the "Info Screen"
def info_screen():
    
    info = True
    
    while info:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(black)
        screen_message("Directions:", red, -250, "large")
        screen_message("To move the panel right : Right Arrow Key", yellow, -150)
        screen_message("To move the panel left : Left Arrow Key", yellow, -100 )
        screen_message("(Press 'P' to pause the game.)", white, -50)
        screen_message("Objective:", red, 50, "large")
        screen_message("Destroy all the bricks without losing all the lives.", yellow, 150)
        screen_message("Save the Smokin\' Ball, by the Slider,", green, 200)
        screen_message("from diving out of the bottom of the screen.", green, 250)

        #Creating 'Button' on the Info Screen        
        button1 = Buttons("Go Back", 20, 530, 100, 50, royalblue, blue, action = "Back")
        button1.createButton()

        pygame.display.update()
        clock.tick(20)

#Defining a function to display the score
def display_score(count):
    scores = font.render("Score: "+ str(count), True, blue)
    gameDisplay.blit(scores, (20,10))

#Defining a function to display the lives
def display_lives(lives):
    life = font.render("Lives: "+ str(lives), True, blue)
    gameDisplay.blit(life, (690,10))

#Defining the "Pause Screen"
def pause_screen():
    
    pause = True
    
    screen_message("Game Paused!", white, -100, size = "large")
    screen_message("Press C to 'Continue' ", green, 25, size = "small")
    screen_message("(or)", green, 100, size = "small")
    screen_message(" Press Q to 'Quit'", green, 175, size = "small")
    pygame.display.update()
    clock.tick(20)
    
    while pause:
        #Event Handling to see what the user presses 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    pause = False
                    
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        clock.tick(5)

#Defining the "Game Complete Screen" 
def game_complete(count):
    
    pause = True
    
    gameDisplay.fill(yellow)
    screen_message("Congratulations!", black, -150, size = "large")
    screen_message("That was a splendid victory.", white, 0, size = "medium")  
    screen_message("Be a sport and press 'Play' again!", white, 80, size = "medium")
    display_score(count)    
    pygame.display.update()
    clock.tick(5)
        
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        #Creating 'Buttons' on the Game Complete Screen
        button1 = Buttons("Play", 300, 500, 100, 50, royalblue, blue, action = "Play")
        button1.createButton()
        button2 = Buttons("Exit", 500, 500, 100, 50, royalblue, blue, action = "Exit")
        button2.createButton()

        pygame.display.update()
        clock.tick(20)

#Defining the "Game Over Screen"
def game_over(gameOver):

    pause = True
        
    if gameOver:
        gameDisplay.fill(red)
        screen_message("Game over!", black, -200, size = "large")
        screen_message("Never give up, stop melting down,", white, -75, size = "small")
        screen_message("and stop grieving!", white, -25, size = "small")
        screen_message("Be a sport and press 'Play' again!", green, 100, size = "medium")
        pygame.display.update()
        
        while pause:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            
            #Creating 'Buttons' on the Game Over Screen
            button1 = Buttons("Play", 280, 500, 100, 50, royalblue, blue, action = "Play")
            button1.createButton()
            button2 = Buttons("Exit", 470, 500, 100, 50, royalblue, blue, action = "Exit")
            button2.createButton()

            pygame.display.update()
            clock.tick(20)

#Defining the main "Game Loop"
def gameLoop():

    global gameOver

    #Uploading the Sprites 
    slider = pygame.image.load('Slider.png').convert()
    sliderRect = slider.get_rect()        #Stating it a 'Rect' object for better and effortless operations
    sliderRect = sliderRect.move((display_x / 2) - (width_slider / 2), display_y - height_slider)
    
    smokeyBall = pygame.image.load('SmokeyBall.png').convert()
    smokeyBallRect = smokeyBall.get_rect()       #Stating it a 'Rect' object for better and effortless operations
    smokeyBallRect = smokeyBallRect.move((display_x / 2) - radius_smokeyBall,  (display_y - (height_slider + (2 * radius_smokeyBall) + 5)))
    
    #Initialising the SmokeyBall's speed
    ball_x_speed = ball_x_init
    ball_y_speed = ball_y_init

    #Defining a "State" for better handling
    on_paddle = 1

    #Initialising important 'game' variables
    count = 0
    lives = 3
    
    gameExit = False
    gameOver = False
    
    #To form a list of "Brick" class elements and get their positions
    brickList = []
    bricks = createBricks()
    for y in range(len(bricks)):
        for x in range(len(bricks[y])):
            if(bricks[y][x] == 1):
                brickList.append(Brick(x * 30,y * 20, red))

    #To form a list of "Rect" objects            
    brick_rect_list = []
    for brick in brickList:
        brick_rect_list.append(brick.make_rects(gameDisplay))
                    
    while not gameExit:

        game_over(gameOver)
        
        #Event Handling of the 'Slider' and the 'Smokey Ball'
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if on_paddle:
                        smokeyBallRect = smokeyBallRect.move(ball_x_speed, ball_y_speed)
                        on_paddle = 0
                        
                if event.key == pygame.K_LEFT:
                    sliderRect = sliderRect.move(-slider_x_speed, 0)
                    
                    if (sliderRect.left < 0):
                        sliderRect.left = 0
                        
                    if on_paddle:
                        smokeyBallRect = smokeyBallRect.move(-slider_x_speed, 0)
                        if smokeyBallRect.left < 0:
                            smokeyBallRect.left = 0

                elif event.key == pygame.K_RIGHT:
                    sliderRect = sliderRect.move(slider_x_speed, 0)

                    if (sliderRect.right > display_x):
                        sliderRect.right = display_x

                    if on_paddle:
                        smokeyBallRect = smokeyBallRect.move(slider_x_speed, 0)
                        if smokeyBallRect.right > display_x:
                            smokeyBallRect.right = display_x

                elif event.key == pygame.K_p:
                    pause_screen()
                    
        #Physics behind the collision between 'Slider' and the 'Smokey Ball'    
        if (smokeyBallRect.left <= sliderRect.right) and (smokeyBallRect.right >= sliderRect.left) and (smokeyBallRect.top <= sliderRect.bottom) and (smokeyBallRect.bottom >= sliderRect.top):

            ball_y_speed = -ball_y_speed

            #Difference between the 'x' co-ordinates of the 'Slider' and the 'Smokey Ball'
            off_position = smokeyBallRect.center[0] - sliderRect.center[0] 
            
            #Handling speed of the bounced 'Smokey Ball'
            if (off_position > 0):

                if off_position > 40: 
                    ball_x_speed += 3

                if off_position > 25: 
                    ball_x_speed += 0

                if off_position > 10: 
                    ball_x_speed += -3
            else:
                
                if off_position < -40: 
                    ball_x_speed += 3

                if off_position < -25: 
                    ball_x_speed += 0

                if off_position < -10: 
                    ball_x_speed += -3

        #Physics behind the collision between 'Bricks' and the 'Smokey Ball'            
        for brick in brick_rect_list:
            
            if (smokeyBallRect.left <= brick.right) and (smokeyBallRect.right >= brick.left) and (smokeyBallRect.top <= brick.bottom) and (smokeyBallRect.bottom >= brick.top):
                i = brick_rect_list.index(brick)
                brick_rect_list.remove(brick) 
                brickList.pop(i) #Removing the "Broken" brick from the list of 'Bricks'
                ball_y_speed = -ball_y_speed
                
                count += 5
                
                #Difference between the 'x' co-ordinates of the 'Brick' and the 'Smokey Ball'
                off_position = smokeyBallRect.center[0] - brick.center[0] 
                
                #Handling speed of the bounced 'Smokey Ball'
                if (off_position > 0): 

                    if off_position > 10: 
                        ball_x_speed += 1

                    if off_position > 5: 
                        ball_x_speed += 0

                    if off_position > 2: 
                        ball_x_speed += -1
                else:

                    if off_position < -10: 
                        ball_x_speed += 1

                    if off_position < -5: 
                        ball_x_speed += 0

                    if off_position < -2: 
                        ball_x_speed += -1

        #Condition to make the 'Smokey Ball' stay on the Game screen    
        if smokeyBallRect.left < 0 or smokeyBallRect.right > display_x:
                    ball_x_speed = -ball_x_speed                

        if smokeyBallRect.top < 0:
                    ball_y_speed = -ball_y_speed    
        
        #Conditional if the 'Smokey Ball' hits the bottom of the screen and then restarting the game after losing a life
        if smokeyBallRect.bottom > display_y:
            
            lives -= 1

            #Displaying the 'Slider' and the 'Smokey Ball' back to their original position after losing a life
            sliderRect.center = display_x / 2 , display_y - (height_slider / 2)
            smokeyBallRect.center = display_x / 2 , display_y - (height_slider + (radius_smokeyBall) + 5)

            ball_x_speed = ball_x_init
            ball_y_speed = ball_y_init

            on_paddle = 1       #Changing the 'State' of the 'Smokey Ball'

            if lives == 0:
                gameOver = True

        #Display "Game Complete" Screen if all the bricks are "Broken"      
        if brickList == []:
            game_complete(count)
        
        if not on_paddle:
            smokeyBallRect = smokeyBallRect.move (ball_x_speed, ball_y_speed)            
                    
        gameDisplay.fill(black)
        screen_message("Smoking Kills", yellow, -185, size = "medium")

        #To reposition the "image" of the sprites with the help of 'Destination' argument 
        gameDisplay.blit(slider, sliderRect)
        gameDisplay.blit(smokeyBall, smokeyBallRect)
        
        #Presenting the Bricks on the Game Screen
        for brick in brickList:
            brick.render(gameDisplay)

        #Displayig the Game variables                
        display_score(count)
        display_lives(lives)

        if on_paddle:
            screen_message("Press 'Space Bar' to launch", white, 100, size = "medium")
            
        pygame.display.update()             #Updating the Game Screen
        clock.tick(30)              #Controlling the 'Frames Per Second'

    pygame.quit()
    quit()

if __name__ == "__main__":
    start_screen()
    

