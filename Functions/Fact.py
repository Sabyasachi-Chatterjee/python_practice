def fact(a):
    f = 1
    for i in range(a,1,-1):
        f = f * i
    # return "Factorial of a number is = ",{f}
    return f"Factorial of the number {a} is {f}"
n = int(input("Enter a Number = "))
print(fact(n))