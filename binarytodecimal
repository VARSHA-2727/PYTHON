def bin2dec(n):
    dec,i=0,0
    while n>0:
        r=n%10
        exp=r*(2**i)
        dec=dec+exp
        n=n//10
        i+=1
    return dec
bn=int(input("enter the bin number"))
decimal=bin2dec(bn)
print(" the decimal number is",decimal)
