def vatCalculate(totalPrice):
    result=totalPrice+(totalPrice*7/100)
    return result
price=int(input("Please Enter Price: "))
print("Price include Vat = ", vatCalculate(price))
