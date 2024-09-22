#Imports
import turtle as trtl
import random as rand
import time

#Functions

#Firing and Collision
def user_shoot():
    global score
    global explosion
    global enemy_img
    global ammo

    if len(ammo) != 0:  
        
        ammo.pop()
        user_missile.goto(user.xcor(),user.ycor())
        user_missile.st()
        
        while user_missile.ycor() < 400:  
            user_missile.fd(7)
            
            for ship in enemies:
                if (abs(user_missile.xcor()-ship.xcor()) < 25 and abs(user_missile.ycor() - ship.ycor()) < 25):
                    user_missile.ht()
                    ship.shape(explosion)
                    time.sleep(0.5)
                    ship.ht()
                    ship.shape(enemy_img)
                    ship.goto(400,400)
                    score += 1
                    break
            
            else:
                continue

            break
        
    user_missile.ht()
    write()

def enemy_shoot():
    global lives
    global enemies
    global enemy_speed_mult

    ship = rand.choice(enemies)
    enemy_missile.goto(ship.xcor(),ship.ycor())
    enemy_missile.st()

    while enemy_missile.ycor() > -400:
        enemy_missile.fd(10 * enemy_speed_mult)

        if abs(enemy_missile.xcor() - user.xcor()) < 25 and abs(enemy_missile.ycor() - user.ycor()) < 25:
            lives -= 1
            user.shape(explosion)
            time.sleep(0.5)
            user.shape(user_img)
            break
    
    enemy_missile.ht()
    write()

#Movement
def enemy_move():
    global ammo
    global user_shot_img

    ammo = []

    for i in range(2):
        user_missile = trtl.Turtle()
        user_missile.setheading(90)
        user_missile.pu()
        user_missile.shape(user_shot_img)

        user_missile.ht()
        ammo.append(user_missile)

    for ship in enemies:
        ship.st()
        ship.goto(rand.randint(-200,200), rand.randint(50,350))

#User Movement
def up():
    user.fd(10)

def down():
    user.bk(10)

def left():
    user.goto(user.xcor()-10, user.ycor())

def right():
    user.goto(user.xcor()+10, user.ycor())

def up_right():
    user.goto(user.xcor()+10,user.ycor()+10)

def down_right():
    user.goto(user.xcor()+10,user.ycor()-10)

def up_left():
    user.goto(user.xcor()-10,user.ycor()+10)

def down_left():
    user.goto(user.xcor()-10,user.ycor()-10)

#Score and Lives
def write():
    global ammo

    scribe.clear()
    scribe.write(f"Score: {score} Lives remaining: {lives}", font= ("Courier", 15, "bold"), align = "center")

    ammo_scribe.clear()
    ammo_scribe.write(f"Ammo: {len(ammo)}", font= ("Courier", 15, "bold"), align = "center")

#Timer     
def elapsed_time(start, end):
    elap = end - start
    return round(elap)


#Setup
wn = trtl.Screen()
wn.setup(height = 768, width = 500)
wn.bgpic(r"""C:\Users\NTTDATA\OneDrive\Programs_Codes\CSE_HW_LESSONS\TurtleSection2\turtle_graphics_proj\starbackground.png""")
    
wn.tracer(0)

    #Explosion Setup
explosion = r"""C:\Users\NTTDATA\OneDrive\Programs_Codes\CSE_HW_LESSONS\TurtleSection2\turtle_graphics_proj\explosion.gif"""
wn.addshape(explosion)

    #User ship setup
user = trtl.Turtle()
user.pu()
user.color("white")
user.setheading(90)
user_img = r"""C:\Users\NTTDATA\OneDrive\Programs_Codes\CSE_HW_LESSONS\TurtleSection2\turtle_graphics_proj\user.gif"""
wn.addshape(user_img)
user.shape(user_img)
user.goto(0,-200)
    
    #Enemy Ships setup
enemies = []
for i in range(6):
    enemy = trtl.Turtle()
    enemy.pu()
    enemy.setheading(270)
    enemy.goto(200,200)
    enemy.speed(4)
    
    enemy_img = r"""C:\Users\NTTDATA\OneDrive\Programs_Codes\CSE_HW_LESSONS\TurtleSection2\turtle_graphics_proj\enemy.gif"""
    wn.addshape(enemy_img)
    enemy.shape(enemy_img)
    
    enemies.append(enemy)
    
    #User Shots Setup
ammo = []
for i in range(2):
    user_missile = trtl.Turtle()
    user_missile.setheading(90)
    user_missile.pu()

    user_shot_img = r"""C:\Users\NTTDATA\OneDrive\Programs_Codes\CSE_HW_LESSONS\TurtleSection2\turtle_graphics_proj\user_bullet.gif"""
    wn.addshape(user_shot_img)
    user_missile.shape(user_shot_img)

    user_missile.ht()
    ammo.append(user_missile)

    #Enemy Shots setup
enemy_missile = trtl.Turtle()
enemy_missile.pu()
enemy_missile.setheading(270)

enemy_shot_img = r"""C:\Users\NTTDATA\OneDrive\Programs_Codes\CSE_HW_LESSONS\TurtleSection2\turtle_graphics_proj\enemy_bullet.gif"""
wn.addshape(enemy_shot_img)
enemy_missile.shape(enemy_shot_img)

enemy_missile.ht()

    #Score Keeper
scribe = trtl.Turtle()
scribe.ht()
scribe.pu()
scribe.color("white")
scribe.goto(0,350)

    #Turtle to Tell how much ammo is left
ammo_scribe = trtl.Turtle()
ammo_scribe.pu()
ammo_scribe.ht()
ammo_scribe.color("white")
ammo_scribe.goto(0,-360)

    #Global Variables
score = 0
lives = 3
enemy_speed_mult = 1
game_start = time.time()

wn.tracer(1)


#Active Code
while True:
    #Events

    wn.listen()
    trtl.onkeypress(up, "w")
    trtl.onkeypress(down, "s")
    trtl.onkeypress(right, "d")
    trtl.onkeypress(left, "a")
    trtl.onkeypress(up_right, "e")
    trtl.onkeypress(up_left, "q")
    trtl.onkeypress(down_right, "c")
    trtl.onkeypress(down_left, "z")
    trtl.onscreenclick(user_shoot )
    wn.update()

    enemy_move()
    
    for i in range(3):
        enemy_shoot()
        enemy_speed_mult += 0.5
        
        if lives == 0 or score == 20:
            break

    else:
        continue

    break


#Events after the user loses or wins
end = time.time()
user.ht()
for ship in enemies:
    ship.ht()
user_missile.ht()
enemy_missile.ht()
scribe.clear()
scribe.goto(0,0)


#Winning Event
if score >= 20:
    scribe.color("green")
    scribe.write(f"YOU WON!\n   Time: {elapsed_time(game_start, end)} seconds", font = ("Cuorier", 30, "bold"), align = "center")

#Losing Event
else:
    scribe.color("red")
    scribe.write(f"     YOU LOST!\n      Score: {score}\n  Time: {elapsed_time(game_start, end)} seconds", font = ("Arial", 30, "bold"), align = "center")

time.sleep(5)
exit()

wn.mainloop()