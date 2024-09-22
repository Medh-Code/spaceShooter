#Imports
import turtle as trtl
import random as rand
import time


#Functions

def enemy_setup():
    global enemies
    enemy_img = r"""C:\Users\NTTDATA\OneDrive\Programs_Codes\CSE_HW_LESSONS\TurtleSection2\turtle_graphics_proj\enemy.gif"""

    wn.tracer(0) #Begins tracer

    #Creates 6 enemy ships and places them into a list
    for i in range(6):
        enemy = trtl.Turtle()
        
        enemy.pu()
        enemy.setheading(270)
        enemy.goto(0,400)
        enemy.speed(4)
        
        wn.addshape(enemy_img)
        enemy.shape(enemy_img)
        
        enemies.append(enemy)

    wn.tracer(1) #Ends tracer, resulting in a shorter wait time for the program to make the 6 enemy ships

#Firing and Collision
def user_shoot():
    global score
    global explosion
    global enemy_img
    global enemies
    
    #User's missile goes to user ship position
    user_missile.speed("fastest") # Setting to fastest allows the missile to immediately go to the user ship's position, decreasing the possible distance from missile to ship from continued user inputs
    user_missile.goto(user.xcor(),user.ycor())
    user_missile.st()
    user_missile.speed("normal") # Resets missile speed to normal 
    
    while user_missile.ycor() < 400:  # the user missile goes forward 7, then the program checks if the missile has hit any enemy ship 
        user_missile.fd(7)

        for ship in enemies: #Checks collision with each enemy ship and the user missile with the turtles (enemy ships) in the list "enemies" until there is a collsion or has checked every ship

            if (abs(user_missile.xcor()-ship.xcor()) < 25 and abs(user_missile.ycor() - ship.ycor()) < 25):
                user_missile.ht()
                ship.shape(explosion) #The enemy ship that has collided with the missile will change to an explosion image
                time.sleep(0.5) #Waits for half a seconf with the explosion image
                ship.ht() #Hides the ship
                del enemies[enemies.index(ship)] #Deletes the ship from the list "enemies"
                
                score += 1 #Adds 1 to the score
                write() #The scribe turtle writes the new score
                break #Breaks out of the for loop if there is a collision
        
        else: #If the collision condition is not met after checking all ships, then the user missile will keep going forward as he while loop is run again
            continue

        break #If there is a collision, then this break exits the while loop as well, ending the function whenever there is a collision.
        
    user_missile.ht() #hides the user's missile

def enemy_shoot():
    global lives
    global enemies
    global enemy_speed_mult

    ship = rand.choice(enemies) # picks a random enemy ship from the list "enemies" to determine which ship will shoot at the user
    
    enemy_missile.goto(ship.xcor(),ship.ycor()) #Returns the enemy missile to the coordinates of the chosen ship 
    enemy_missile.st()

    while enemy_missile.ycor() > -400: # Allows for collision checking until the enemy missile hits the end of the map
        enemy_missile.fd(10 * enemy_speed_mult) #increases missile speed every round

        #Collision checking each time the enemy missile moves forward
        if abs(enemy_missile.xcor() - user.xcor()) <= 28 and abs(enemy_missile.ycor() - user.ycor()) <= 28:
            lives -= 1 #Removes one of the user's lives
            user.shape(explosion) #Replaces the user's ship image with an explosion
            time.sleep(0.5) #Keeps the image for half a second
            user.shape(user_img) #Returns back to the orrginal user ship image
            write() #Scribe turtle updates the user's lives
            break #Ends the while loop since the collision has occured
    
    enemy_missile.ht() #Hides the missile

#Movement
def enemy_move():
    global enemies

    for ship in enemies: #hides all surviving turtle images
        ship.ht()

    enemies = [] #Resets the enemies list

    enemy_setup() #Adds 6 new enemy ships

    for ship in enemies: #moves every ship in the enemies list to a random position on the screen
        ship.st()
        ship.goto(rand.randint(-220,220), rand.randint(50,350))

#User Movement
def up(): #Moves user up
    user.fd(10)

def down(): #Moves user down
    user.bk(10)

def left(): #Moves user left
    user.goto(user.xcor()-10, user.ycor())

def right(): #Moves user right
    user.goto(user.xcor()+10, user.ycor())

def up_right(): #Moves user forward at heading 45
    user.goto(user.xcor()+10,user.ycor()+10)

def down_right(): #moves user forward at heading 315
    user.goto(user.xcor()+10,user.ycor()-10)

def up_left(): #Moves user forward at heading 135
    user.goto(user.xcor()-10,user.ycor()+10)

def down_left(): #moves user forward at heading 225
    user.goto(user.xcor()-10,user.ycor()-10)

