a = 0
b = 1
x = int(input("Enter an Ending Number = "))

print(a, end =" ")
print(b, end=" ")
for i in range(2,x):
    c = a + b 
    print(c, end=" ")
    a=b
    b=c
