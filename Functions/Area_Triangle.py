def Area_Perimeter_Triangle(b,h,x,y,z):
    area = (((b * h)*1)/2)
    perimeter = (x + y + z)
    return f"""The Area of Tringle is = {area} 
    The Perimeter of Triangle is = {perimeter}"""
b = int(input("Enter a Base of Triangle = "))
h = int(input("Enter a Height of Triangle = "))
x = int(input("Enter the First Side of a Triangle = "))
y = int(input("Enter the Second Side of a Triangle = "))
z = int(input("Enter the Third Side of a Triangle = "))
print(Area_Perimeter_Triangle(b,h,x,y,z))
