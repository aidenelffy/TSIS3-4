n = int(input())

number = n
reverse = 0
while n > 0:
    last_number = n%10
    reverse = (reverse * 10) + last_number
    n//=10

if number == reverse:
    print("YES")
else:
    print("NO")