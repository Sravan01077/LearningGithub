
a = int(input("Enter a value to Check that Number is ArmStrong or Not"))  
check = a  
b = len(str(a))
s1 = 0
while a != 0:
    r = a % 10
    s1 = s1+(r**b)
    a = a//10
if check == s1:
    print("The given number", check, "is armstrong number")
else:
    print("The given number", check, "is not armstrong number")
