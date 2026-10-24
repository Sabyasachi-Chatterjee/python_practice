# PROBLEM STATEMENT:
# CODE:
mtly_salary = int(input("Enter Your Monthly Salary = $ "))
yrly_salary = (mtly_salary * 12)
if(yrly_salary <= 250000.00):
    icm_tax = ((0 * yrly_salary)/100)
elif(yrly_salary > 250000.00 and yrly_salary <= 500000.00):
    icm_tax = ((10 * yrly_salary)/100)
elif(yrly_salary > 500000.00 and yrly_salary <= 1000000.00):
    icm_tax = ((20 * yrly_salary)/100)
else:
    icm_tax = ((30 * yrly_salary)/100)
print(f"Your Monthly Salary is = $ {mtly_salary}, Yearly Salary is = $ {yrly_salary}, and Your Income Tax Deducted is = $ {icm_tax}")
# OUTPUT:
# Enter Your Monthly Salary = $ 15000
# Your Monthly Salary is = $ 15000, Yearly Salary is = $ 180000, and Your Income Tax Deducted is = $ 0.0
# Enter Your Monthly Salary = $ 250000
# Your Monthly Salary is = $ 250000, Yearly Salary is = $ 3000000, and Your Income Tax Deducted is = $ 900000.0