menuList = []
totalPrice = 0

def showBill():
    print("------ Restaurant ------")
    for number in range(len(menuList)):
        print(menuList[number][0],menuList[number][1],"Baht")
while True:
    menuName = input("Please Enter Manu: ")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = float(input("Price: "))
        menuList.append([menuName,menuPrice])
        totalPrice += menuPrice

showBill()
print("Total Price is",totalPrice,"Baht")