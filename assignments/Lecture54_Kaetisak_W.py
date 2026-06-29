def login():
    username_input = input("Username : ")
    password_input = input("Password : ")
    if username_input == "admin" and password_input == "1234":
        show_menu()
        user_selected = menu_select()
        if user_selected == 1:
            price = int(input("Price (THB) : "))
            print(vat_calculator(price))
        elif user_selected == 2:
            print(price_calculator())
    else:
        return False

def show_menu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")

def menu_select():
    user_selected = int(input(">>"))
    return user_selected

def vat_calculator(total_price):
    vat = 7
    result = total_price + (total_price * vat / 100)
    return result

def price_calculator():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return vat_calculator(price1 + price2)

login()