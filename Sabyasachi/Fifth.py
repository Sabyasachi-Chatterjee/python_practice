a = int(input("Enter First Numner = "))
b = int(input("Enter Second Number = "))
c = int(input("Enter Third Number = "))
if(a > b and a > c):
    print("The Largest Number is = ", a)
elif(b > a and b > c):
    print("The Largest Number is = ", b)
elif(c > a and c > b):
    print("The Largest Number is = ", c)
else:
    print("All the Numbers are Same.")