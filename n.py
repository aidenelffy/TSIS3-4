def sum(x,y):
    if(y==0):
        return x
    elif(y <0):
        return(-(1+sum(-x, -y-1)))
    else:
        return(1+sum(x,y-1))
x=int(input())
y=int(input())
print(sum(x,y))