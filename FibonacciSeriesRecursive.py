

def fib(a):
    if a <= 1:
        return a
    else:
        b = fib(a-1)
        c = fib(a-2)
        d = b + c
        return d

a = 10
for i in range(a):
    print(fib(i))


