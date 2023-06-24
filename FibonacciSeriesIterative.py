a=int(input("enter how many Fibonacci series you want "))
n1=0
n2=1
print(n1)
print(n2)
for i in range(2,a):
    sum=n1+n2
    print(sum)
    n1=n2
    n2=sum
