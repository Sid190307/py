class Products:
    def __init__(self,ID,name,price):
        self.ID = ID
        
        self.name = name
        self. price = price

    def display_product(self):
        print("Product id: ",self.ID)
        print("Product name: ",self.name)
        print("Product price: ",self.price)
        print()

    def get_product(num):
        product_list = []
        print("\nenter the details\n") for i in range (num):
            print("Product ",(i+1))
            p_id = input("Enter id: ")
            p_name = str(input("Enter the name: "))
            p_price = int(input("Enter the price: "))

            new_products = Products(p_id,p_name,p_price)
            product_list.append(new_products)
        return product_list
    
    def show_product(products):
        for prod in products:
            print(prod.display_product())

    def show_price_products(products):
        x = int(input("Enter the minimum price: "))
        print("products above the price ",x," are: ")
        found = False

        for prod in products:
            if prod.price > x:
                print(prod.display_product())
                found = True

        if not found:
            print("No products available above the price ",x)

num = int(input("Enter the number of products you are going to input: "))
all_products = Products.get_product(num)

while True:
    print("\nMenu")
    print("1. Show all products")
    print("2. Show all products above a certain price")
    print("3. Exit")
    ch = int(input("enter the choice: "))
    print()
    
    if ch == 1:
        Products.show_product(all_products)
    elif ch == 2:
        Products.show_price_products(all_products)
    elif ch == 3:
        break
    else:
        print("INVALID CHOICE!!!! PLEASE TRY AGAIN.")
