# fibonacci sequence! first 10
import random

def fibonacci(n):
    f1 = 0
    f2 = 1
    for i in range(n):
        print(f1)
        f3 = f1 + f2
        f1 = f2
        f2 = f3

fibonacci(10)