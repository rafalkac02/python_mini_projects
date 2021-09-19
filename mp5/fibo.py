from cs50 import get_int

n = get_int("How many Fibonacci numbers would you like to generate? ")

fibo = []

for i in range(n):
    if len(fibo) <= 1:
        fibo.append(1)
    else:
        fibo.append(fibo[i-2] + fibo[i-1])

print(fibo)