def tm(a, g, c, t):
    length = a + g + c + t
    if length <= 13:
        return (a + t) * 2 + (g + c) * 4
    else:
        return 64.9 + 41 * (g + c - 16.4) / (a + t + g + c)

print(tm(1, 1, 1, 4))
