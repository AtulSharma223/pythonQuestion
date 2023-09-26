num=int(input("Enter number"))
print("Actual number is ",num)
reversed=0
while num>0:
    reversed=reversed*10+num%10
    num=num//10
print("Reversed number is ",reversed)