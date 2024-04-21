import random
import time

problem = ['lion', 'tiger', 'dragon', 'cat', 'dog', 'monkey']

n = 1
print('타자게임 할 준비가 되면 엔터를 눌러주세요!')
input()


while n <= 5:
    print('문제', n)
    q = random.choice(problem)
    print(q, '를 따라 입력하세요!')
    start = time.time()
    a = input()

    if q == a:
        print('정답')
        n += 1
        q = random.choice(problem)
    else:
        print('오답')

end = time.time()
et = end - start

print(f' 소요된 시간은 {et:0.2f}초입니다.')

