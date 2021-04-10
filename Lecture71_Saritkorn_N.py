menuList = []
priceList = []
totalPrice = 0

def showBill():
    print("------ Restaurant ------")
    for number in range(len(menuList)):
        print(menuList[number],priceList[number],"Baht")
while True:
    menuName = input("Please Enter Manu: ")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = float(input("Price: "))
        menuList.append(menuName)
        priceList.append(menuPrice)
        totalPrice += menuPrice
showBill()
print("Total Price is",totalPrice,"Baht")