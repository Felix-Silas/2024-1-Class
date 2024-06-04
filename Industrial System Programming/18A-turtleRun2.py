import turtle as t
import random

t.title("Turtle Run")

score = 0
playing = False

t.bgcolor("orange")
t.setup(500, 500)
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

def turn_right(): # 오른쪽
    t.setheading(0)

def turn_left(): # 왼쪽
    t.setheading(180)

def turn_up(): # 위
    t.setheading(90)

def turn_down(): # 아래
    t.setheading(270)

def start(): #게임 시작 및 초기화
    global playing
    if playing == False:
        t.setup(500, 500) # 그래픽 창 크기
        te.goto(0, 200)
        ts.goto(0, -200)
        t.home()
        playing = True
        t.clear()
        play()

def play():
    global score
    global playing
    t.forward(10)
    if random.randint(1,5) == 3: #20% 확률로 쳐다보기 
        ang = te.towards(t.pos())
        te.setheading(ang)
    speed=score+5 #점수가 오를 때 마다 속도 증가
    if speed >15:
        speed = 15
    te.forward(speed)
    if t.distance(te) < 15: #닿으면 점수표시 game over 표시
        text = "Score:"+ str(score)
        meassage("Game Over", text)
        playing = False
        score = 0
    if t.distance(ts) < 15: #먹으면 점수 증가 및 점수 표시
        score = score + 1
        t.write(score)
        s_x = random.randint(-100, 100)
        s_y = random.randint(-100, 100)
        ts.goto(s_x, s_y)
    if playing:
        t.ontimer(play,100)

def meassage(m1,m2): #화면에 메시지 표시
    t.clear()
    t.goto(0,100)
    t.write(m1,False,"center",("",20))
    t.goto(0,-100)
    t.write(m2,False,"center",("",15))
    t.home()

t.onkeypress(start,"space")
t.onkeypress(turn_right, "Right")
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_down, "Down")
t.listen()
meassage("Tirtle Run","[Space}")
