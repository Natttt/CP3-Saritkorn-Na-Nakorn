def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        return True
    else:
        return False
def showMenu():
    print("Done !")
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
def menuSelect():
    userSelected = int(input(">>"))
    return userSelected
def vatCalculator(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    return result
def priceCalculator():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return vatCalculator(price1 + price2)

if(login()):
    showMenu()
    selectmenu = menuSelect()
    if selectmenu == 1:
        if selectmenu == 1:
            totalPrice = int(input("Enter Price: "))
            vatCalculator(totalPrice)
            print("Price included Vat :", vatCalculator(totalPrice))
    if selectmenu == 2:
        print("Total Price included Vat :",priceCalculator())
else:
    print("Login Failed")
