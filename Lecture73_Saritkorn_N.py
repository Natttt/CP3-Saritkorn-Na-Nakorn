systemMenu = {"ไก่ทอด": 35, "เป็ดทอด": 45, "ปลาทอด": 55, "ผักทอด": 20}
menuList = []
totalPrice = []

def showBill():
    print("------ Restaurant ------")
    for number in range(len(menuList)):
        print(menuList[number][0],menuList[number][1],"Baht")
        totalPrice.append(menuList[number][1])
while True:
    menuName = input("Please Enter Manu: ")
    if(menuName.lower() == "exit"):
        break
    else:
        menuList.append([menuName,systemMenu[menuName]])


showBill()
print("Total Price is",sum(totalPrice),"Baht")