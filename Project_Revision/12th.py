def leap(year):
    if(year % 4 == 0 or year % 400 == 0):
        print (year, " is a leap year.")
    else:
        print (year, " is not a leap year.")
def main():
    year = int(input("Enter a Year = "))
    leap(year)
if __name__ == "__main__":
    main()