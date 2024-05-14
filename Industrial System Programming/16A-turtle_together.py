import turtle as t
import random

t.shape('arrow')

# 함수 정의 (10도에서 80도 사이)
def turn_up():
    if t.heading() <= 78:
        t.left(2)

def turn_down():
    if t.heading() >= 12:
        t.right(2)

def fire():
    # 50각형 그리면서 다시 돌아오게(마치 쏘는 것처럼)
    n = 50
    for i in range(n):
        t.forward(25)
        t.right(360/n)
        if t.ycor() <= 0: # while 하면 위가 다 짧아짐
            a = t.xcor()
            print(a) # x 좌표 출력
            # 성공 여부 판정 (땅에 박혔을 떄 x 좌표가 타겟을 기준으로 +-25 사이에 있으면 성공)
            if a  >= target - 25 and a <= target + 25:
                t.color("blue")
                t.write("Good!", False, "center", ("", 15))
            else:
                t.color("red")
                t.write("Bad!", False, "center", ("", 15))
            break

# 땅 만들기
t.goto(300, 0)
t.goto(-300, 0)
t.home()
t.up()

# target 지점 그리기
target = random.randint(0, 200)
t.goto(target-25, 2)
t.down()
t.pensize(20)
t.color('green')
t.goto(target+25, 2)

# 쏘기 위한 위치로 이동
t.up()
t.color('black')
t.goto(-200, 0)


t.onkeypress(turn_up, 'Up')
t.onkeypress(turn_down, 'Down')
t.onkeypress(fire, "space")
t.listen() # 키보드 입력 받게 하기
