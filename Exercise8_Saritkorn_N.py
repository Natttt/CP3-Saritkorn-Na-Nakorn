product1 = "Mouse"
product2 = "Keyboard"
product3 = "USB Flash Drive 16GB"

product1Price = 500
product2Price = 600
product3Price = 200

usernameInput = input("Username :")
passwordInput = input("Password :")
if usernameInput == "admin" and passwordInput == "1234":
    print("----- Welcome to Nat's Gadget Shop -----")
    print("Product List")
    print("1. ", product1, product1Price, "Baht")
    print("2. ", product2, product2Price, "Baht")
    print("3. ", product3, product3Price, "Baht")
    productInput = int(input("Please input Product ID: "))
    if productInput == 1:
        amount = int(input("Quantity :"))
        TotalPrice = amount*product1Price
        print(TotalPrice, "Baht")
    elif productInput == 2:
        amount = int(input("Quantity :"))
        TotalPrice = amount*product2Price
        print(TotalPrice, "Baht")
    elif productInput == 3:
        amount = int(input("Quantity :"))
        TotalPrice = amount * product3Price
        print(TotalPrice, "Baht")
    elif productInput > 3:
        print("Invalid Product ID")
    print("Thank you")
else:
    print("Login Fail")
