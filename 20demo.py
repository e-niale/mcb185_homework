# 20demo.py by elaine :3
import math
import random

# tuples
""" t = 1, 2  
print(t)
print(type(t)) """
""" person = 'Steve', 21, 57891.50 # name, age, yearly income
print(person) """

def midpoint(x1, y1, x2, y2):
    x = (x1 + x2) / 2
    y = (y1 + y2) / 2
    return x, y

m = midpoint(1, 2, 3, 4)
mx, my = midpoint(1, 2, 3, 4)

# while loop 
""" i = 0
while True:
    i = i + 1
    print('hey', i)
    if i == 3: break """

# for loops 
""" for i in range(1, 10, 3):
    print(i) """
""" for i in range(1, 10, 3):
    print(i) """
""" basket = 'milk', 'eggs', 'bread'
for thing in basket:
    print(thing)
for i in range(len(basket)):
    print(basket[i]) """

# nesting
""" for i in range(7):
    if i % 2 == 0: print(i, 'is even')
    else:          print(i, 'is odd') """

# sum of numbers 1 through n (triangular number)
def triangularnum(n):
    tri = 0
    for i in range(1,n+1):
        tri += i
    return tri


# factorial of a number
def factorial(n):
    if n == 0: return 1
    fact = 1
    while n > 0:
        fact = fact * n
        n -= 1
    return fact

# Poisson probability
def poisson(k, n):
    return (n**k * math.e**-n) / factorial(k)

# n choose k
def nchoosek(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))

# euler's number 
def eulersnum(n):
    euler = 1
    for i in range(1, n):
        euler += 1/factorial(i)
    return euler

# prime number check
def primecheck(n):
    rem = 0
    for i in range(2, n):
        if n % i == 0:
            return "Not Prime"
        return "Prime"

# Nilakantha estimate of pi
def pi_nilakantha(n):
    pi = 3
    for i in range(2, n, 4):
        pi += 4 / (i * i+1 * i+2) # doesn't give right answer?
    for i in range(4, n, 4):
        pi -= 4 / (i * i+1 * i+2)
    return pi
# correct answer
def nilakantha(limit):
    pi = 3
    for i in range(1, limit+1):
        n = 2 * i
        d = n * (n+1) * (n+2)
        if i % 2 == 0: pi = pi - 4 / d
        else:          pi = pi + 4 / d
    return pi

# random seeds
""" random.seed(1)
print(random.random())
print(random.random())
random.seed(2)
print(random.random())
print(random.random())
random.seed(1)
print(random.random())
print(random.random()) """

# monty pi-thon
def montypithon():
    inside = 0
    count = 0
    while True:
        x = random.random()
        y = random.random()
        count += 1
        if math.sqrt(x**2 + y**2) < 1:
            inside += 1
        print(inside/count * 4)

# dice roll avgs
def d6x3(n):
    total = 0
    for i in range(1, n+1):
        roll = 0
        for i in range (1, 4):
            roll += random.randint(1, 6)
        total += roll
    return total / n
def d6x3r1(n):
    total = 0
    for i in range(1, n+1):
        roll3 = 0
        for i in range (1,4):
            roll = random.randint(1, 6)
            while roll == 1: 
                roll = random.randint(1,6)
            roll3 += roll
        total += roll3
    return total / n
def d6x2max(n):
    total = 0
    for i in range(1, n+1):
        for i in range (1,4):
            roll1 = random.randint(1,6)
            roll2 = random.randint(1,6)
            if roll1 > roll2:
                total += roll1
            else:
                total += roll2
    return total / n
def d6x4drop(n):
    total = 0
    for i in range(1, n+1):
        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)
        roll3 = random.randint(1, 6)
        roll4 = random.randint(1, 6)
        if roll1 > roll2 or roll1 > roll3 or roll1 > roll4:
            total += roll1
        if roll2 > roll1 or roll2 > roll3 or roll2 > roll4:
            total += roll2
        if roll3> roll1 or roll3 > roll2 or roll3 > roll4:
            total += roll3
        if roll4 > roll1 or roll4 > roll2 or roll4 > roll3:
            total += roll4
    return total / n






        