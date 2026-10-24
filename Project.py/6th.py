list = [1,2,3,4,5,6,7,8,9,10] # a list containing a combo of even and odd numbers
sum_even = sum_odd = 0

# FOR LOOP 1
# for elements in list:
#     if elements % 2 == 0:
#         sum_even += elements
#     else:
#         sum_odd += elements

# FOR LOOP 2
for i in range(0, len(list)):
    if list[i] % 2 == 0:
        sum_even += list[i]
    else:
        sum_odd += list[i]

print("The sum of all even numbers:",sum_even)
print("The sum of all odd numbers:", sum_odd)
#