import turtle as t

def polygon(n):
    for x in range(n):
        t.forward(50)
        t.left(360/n)

def py(n):
    polygon2(n, 50)


def polygon2(n, a):
    for x in range (n):
        t.forward(a)
        t.left(360/n)

polygon(3)
py(3)
polygon(5)



t.up()
t.forward(100)
t.down()

polygon2(3, 75) 
polygon2(5, 100)
