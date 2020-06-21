def gcd(a, b):
    if (b == 0):
        return a
    elif(a==0):
        return b
    elif(a>b):
        return gcd(b, a%b)
    else:
        return gcd(a, b%a)
def lcm(a,b):
    return a*b//gcd(a, b)
a = int(input())
b = int(input())
print (gcd(a, b)+lcm(a, b))