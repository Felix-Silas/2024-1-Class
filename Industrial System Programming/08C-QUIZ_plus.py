import random

answer = 0

for i in range(1, 11):
    print("program", i)
    a = random.randint(1, 30)
    b = random.randint(1, 30)
    sum = a + b

    print(a, "+", b, "=")
    x = input()
    c = int(x)

    if sum == c:
        answer += 1
        print('정답')
    else:
        print('오답')

print("총 10문제 중에,", answer, "문제를 맞췄습니다.")

if answer >= 7:
    print("천재!")
else:
    print("바보?")
