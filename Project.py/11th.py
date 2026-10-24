def find_extremes(l):
    smallest = l[0]
    largest = l[0]
    for i in l:
        if i < smallest:
            smallest = i
        if i > largest:
            largest = i
    return smallest,largest        
def main():
    list = [2,8,9,4,11,5,6]
    s,l = find_extremes(list)
    print("The Smallest No. is = ", s, "and the Largest No. is = ", l)
if __name__=="__main__":
    main()

        

           
    