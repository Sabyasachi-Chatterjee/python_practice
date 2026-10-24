fact = False
num = int(input("Enter a Number = ")) # Taking a number as user input

# Checking for different conditions
if (num == 0 or num == 1):
    print(num, "is neither a Prime Number nor a Composite Number.")
elif(num % 2 == 0):
    fact = True
    print(num, "is a Composite Number.")
else:
    print(num, "is a Prime Number.")
