import turtle as t
import random

t.bgcolor("orange")
t.setup(500, 500)
t.bgcolor("orange")
t.shape("turtle")
t.speed(0)
t.up()
t.color("white")
 
# 악당 거북이
te = t.Turtle()
te.shape('turtle')
te.color('red')
te.speed(0)
te.up()
te.goto(0, 200)

# 먹이
ts = t.Turtle()
ts.shape('circle')
ts.color('green')
ts.up()
ts.goto(0, -200)

# 함수 정의
def forward():
    t.forward(10)
    if t.distance(ts) < 15:
        print('냠냠')
        s_x = random.randint(-100, 100)
        s_y = random.randint(-100, 100)
        ts.goto(s_x, s_y)
    t.ontimer(forward, 500)


def turn_right(): # 오른쪽
    t.setheading(0)

def turn_left(): # 왼쪽
    t.setheading(180)

def turn_up(): # 위
    t.setheading(90)

def turn_down(): # 아래
    t.setheading(270)


t.ontimer(forward, 500) # 0.5초
t.onkeypress(turn_right, "Right")
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_down, "Down")
t.listen()