#Score and Lives
def write(): #Updates the user's score and lives
    scribe.clear()
    scribe.write(f"Score: {score} Lives remaining: {lives}", font= ("Courier", 15, "bold"), align = "center")

#Timer     
def elapsed_time(start, end): #Calculates time survived from the start of the game to the end in seconds
    elap = end - start
    return round(elap)

#Setup
wn = trtl.Screen()
wn.setup(height = 700, width = 500) #Screen size set to 700*500 pixels
wn.bgpic(r"""C:\Users\NTTDATA\OneDrive\Programs_Codes\CSE_HW_LESSONS\TurtleSection2\turtle_graphics_proj\starbackground.png""") # Background set to a custom spacebackground

wn.tracer(0) #Begin tracer to make the setup portion of the code faster and seamless

    #Global Variables
score = 0 #User's score from enemy kills
lives = 3 #How many times the user can get hit unti the game ends
enemy_speed_mult = 1 #Base multiplier for the enemy's missile speed
game_start = time.time() #initilaizes the start time of the game 
enemies = [] #Initializes enemies as an empty list

    #Explosion Setup
explosion = r"""C:\Users\NTTDATA\OneDrive\Programs_Codes\CSE_HW_LESSONS\TurtleSection2\turtle_graphics_proj\explosion.gif"""
wn.addshape(explosion) #Adds explosion image for later use during collisions

    #User ship setup
user = trtl.Turtle()
user.pu()
user.setheading(90)

user_img = r"""C:\Users\NTTDATA\OneDrive\Programs_Codes\CSE_HW_LESSONS\TurtleSection2\turtle_graphics_proj\user.gif"""
wn.addshape(user_img)
user.shape(user_img)

user.goto(0,-200)
    
    #Enemy Ships setup
enemy_setup()
    
    #User Shots Setup
user_missile = trtl.Turtle()
user_missile.setheading(90)
user_missile.pu()

user_shot_img = r"""C:\Users\NTTDATA\OneDrive\Programs_Codes\CSE_HW_LESSONS\TurtleSection2\turtle_graphics_proj\user_bullet.gif"""
wn.addshape(user_shot_img)
user_missile.shape(user_shot_img)

user_missile.ht()

    #Enemy Shots setup
enemy_missile = trtl.Turtle()
enemy_missile.pu()
enemy_missile.setheading(270)

enemy_shot_img = r"""C:\Users\NTTDATA\OneDrive\Programs_Codes\CSE_HW_LESSONS\TurtleSection2\turtle_graphics_proj\enemy_bullet.gif"""
wn.addshape(enemy_shot_img)
enemy_missile.shape(enemy_shot_img)

enemy_missile.ht()

    #Scribe Setup
scribe = trtl.Turtle()
scribe.ht()
scribe.pu()
scribe.color("white")
scribe.goto(0,-400)


wn.tracer(1) #Ends the tracer creating a faster and more seamless startup


#Active Code
while True:
    
    #Events
    wn.listen() #Listen for any key inputs

    trtl.onkeypress(up, "w")
    trtl.onkeypress(down, "s")
    trtl.onkeypress(right, "d")
    trtl.onkeypress(left, "a")
    trtl.onkeypress(up_right, "e")
    trtl.onkeypress(up_left, "q")
    trtl.onkeypress(down_right, "c")
    trtl.onkeypress(down_left, "z")
    
    wn.update()

    enemy_move() #Enemy moves while the program listens for key inputs
    
    #Enemies shoot 4 times randomly at the user while checking if the user has reached the score of 20 or has lost all of their lives
    for i in range(4):
        enemy_shoot()
        
        if lives == 0 or score == 20:
            break
        
        user_shoot()
        enemy_speed_mult += 0.5 #Increases the enemies missile speed
    
    #This else is used to continue the while loop if the conditions in the for loop are not met and the for loop is broken
    else:
        continue

    break


#Events after the user loses or wins
end = time.time() #Sets the end time

#Hides user and enemy turtles on the screen
user.ht()
for ship in enemies:
    ship.ht()
user_missile.ht()
enemy_missile.ht()

#Sets the scribe to write the final result of the game
scribe.clear()
scribe.goto(0,0)

#Winning Event
if score >= 20:
    scribe.color("green")
    scribe.write(f"     YOU WON!\n   Time: {elapsed_time(game_start, end)} seconds", font = ("Cuorier", 30, "bold"), align = "center")

#Losing Event
else:
    scribe.color("red")
    scribe.write(f"     YOU LOST!\n      Score: {score}\n  Time: {elapsed_time(game_start, end)} seconds", font = ("Arial", 30, "bold"), align = "center")

#Waits for 3 seconds until quitting the program with a thank you message
time.sleep(3)
quit("Thank you for playing!")

wn.mainloop()