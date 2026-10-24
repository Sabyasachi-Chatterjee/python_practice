# Cases :-
# Check whether a given number is present in the range or not
# Print the numbers in a series from 10 - 20 with step value of 3
# Factorial of a number
# Fibonacci Series
# Print first 10 natural
# Square of the numbers from 20 - 40
# print multtiple of 3 and their sum from range of 10 -30
print("Menu =\n 1 : Number in the Range from 10 - 20 \n 2 : 10 - 20 series numbers with 3 increment\n 3 : Factorial\n 4 : Fibonacci\n 5 : First 10 Natural No.\n 6 : Square of Nos. from 20 - 40\n 7 : Multiples of 3 from 10 - 30 and their sum")
ch = int(input("Enter your Choice from 1 - 7 = "))
match(ch):
    case 1: 
       _range = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
       n = int(input("Enter a number = "))
       if n in _range:
        print("True")
       else:
        print("False")
    case 2:
        for i in range(10,20,3):
            print("The Numbers are = ",i)
    case 3:
        n = int(input("Enter a Number = "))
        fact = 1
        for i in range(n,1,-1):
         fact = fact * i
        print("The Factorial of ", n, " is = ", fact)
    case 4:
        n = int(input("Enter the Nuber of Terms of the Seies = "))
        a = 0
        b = 1
        print(a)
        print(b)
        for i in range(1,n + 1):
            c = a + b
            print(c)
            a = b
            b = c
    case 5:
        print("The First 10 Natural is = ")
        for i in range(1,11):
            print(i)
    case 6:
        sum = 0
        for i in range(20, 41):
         square = i ** 2
         print("The square of ", i," is = ",square)
         sum = sum + square
        print("The total sum of all squares is = ",sum)
    case 7:
       sum = 0
       print("The multiples are:")
       for i in range(10, 31):
        if i % 3 != 0:
          continue
        print(i, end =" ")
        multiples = i
        sum = sum + i
    #    print("The Multiples of 3 from 10 - 30 are = ",multiples)
       print("\nAnd their sum is = ",sum)
    case default:
        print("Invalid Choice! Enter Your Correct Choice Again!")