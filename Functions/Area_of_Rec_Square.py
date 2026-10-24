def Area_Rect(l,b):
    area_1 = l * b
    return f"The Area of Rectangle is = {area_1}"
def Area_Squa(s):
    area_2 = s ** 2
    return f"The Area of Square is = {area_2}"
print("Menu - ")
print("Press 1 to Find the Area of a Rectangle - ")
print("Press 2 to Find the Area of a Square - ")
ch = int(input("Enter Your Choice = "))
match(ch):
    case 1:
        l = int(input("Enter the Length of the Rectangle = "))
        b = int(input("Enter the Breadth of the Rectangle = "))
        print(Area_Rect(l,b))
    case 2:
        s = int(input("Enter the Side of a Square = "))
        print(Area_Squa(s))
    case default:
        print("Please Enter a Valid Choice again !!!")