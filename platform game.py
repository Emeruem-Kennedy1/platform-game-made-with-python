import turtle


from numpy import random
a = random.randint(-360,0)
b = random.randint(0,100)

c = random.randint(290)
d = random.randint(120,200)

score = 0
life_count = 5

highest_score = []


#setting up the screen of the game
win = turtle.Screen()
win.title('bounce game')
win.setup(width=800, height=700)
win.bgcolor('black')
win.tracer(0)

#creating the objects for the game

#pen

#Slider
slider = turtle.Turtle()
slider.speed(0)
slider.shape('square')
slider.color('white')
slider.shapesize(stretch_wid=.5,stretch_len=9)
slider.penup()
slider.goto(0,-320)
#ball
ball = turtle.Turtle()
ball.speed(3)
ball.shape('circle')
ball.color('white')
ball.penup()
ball.goto(0,-300)
#move the ball
ball.dx = 1
ball.dy = 1

player_score = 0

# emeny rectangles
'''
enemy1 = turtle.Turtle()
enemy1.speed(0)
enemy1.shape('square')
enemy1.color('white')
enemy1.shapesize(stretch_wid=1,stretch_len=8)
enemy1.penup()
enemy1.goto(a,b)
enemy1.dx = .3

enemy2 = turtle.Turtle()
enemy2.speed(0)
enemy2.shape('square')
enemy2.color('white')
enemy2.shapesize(stretch_wid=1,stretch_len=8)
enemy2.penup()
enemy2.goto(c,d)
enemy2.dx = -0.3
'''
# highest score
highest = turtle.Turtle()
highest.speed(0)
highest.penup()

pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write('       Score: 0   ', align='left', font=('Courier',24,'normal'))


life = turtle.Turtle()
life.speed(0)
life.color('red')
life.penup()
life.hideturtle()
life.goto(0,260) 
life.write('lives: 5      ', align='right', font=('Courier',24,'normal'))


#the goal
goal = turtle.Turtle()
goal.speed(0)
goal.shape('square')
goal.color('green')
goal.shapesize(stretch_wid=1,stretch_len=11)
goal.penup()
goal.goto(0,330)

'''
#life stuff
life_1 = turtle.Turtle()
def add_life_1():
    life_1 = turtle.Turtle()
    life_1.speed(0)
    life_1.shape('circle')
    life_1.color('red')
    life_1.shapesize(stretch_wid=1,stretch_len=1)
    life_1.penup()
    life_1.goto(330,300)
def add_life_2():
    life_2 = turtle.Turtle()
    life_2.speed(0)
    life_2.shape('circle')
    life_2.color('red')
    life_2.shapesize(stretch_wid=1,stretch_len=1)
    life_2.penup()
    life_2.goto(300,300)
def add_life_3():
    life_3 = turtle.Turtle()
    life_3.speed(0)
    life_3.shape('circle')
    life_3.color('red')
    life_3.shapesize(stretch_wid=1,stretch_len=1)
    life_3.penup()
    life_3.goto(270,300)
def add_life_4():
    life_4 = turtle.Turtle()
    life_4.speed(0)
    life_4.shape('circle')
    life_4.color('red')
    life_4.shapesize(stretch_wid=1,stretch_len=1)
    life_4.penup()
    life_4.goto(240,300)
def add_life_5():
    life_5 = turtle.Turtle()
    life_5.speed(0)
    life_5.shape('circle')
    life_5.color('red')
    life_5.shapesize(stretch_wid=1,stretch_len=1)
    life_5.penup()
    life_5.goto(210,300)

def lose():
    life_1.clear()
'''



#move functions
def move_right():
    pos = slider.xcor()
    pos += 20
    slider.setx(pos)


def move_left():
    pos = slider.xcor()
    pos -= 20
    slider.setx(pos)

win.listen()

win.onkeypress(move_right,'Right')
win.onkeypress(move_left,'Left')

while True:
    win.update()

    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
   
    '''
    enemy1.setx(enemy1.xcor()+enemy1.dx)
    enemy2.setx(enemy2.xcor()+enemy2.dx)
    
    if enemy1.xcor()>300:
        enemy1.dx *= -1
    if enemy1.xcor()<-300:
        enemy1.dx *= -1

    if enemy2.xcor()>300:
        enemy2.dx *= -1
    if enemy2.xcor()<-300:
        enemy2.dx *= -1
    '''
    if ball.xcor()>380:
        ball.dx *= -1
    if ball.xcor()<-380:
        ball.dx *= -1
    #ball and goal shirr
    if ball.ycor() >= 310 and ball.xcor()<-110:
        ball.dy *= -1
    
    if ball.ycor()>=310 and ball.xcor()>110:
        ball.dy *= -1

    #paddle and ball stuffs
    if (ball.ycor() < (-310) and ball.ycor() > -330 ) and (ball.xcor()< slider.xcor()+100) and (ball.xcor() > slider.xcor() -80) :
        ball.sety(-300)
        ball.dy *= -1
    if ball.ycor()<-330 :
        slider.goto(0,-320)
        life_count -=1
        life.clear()
        life.write('lives: {}      '.format(life_count), align='right', font=('Courier',24,'normal'))

        ball.goto(0,-300)
        
    
    #scoring
    if ball.xcor()<=110 and ball.ycor()>310 and ball.xcor()>=110:
        slider.goto(0,-320)
        ball.goto(0,-300)
        score += 1
        pen.clear()
        pen.write('       Score: {}   '.format(score), align='left', font=('Courier',24,'normal'))

   


    

    