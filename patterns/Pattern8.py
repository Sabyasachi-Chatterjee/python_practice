#
#*
#*#
#*#*
#*#*#
# n lines


n = int(input("Enter the Number of Lines = "))
# for i in range(0,n + 1):
#     for j in range(1,i):
#         for k in range(1,j):
#          print("#")
#         print("*")
#     print("#")
for i in range(1,n+1):
    for j in range(1,i+1):
        if(j % 2 == 0):
            print("*", end= " ")
        else:
            print("#",end=" ")
    print()