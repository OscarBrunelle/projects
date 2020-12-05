n=int(input("give me a number: "))
digits=int(input("number of digits :"))
base=int(input("give me its base :"))
result=0
i=digits-1
for x in range(digits):
    if i == digits-1:
        result+=(n//(10**i))*(base**(i+1))
        i-=1
    elif i==0:
        result=(n%10)*base**(i+1)
    else:
        result+=(n//(10**i)-n//(10**(i+1)))*(base**(i+1))
        i-=1
print(result)
