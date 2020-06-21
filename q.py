def div(n):
    global sum
    sum = 0
    if n == 0:
        return n
    else:
        return n % 10 + div(n//10)
n = int(input())
m = n % 10
if div(n) % m == 0:
    print("Yes")
else: print("No")




