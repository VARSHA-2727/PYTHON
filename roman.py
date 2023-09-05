def roman2int(romstr):
    roman_dict={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500}
    romanback=list(romstr)[::-1]
    value=0
    rightval=roman_dict[romanback[0]]
    for numeral in romanback:
        leftval=roman_dict[numeral]
        if leftval<rightval:
            value-=leftval
        else:
            value+=rightval
            rightval=leftval
    return value
romstr=input("enter the roman number")
print(roman2int(romstr))

