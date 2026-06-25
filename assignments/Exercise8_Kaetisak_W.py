"""
ในการเข้าใช้งานโปรแกรมให้ผู้ล็อคอินโดยใช้ Username และ Password(ผู้เรียนกำหนดเอง)
หากสำเร็จ โปรแกรมจะขึ้นหน้าต้อนรับและแสดงรายการสินค้าพร้อมราคา (ผู้เรียนกำหนดเอง)
เมื่อเลือกสินค้าที่ต้องการเรียบร้อยแล้ว โปรแกรมจะถามจำนวนที่ต้องการซื้อ
หลังจากผู้ซื้อเลือกเรียบร้อยแล้ว โปรแกรมจะทำการแสดงสรุปราคารวมของรายการสั่งซื้อทั้งหมด
"""

usernameInput = input("Username :")
passwordInput = input("Password :")
if usernameInput == "admin" and passwordInput == "88888":
    print("Login successful!")
    print("Welcome to the store!")
    print("Here are our products:")
    print("1. Laptop - $500")
    print("2. Smartphone - $300")
    print("3. Mouse - $100")
    product = int(input("Enter the product number: "))
    quantity = int(input("Enter the quantity: "))
    price = 0
    if product == 1:
        price = 500
    elif product == 2:
        price = 300
    elif product == 3:
        price = 100
    total_price = price * quantity
    print(f"The total price is ${total_price}")
else:
    print("Login failed!")