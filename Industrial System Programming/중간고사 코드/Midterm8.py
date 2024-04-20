def factorial(n):
    fact = 1

    for i in range(1, n+1):
        fact *= i

    return fact


a = factorial(5)
print(a)
        
    

def age(n):
    if n != 0:
        print(n)
        age(n-1)
    else:
        return 0


#age(55)


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

print(fib(5))
