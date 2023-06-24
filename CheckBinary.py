def check(string) :
    b = set(string)
    s = {'0', '1'}
    if s == b or b == {'0'} or b == {'1'}:
        print("Binary String")
    else :
        print("Non Binary String")
  
s1= "0110101"
check(s1)
s2 = "1021"
check(s2)
s3="abcd"
check(s3)