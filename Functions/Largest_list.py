def largest_list(l):
    largest = l[0]
    for i in range(1, len(l)):
        if i > largest:
            largest = i
    return largest
li = [8,5,3,2,1,6,8]
print(largest_list(li))