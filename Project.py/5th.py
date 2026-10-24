num = int(input("Enter a Number = "))
temp = num
rev = 0
while(num>0):
    d = num % 10
    rev = (rev * 10) + d
    num = num // 10
if(temp == rev):
    print(temp, "is a Palindrome Number.")
else:
    print(temp, "is not a Palindrome Number.")
