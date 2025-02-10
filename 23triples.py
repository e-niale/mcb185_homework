# pythagorean triples
import math

def pythagorean3():
    for i in range(1, 100):
        a = i
        for i in range(a+1,100):
            b = i
            c = math.sqrt(a**2 + b**2)
            if c % 1 == 0:
                print(a, b, int(c))
pythagorean3()