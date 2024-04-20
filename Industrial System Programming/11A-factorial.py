def factorial(n):
    fact = 1
    for x in range(1, n+1):
        fact = fact * x
    return fact

print(factorial(5))
print(factorial(50))


def age(a):
    if a==0:
        return 0
    print('age', str(a))
    # 재귀함수
    age(a-1)

age(55)


def factorial_n(n):
    
    if n >= 2:
        return n * factorial_n(n-1)
    else:
        return 1

print(factorial_n(5))

def fib(n):

    if n >= 3:
        return fib(n-1) + fib(n-2)
    
    elif n == 2:
        return 1
    
    else:
        return 0


print(fib(4))


    
