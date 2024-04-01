import turtle as t

t.color('green')
t.bgcolor('black')
t.speed(0)

angle = 6
n = int(360 / angle)

for i in range(n):
    t.circle(100)
    t.left(angle)
