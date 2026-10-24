list = [1,2,3,4,5,6,7,8,9,10]
sumeven = sumodd = 0
for i in range(0, len(list)):
    if list[i] % 2 == 0:
        sumeven += list[i]
    else:
        sumodd += list[i]

print("The sum of all even numbers:",sumeven)
print("The sum of all odd numbers:", sumodd)