def multiples(n):
    l = [56,72,54,3,55,25,81]
    for i in range(0,7):
        if(l[i] % n == 0):
            return l[i]
        else:
            return "none"
def main():
    n = int(input("Enter a Number = "))
    result = multiples(n)
    print("The Multiples of ",n, "are = ", result)
if __name__ == "__main__":
    main()