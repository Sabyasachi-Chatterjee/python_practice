num = int(input("Enter a Number = "))
x = num
rev = 0
while(num>0):
    d = num % 10
    rev = (rev * 10) + d
    num = num // 10

if(x == rev):
    print(x, "is a Palindrome Number.")
else:
    print(x, "is not a Palindrome Number.")
