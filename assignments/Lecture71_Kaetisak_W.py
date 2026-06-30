menuList = []
priceList = []

def showBill():
    print("My Food".center(20, "-"))
    for number in range(len(menuList)):
        print(menuList[number], priceList[number])
    print("Total :",sum(priceList))

while True:
    menuName = input("Please Enter Menu :")
    if (menuName.lower() == "exit"):
        break
    else:
        menuPrice = int(input("Price :"))
        menuList.append(menuName)
        priceList.append(menuPrice)
showBill()