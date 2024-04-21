import random

def make_quesion():
    a = random.randint(1, 40)
    b = random.randint(1, 20)
    op = random.randint(1, 3)

    q = str(a)

    if op == 1:
        q = q + '+'
    if op == 2:
        q = q + '-'
    if op == 3:
        q = q + '*'

    q = q + str(b)

    return q


ct_answer = 0 # 정답 수
ct_wrong = 0 # 오답 수

for i in range(5):
    q = make_quesion()
    print(q)
    ans = input("=")
    r = int(ans)

    if eval(q) == r:
        print("정답!")
        ct_answer += 1
    else:
        print("오답")
        ct_wrong += 1

print("정답 수:", ct_answer, "오답 수:", ct_wrong)

if ct_wrong == 0:
    print("전부 다 맞았습니다.")
    
