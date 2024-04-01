import turtle as t
import random

t.shape("turtle")  # ‘거북이’모양의 거북이 그래픽을 사용
t.speed(0)

for x in range(500): # 거북이를 500번 움직임
    a = random.randint(1, 360) # 1~360에서 아무 수나 골라 a에 저장
    t.setheading(a) # 거북이 방향을 a 각도로돌림
    t.forward(10) # 거북이가 10만큼 앞으로 이동
