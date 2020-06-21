k = input()
list = []
x = len(k)
for i in range (0,x):
    list.append(k[i])

for i in range(0,x):
    for j in range(0,x):
        if list[i]<list[j]:
            temp = list[i]
            list[i]=list[j]
            list[j]=temp
j=""

for i in range(0,x):
    j = j+list[i]

print(j)