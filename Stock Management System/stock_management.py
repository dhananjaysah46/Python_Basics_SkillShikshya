# A mini Console-Based Stock Management System using Python Dictionary

# Dictionary to hold stock information
stock = {}

def display_stock():
    if stock == {}:
        print("No Products in Stock.")
    else:
        for product, details in stock.items():
            print(f"Product: {product}, Quantity: {details['quantity']}, Price: {details['price']}")

def add_product(product_id, product_name, price, quantity):
    if product_id in stock:
        print("Product already exists.")
    else:
        stock[product_id] = {'name': product_name, 'price': price, 'quantity': quantity}
        print(f"Product {product_name} added successfully.")

def update_quantity(product_id, quantity):
    if product_id in stock:
        stock[product_id]['quantity'] = quantity
        print(f"Updated quantity of {stock[product_id]['name']} to {quantity}.")
        if product_id not in stock:
            print("Error, Product not found.")
        else:
            stock[product_id]['quantity'] += quantity
            print(f"Updated quantity of {stock[product_id]['name']} to {stock[product_id]['quantity']}.")

def sell_product(product_id, quantity):
    if product_id in stock:
        if product_id not in stock:
            print("Error, Product not found.")
        else:
            if quantity >= stock[product_id]['quantity']:
                print("Insufficient stock.")
            else:
                stock[product_id]['quantity'] -= quantity

                total_price = stock[product_id]['price'] * quantity
                print(f"Sold {quantity} pcs of {stock[product_id]['name']}. Total price: {total_price}.")      
    else:
        print("Error, Product not found.")

def main():
    while True:
        print("\nStock Management System")
        print("1. Display Stock")
        print("2. Add Product")
        print("3. Update Quantity")
        print("4. Sell Product")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            display_stock()
        elif choice == '2':
            product_id = input("Enter Product ID: ")
            product_name = input("Enter Product Name: ")
            price = float(input("Enter Product Price: "))
            quantity = int(input("Enter Product Quantity: "))
            add_product(product_id, product_name, price, quantity)
        elif choice == '3':
            product_id = input("Enter Product ID: ")
            quantity = int(input("Enter New Quantity: "))
            update_quantity(product_id, quantity)
        elif choice == '4':
            product_id = input("Enter Product ID: ")
            quantity = int(input("Enter Quantity to Sell: "))
            sell_product(product_id, quantity)
        elif choice == '5':
            print("Exiting Console-based Stock Management System.")
            break
        else:
            print("Invalid choice. Please try again.")
# Run the main function
main()