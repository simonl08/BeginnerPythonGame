import turtle
import random
import pygame.mixer

score = 0
lives = 3
pygame.mixer.init()
pygame.mixer.music.load("Dragon_Quest_VIII_Overture.mp3")
pygame.mixer.music.play(-1)
wn = turtle.Screen() #This assign the wn the turtle screen command 
wn.title("Falling slimes")
wn.bgcolor("green") #This sets the background colour
wn.bgpic("bgv2.gif") #This sets the background image
wn.setup(width=800, height=600) #This sets the size of the window 800 width and 600 height
wn.register_shape("slime.gif")
wn.register_shape("coin.gif")
wn.register_shape("knight.gif")
wn.tracer(0) #This stops the automatic updates of the screen

# Creating the player (order of code matters here)
player = turtle.Turtle() #Turtle is the class name
player.speed(0) #This sets the drawing speed or animation speed NOT MOVEMENT SPEED
player.shape("knight.gif")
player.color("white")
player.penup() #This prevent the object from drawing lines when it moves
player.goto(0, -250) #(0, 0) is centre (0, 250) will position it at the bott
player.direction = "stop"

#Creating the list of item coins
itemCoins = [] #created an empty list for the coins

# Adding item coin
for i in range(12):
    itemCoin = turtle.Turtle() 
    itemCoin.speed(0) #This is a speed function
    itemCoin.shape("coin.gif")
    itemCoin.color("blue")
    itemCoin.penup() 
    itemCoin.goto(-100, 250)
    itemCoin.speed = random.uniform(0.8, 1) #the speed variable of which the coin falls randomly between 0.8&1
    itemCoins.append(itemCoin) #add more coins to the list 'itemCoins' which we made earlier

#Creating the list of slimes (enemies)
slimes = [] #created an empty list for the coins

# Adding slime
for i in range(12):
    slime = turtle.Turtle() 
    slime.speed(0) #This is a speed function
    slime.shape("slime.gif")
    slime.color("red")
    slime.penup() 
    slime.goto(100, 250)
    slime.speed = random.uniform(0.8, 1) #the speed variable of which the coin falls randomly between 0.8&1
    slimes.append(slime) #add more coins to the list 'itemCoins' which we made earlier

#Make the pen write the scoring and lives
pen = turtle.Turtle() 
pen.hideturtle()
pen.speed(0) 
pen.shape("square")
pen.color("white")
pen.penup()
pen.goto(0, 260) 
font = ("Courier", 24, "normal") # assign the type of font to use
pen.write("Score: {}  Lives: {}".format(score, lives), align="center", font=font) #Make the pen write score and lives

#Game Over text
over = turtle.Turtle() 
over.hideturtle()
over.speed(0) 
over.shape("square")
over.color("white")
over.penup()
over.goto(0, 0) 
font2 = ("Courier", 36, "normal") 

#Functions created here to move the player 
   
def go_left():
    player.direction = "left"
def go_right():
    player.direction = "right"

#User input with keyboard binding
wn.listen() #Telling the program to listen to keyboard inputs
wn.onkeypress(go_left,  "Left")  #onkeypress means if a key is pressed (Left arrow in this case)then do something
wn.onkeypress(go_right,  "Right")

#The main game loop
while True:
    #This update the screen at a time 
    wn.update()

    #Moving the players with user input
    if player.direction == "left":
        x = player.xcor() #This finds the current x coordinate of the player
        x -= 0.8 #This subtracts 0.8 from x (which is 0) making the pointer at -0.8x on the coordinate 
        player.setx(x)
    if player.xcor() <= -380: #Constrains the player within the game window based on the coordinates
        player.goto(-380,-250)
    
   
    if player.direction == "right":
        x = player.xcor() 
        x += 0.8 
        player.setx(x)
    if player.xcor() >= 380:
        player.goto(380,-250)
 

#Moving the coins for score
    for itemCoin in itemCoins: #for every itemCoint in the itemCoins list
        y = itemCoin.ycor() 
        y -= itemCoin.speed #makes the coin fall down the y axis at a random value between 0.8&1(declared earlier)
        itemCoin.sety(y)#This sets the position of the coin based on it's coordinate

        #Checks if the coin falls off the screen
        if y < -300: #if the coin is at the bottom of the screen (as height is set to 600)
            x = random.randint(-380, 380) #Introducing the random module
            y = random.randint(300, 400)
            itemCoin.goto(x, y)

        #Checking for coin collision with the player
        if itemCoin.distance(player) < 20: #if the item coin is 20px within the player
            x = random.randint(-380, 380) #spawns the coin randomly 
            y = random.randint(300, 400)
            itemCoin.goto(x, y)
            score += 1 #add one point for every collision with coin
            pen.clear()
            pen.write("Score: {}  Lives: {}".format(score, lives), align="center", font=font)

        if lives == 0:
            itemCoin.goto(0,420)
#Moving the slimes
    for slime in slimes: 
        y = slime.ycor() 
        y -= slime.speed 
        slime.sety(y)

        #Checks if the slime falls off the screen
        if y < -300: 
            x = random.randint(-380, 380) 
            y = random.randint(300, 400)
            slime.goto(x, y)

        #Checking for slime collision with the player
        if slime.distance(player) < 20: 
            x = random.randint(-380, 380) 
            y = random.randint(300, 400)
            slime.goto(x, y)
            lives -= 1 #Lose a life everytime you collide with slime
            pen.clear()
            pen.write("Score: {}  Lives: {}".format(score, lives), align="center", font=font)

        if lives == 0:
            pen.clear()
            over.write("GAME OVER", align="center", font=font2) 
            pen.write("Score: {}".format(score), align="center", font=font)
            slime.goto(0,420)
            player.goto(0,-250)
            player.direction = "stop"

#This will keep the game window opened
wn.mainloop()
