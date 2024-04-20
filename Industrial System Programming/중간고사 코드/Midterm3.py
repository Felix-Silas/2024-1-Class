import turtle as t

t.shape("turtle")


t.bgcolor("black")
t.color("green")
t.speed(10)


a = 6
n = int(360 / a)


for i in range(n):
    t.left(a)
    t.circle(100)
    
