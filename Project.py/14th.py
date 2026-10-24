a = int(input("Enter a Number = "))
fact = 1
for i in range(a,1,-1):
    fact = fact * i
print("The Factorial of ", a, " is = ", fact)
print(f"The Factorial of {a} is = {fact}")