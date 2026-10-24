def SI(p,r,t):
    si = ((p * r * t)/100)
    return f"The SI is = {si}"
p = int(input("Enter a Princpal Amount = "))
r = int(input("Enter a Rate of Interest = "))
t = int(input("Enter a Time Period = "))
print(SI(p,r,t))