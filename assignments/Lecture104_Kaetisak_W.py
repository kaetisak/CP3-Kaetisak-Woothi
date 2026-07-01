class Customer:
    name = ""
    lastName = ""
    age = 0

    def addCart(self):
        print("Added to %s %s's cart" % (self.name, self.lastName))


customer1 = Customer()
customer1.name = "Bob"
customer1.lastName = "Baby"
customer1.age = 8
customer1.addCart()

customer2 = Customer()
customer2.name = "Oliver"
customer2.lastName = "Smith"
customer2.age = 28
customer2.addCart()

customer3 = Customer()
customer3.name = "Emma"
customer3.lastName = "Johnson"
customer3.age = 34
customer3.addCart()

customer4 = Customer()
customer4.name = "William"
customer4.lastName = "Brown"
customer4.age = 45
customer4.addCart()