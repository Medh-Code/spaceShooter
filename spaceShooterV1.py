#Imports
import turtle as trtl
import random as rand
import time

#Functions

#Firing
def user_shoot():
    global score
    user_missile.goto(user.xcor(),user.ycor())
    user_missile.st()
    
    while user_missile.ycor() < 300:  
        user_missile.fd(10)
        
        if (abs(user_missile.xcor()-enemy.xcor()) < 15 and abs(user_missile.ycor() - enemy.ycor()) < 15):
            user_missile.ht()
            score += 1
            
            break
    
    user_missile.ht()
    write()

def enemy_shoot():
    global lives

    enemy_move()
    enemy_missile.goto(enemy.xcor(),enemy.ycor())
    enemy_missile.st()

    while enemy_missile.ycor() > -400:
        enemy_missile.fd(10)

        if abs(enemy_missile.xcor() - user.xcor()) < 15 and abs(enemy_missile.ycor() - user.ycor()) < 15:
            lives -= 1
            break
    
    enemy_missile.ht()
    write()

#Movement
def enemy_move():
    enemy.goto(rand.randint(-650,650), rand.randint(0,300))

def drag(x,y):
    wn.tracer(0)
    user.goto(x,y)
    wn.tracer(1)

#Score and Lives
def write():
    scribe.clear()
    scribe.write(f"Score: {score}\nLives remaining: {lives}", font= ("Roboto", 15) )

#Timer and Timer Events
    
def elapsed_time(start, end):
    elap = end - start
    return elap


#Setup
wn = trtl.Screen()
wn.setup(height = 768, width = 1366)
wn.bgpic(r"""C:\Users\NTTDATA\OneDrive\Programs_Codes\CSE_HW_LESSONS\TurtleSection2\turtle_graphics_proj\starbackground.png""")
    
wn.tracer(0)    
    #User ship setup
user = trtl.Turtle()
user.pu()
user.color("white")
user.setheading(90)
wn.addshape(r"""C:\Users\NTTDATA\OneDrive\Programs_Codes\CSE_HW_LESSONS\TurtleSection2\turtle_graphics_proj\user.gif""")
user.shape(r"""C:\Users\NTTDATA\OneDrive\Programs_Codes\CSE_HW_LESSONS\TurtleSection2\turtle_graphics_proj\user.gif""")
    
    #Enemy Ship setup
enemy = trtl.Turtle()
enemy.pu()
enemy.setheading(270)
enemy.goto(200,200)
wn.addshape(r"""C:\Users\NTTDATA\OneDrive\Programs_Codes\CSE_HW_LESSONS\TurtleSection2\turtle_graphics_proj\enemy.gif""")
enemy.shape(r"""C:\Users\NTTDATA\OneDrive\Programs_Codes\CSE_HW_LESSONS\TurtleSection2\turtle_graphics_proj\enemy.gif""")
    
    #User Shots Setup
user_missile = trtl.Turtle()
user_missile.setheading(90)
user_missile.pu()
user_missile.shape("circle")
user_missile.color("red")
user_missile.ht()

    #Enemy Shots setup
enemy_missile = trtl.Turtle()
enemy_missile.pu()
enemy_missile.setheading(270)
enemy_missile.color("green")
enemy_missile.shape("square")
enemy_missile.ht()

    #Score Keeper
scribe = trtl.Turtle()
scribe.ht()
scribe.pu()
scribe.color("white")
scribe.goto(400,300)

    #Global Variables
score = 0
lives = 3

wn.tracer(1)

#Active Code
while lives != 0:
    #Events
    
    wn.listen()
    user_shoot()
    user.ondrag(drag) 
    enemy_shoot()

wn.mainloop()