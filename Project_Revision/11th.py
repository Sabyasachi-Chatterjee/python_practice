def find_extremes(l):
    s = l[0]
    l = l[0]
    for i in l:
        if i < s:
            s = i
        if i > l:
            l = i
    return s,l        
def main():
    list = [2,8,9,4,11,5,6]
    s,l = find_extremes(list)
    print("The Smallest No. is = ", s, "and the Largest No. is = ", l)
if __name__=="__main__":
    main()

        

           
    