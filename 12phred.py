import math

def char_to_prob(char):
    ascii = ord(char)
    if ascii >= 33 and ascii <= 126:
        return 10**-((ascii - 33)/10)
print(char_to_prob('B'))

def prob_to_char(p):
    if p >= 0 and p <= 1:
        return chr(int(-(math.log10(p) - 33)))
print(prob_to_char(0.0006))