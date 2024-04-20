import turtle as t

t.shape("turtle")


n = 3

angle = 360 / n

t.color("red")
for i in range(n):
    t.forward(100)
    t.left(angle)

t.pensize(3)
t.color("green")

for i in range(4):
    t.forward(100)
    t.left(90)

t.color("blue")

t.circle(50)




