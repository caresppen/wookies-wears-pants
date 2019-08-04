#Space Invaders - Part 9
#Completed game program
#Python 3.7 on Windows

import turtle
import math
import random
import winsound

#Set up the screen
wn = turtle.Screen()
wn.setup(800, 700)
wn.bgcolor('black')
wn.title('Space Invaders')
wn.bgpic('C:\\@Carlos\\Courses\\Python Essential Training\\Exercise Files\\Extra\\Space Invaders\\space_invaders_background.gif')

#Register the shapes
turtle.register_shape('C:\\@Carlos\\Courses\\Python Essential Training\\Exercise Files\\Extra\\Space Invaders\\player.gif')
turtle.register_shape('C:\\@Carlos\\Courses\\Python Essential Training\\Exercise Files\\Extra\\Space Invaders\\invader.gif')

#Draw a border
border_pen = turtle.Turtle()

border_pen.speed(0)
border_pen.color('green')

border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()

border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

#Set the score to 0
score = 0
#Draw score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color('green')
score_pen.penup()
score_pen.setposition(-290, 270)
scorestring = 'Score: %s' %score
score_pen.write(scorestring, False, align='left', font=('Arial', 14,'normal'))
score_pen.hideturtle()

#Create the player turtle
player = turtle.Turtle()

player.color('blue')
# player.shape('triangle')
player.shape('C:\\@Carlos\\Courses\\Python Essential Training\\Exercise Files\\Extra\\Space Invaders\\player.gif')

player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerspeed = 10

#Create the player's bullet
bullet = turtle.Turtle()

bullet.color('yellow')
bullet.shape('triangle')

bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 20

#Define bullet state
#ready - ready to fire
#fire - bullet is firing
bulletstate = 'ready'

#Choose a number of enemies
number_of_enemies = 5
#Create an empty list of enemies
enemies = []

#Add enemies to the list
for i in range(number_of_enemies):
    #Create the enemy --> append function adds the enemies at the end of the list
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.color('red')
    # enemy.shape('circle')
    enemy.shape('C:\\@Carlos\\Courses\\Python Essential Training\\Exercise Files\\Extra\\Space Invaders\\invader.gif')
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)  # (-220, -200) to an easy GAME OVER. (100, 250) as DEFAULT
    enemy.setposition(x, y)

enemyspeed = 1.5

#Move the player left and right + bullet movement
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)

def fire_bullet():
    #Declare bulletstate as global if it needs changed
    global bulletstate
    if bulletstate == 'ready':
        winsound.PlaySound('C:\\@Carlos\\Courses\\Python Essential Training\\Exercise Files\\Extra\\Space Invaders\\laser.wav', winsound.SND_ASYNC)
        bulletstate = 'fire'
        #Move the bullet to the just above the player
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()

def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if distance < 15:
        return True
    else:
        return False

#Create keyboard bindings
turtle.listen()
turtle.onkeypress(move_left, 'Left')
turtle.onkeypress(move_right, 'Right')
turtle.onkey(fire_bullet, 'space')

#Main game loop
while True:

    for enemy in enemies:
        #Move the enemy
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        #Move the enemy back and down
        if enemy.xcor() > 280:
            #Move all the enemies down
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            #Change enemy direction
            enemyspeed *= -1
        
        if enemy.xcor() < -280:
            #Move all the enemies down
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            #Change enemy direction
            enemyspeed *= -1
        
        #Check for a collision between the bullet and the enemy
        if isCollision(bullet, enemy):
            winsound.PlaySound('C:\\@Carlos\\Courses\\Python Essential Training\\Exercise Files\\Extra\\Space Invaders\\explosion.wav', winsound.SND_ASYNC)
            #Reset the bullet
            bullet.hideturtle()
            bulletstate = 'ready'
            bullet.setposition(0, -400)
            #Reset the enemy
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(x, y)
            #Update the score
            score += 10
            scorestring = 'Score: %s' %score
            score_pen.clear()
            score_pen.write(scorestring, False, align='left', font=('Arial', 14,'normal'))

        #Check for a collision between the enemy and the player --> GAME OVER
        if isCollision(enemy, player):
            winsound.PlaySound('C:\\@Carlos\\Courses\\Python Essential Training\\Exercise Files\\Extra\\Space Invaders\\explosion.wav', winsound.SND_ASYNC)
            player.hideturtle()
            for en in enemies:
                en.hideturtle()
            go = 'GAME OVER'
            print(f'{go}')
            score_pen.clear()
            score_pen.setposition(0, 0)
            score_pen.write(go, False, align='center', font=('None', 20,'bold'))
            break
    
    #Move the bullet
    if bulletstate == 'fire':
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    #Check to see if the bullet has reached the top
    if bullet.ycor() > 275 and bulletstate == 'fire':
        bullet.hideturtle()
        bulletstate = 'ready'


turtle.done()
