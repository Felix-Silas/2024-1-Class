import turtle as t

# 비동기함수: 이벤트가 발생하면 호출이 되는 함수
def turn_right(): # 오른쪽으로 이동하는함수
    t.setheading(0) # t.seth(0)으로 입력해도 됨
    t.forward(10) # t.fd(10)으로 입력해도 됨
    
def turn_up(): # 위로 이동하는함수
    t.setheading(90)
    t.forward(10)
def turn_left():
    t.setheading(180) # 왼쪽으로 이동하는함수
    t.forward(10) 
def turn_down(): # 아래로 이동하는함수
    t.setheading(270)
    t.forward(10)

def blank():
    t.clear()

t.shape("turtle")  # 거북이 모양을사용
t.speed(0)
t.onkeypress(turn_right, "Right")
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_down, "Down")
t.onkeypress(blank, "Escape")
t.listen()
