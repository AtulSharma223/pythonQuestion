def convertToOctal(num):
    octal=""
    temp=num
    while num>0:
        rem=num%8
        octal=str(rem)+octal
        num=num//8
    return octal

octalNumber=convertToOctal(1000)
print("octal number is ",octalNumber)