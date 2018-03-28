print("Hello snake")
print("============")

def fib(n):
    a, b = 0, 1
    i = 0
    while i < n:
        a, b = b, a + b
    return a


print(fib(10))

