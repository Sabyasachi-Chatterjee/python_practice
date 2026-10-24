#     5        
#    45
#   345 
#  2345
# 12345


a = int(input("Enter the No. of Lines = "))
for i in range(a,0,-1):
    for j in range(i-1,0,-1):
          print(" ", end="")
    for k in range(i,a+1):
            print(k, end= "")

    print()