n = int(input())
a, b, c = 0, 1, 1
i = 2
while i < n:
    d = a + b + c
    a, b, c = b, c, d
    i += 1
 
print(d)