def gcd(a, b):
    mod = a % b
    while mod > 0:
        a = b
        b = mod
        mod = a % b
    return b

def lcd(a, b):
    return a*b // gcd(a, b)

print(lcd(24, 32))
