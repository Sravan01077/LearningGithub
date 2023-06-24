a=int(input("enter a value"))
ra=0
while a != 0:
    b=a%10
    ra=ra*10+b
    a=a//10
print("reversed number:" + str(ra))