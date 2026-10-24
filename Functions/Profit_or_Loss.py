def ProLoss(cp,sp):
    if(cp > sp):
        result = "Loss"
        result_value = (cp - sp)
    else:
        result = "Profit"
        result_value = (sp - cp)
    return f""" The Result is = {result}
    The Result Value is = {result_value}"""
cp = int(input("Enter the Cost Price = "))
sp = int(input("Enter the Selling Price = "))
print(ProLoss(cp,sp))