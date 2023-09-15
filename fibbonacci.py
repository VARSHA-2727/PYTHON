def Fn(n):
    if(n<=1):
        return n
        return(Fn(n-1)+Fn(n-2))
N=int(input("enter the n value"))
if (N<1):
    print("n is greater than 0")
else:
    for x in range(0,N):
        print(Fn(x),end=" ")
