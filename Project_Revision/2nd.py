fact = False
x = int(input("Enter a Number = "))
if (x == 0 or x == 1):
    print("Neither prime nor composite")
elif(x % 2 == 0):
    fact = True
    print(x, "is not a Prime Number.")
else:
    print(x, "is a Prime Number.")
