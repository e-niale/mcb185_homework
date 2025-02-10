# 10demo.py by elaine :3

# background
import math

# printing math for fun
""" print("hello, again") # greeting 
print(1.5e-2)
print(1+1)
print(2**3)
print(pow(2,3))
print(math.pow(2,3))
print(2**0.5)
print(math.sqrt(2))
print(math.log(2))
print(1/0) # divide by zero error
print(math.log(0)) # math domain error 
print(math.sqrt(-1)) # math domain error """

# variable use + math 
""" a = 3 # side 1
b = 4 # side 2
c = math.sqrt(a**2 + b**2)  
print(c) """

# functions
""" def pythagoras(a,b):
    return math.sqrt(a**2 + b**2)
print(pythagoras (3,4)) """

# if statements
""" a = 2
b = 3
if a == b:
    print('a equals b')
print(a, b, sep=', ', end='!\n') """

# F to C
""" def f2c(f):
    print((f-32) * 5/9)
f2c(100) """

# MPH to KPH
""" def mph2kph(m):
    print((m*1.609))
mph2kph(100) """

# DNA concentration from OD260
""" def od260(od):
    print(od*50)
od260(5) """

# arithmetic mean of 3 numbers
""" def arithmean(a, b, c):
    print((a+b+c)/3)
arithmean(1,2,3) """

# geomentric mean of 3 numbers
""" def geomean(a, b, c):
    print((a+b+c)**(1/3))
geomean(1,2,3) """

# harmonic mean of 3 numbers
""" def harmmean(a, b, c):
    print((3/(1/a + 1/b + 1/c)))
harmmean(1,2,3) """

# pythagorean theorem
""" def pythag(x1, y1, x2, y2):
    b = abs(x1 - x2)
    h = abs(y1 - y2)
    print(math.sqrt(b**2 + h**2))
pythag(0,0,3,4) """

# Booleans 
""" a = 1
b = 2
c = a == b
print(a == b) """

# if-elif-else
""" a = 1
b = 2
if   a < b:  print('a < b')
elif a <= b: print('a <= b')
elif a == b: print('this will never print!') """

# Type Error
""" a = 1
s = 'G'
if a < s: print('a < s') """

# Integer checker
""" def isint(n):
    if n//1 == n: print (n, "is an integer")
    else: print(n, "is not an integer")
isint(103.234) """

# Valid probability
""" def validprob(n):
    if n >= 0 and n <= 1: print (n, "is a valid probability")
    else: print (n, "is not a valid probability")
validprob(0.5632) """

# Molecular weight
""" def molecweight(nt):
    if nt == 'A': return(nt + ": 313.2 g/mol")
    elif nt == 'C': return(nt + ": 289.2 g/mol")
    elif nt == 'G': return(nt + ": 329.2 g/mol")
    elif nt == 'T': return(nt + ": 304.2 g/mol")
print(molecwe ight("K")) """

# nt complement 
""" def ntcomplement(nt):
    if nt == 'A': return("T")
    elif nt == 'C': return("G")
    elif nt == 'G': return("C")
    elif nt == 'T': return("A")
print(ntcomplement("F")) """

# max 3
""" def max3(a, b, c):
    if a > b and a > c: return a
    elif b > c: return b
    else: return c
print(max3(3,6,0)) """

# return sensitivity, specificity, and F1 given true positive, false positive, true negative, false negative
""" def sensitivity(tp, fn):
    return tp / (tp + fn)
def specificity(tn, fp):
    return tn / (tn + fp)
def f1(tn, fp, tp, fn):
    print("F1 score:", 2 * specificity(tn, fp) * sensitivity(tp,fn) / (specificity(tn, fp) + sensitivity(tp, fn)))
f1(1, 2, 3, 4) """

# shannon entropy
""" def shannonentropycalc(a, c, g, t):
    total = a + c + g + t
    a = a / total
    c = c / total
    g = g / total
    t = t / total
    return -1 * (a * math.log2(a) + c * math.log2(c) + g * math.log2(g) + t * math.log2(t))
def shannon_entropy(a, c, g, t):
    total = a + c + g + t
    if total == 0: print (0)
    if a == 0: a = 1 * 10**-20
    if c == 0: c = 1 * 10**-20
    if g == 0: g = 1 * 10**-20
    if t == 0: t = 1 * 10**-20
    entropy = shannonentropycalc(a, c, g, t)
    if abs(entropy - 0) < 1e-9: print(0) 
    else: print(entropy)

shannon_entropy(1, 1, 0, 1) """

# phred quality with base 2

def base2phred(char):
    ascii = ord(char)
    if ascii <= 64:
        return 1
    elif ascii > 64 and ascii <= 126:
        return 2**-(ascii - 64)
print(base2phred(' '))
