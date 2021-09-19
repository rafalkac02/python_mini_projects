from cs50 import get_int

def prime(n):
    if num < 2:
        return False
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
    return True

num = get_int("Number: ")

if prime(num):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")