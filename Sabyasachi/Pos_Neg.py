def Posneg(n):
    if(n>0):
        return "Positive"
    elif(n<0):
        return "Negative"
    else:
        return "Zero"
def main():
    n = int(input("Enter a Number = "))
    Result = Posneg(n)
    print(n, "is a ", Result, "Number.")
if __name__ == "__main__":
    main()