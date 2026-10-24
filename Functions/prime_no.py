def prime(num):
    fact = False
    if (num == 0 or num == 1):
     return (f"{num} is neither a Prime Number nor a Composite Number.")
    #  print(num, "is neither a Prime Number nor a Composite Number.")
    elif(num % 2 == 0):
     fact = True
     return (f"{num} is a Composite Number.")
    #  print(num, "is a Composite Number.")
    else:
      return (f"{num} is a Prime Number.")
    #  print(num, "is a Prime Number.")
n = int(input("enter a number = "))
print(prime(n))