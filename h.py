def lcm_gcd(a, b):
    c = a*b
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return (c//(a+b))+a+b

a = int(input())
b = int(input())
print (lcm_gcd(a, b))