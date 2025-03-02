#Write a recursive function in Python to find the GCD of two numbers.

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

print(gcd(48, 18))  