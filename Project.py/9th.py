# Input elements in list via user
#  l = []
# for i in range(0,6):
#     a = int(input("Enter a Number = "))
#     l.append(a)
# print(l)

new_list = []
l = [3,5,0,7,1,6]
for i in range(0,6):
    l[i] += 2
    new_list.append(l[i])
print(new_list, end =" ")
#