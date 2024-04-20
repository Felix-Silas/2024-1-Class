import random

def make_question():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    op = random.randint(1, 3)

    if op == 1:
        st = str(a) + '+' + str(b)
    if op == 2:
        st = str(a) + '-' + str(b)
    if op == 3:
        st = str(a) + '*' + str(b)

    return st


sc1 = 0
sc2 = 0

for i in range(5):
    st = make_question()
    print(st)

    answer = int(input('답은?'))

    if eval(st) == answer:
        print('정답')
        sc1 += 1
    else:
        print('바보')
        sc2 += 1


print(sc1)
print(sc2)
