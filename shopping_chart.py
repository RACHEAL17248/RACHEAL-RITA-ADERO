class Product:
    def __init__(self, product_name, price, quantity_in_stock):
        # Instance variables for Product
        self.product_name = product_name
        self.price = price
        self.quantity_in_stock = quantity_in_stock

    def display_product_info(self):
        """Displays product details."""
        print(f"Product: {self.product_name}, Price: ${self.price}, Stock: {self.quantity_in_stock}")

class ShoppingCart:
    # Class variable
    total_carts = 0

    def __init__(self):
        self.items = []  # A list of tuples (Product, Quantity)
        ShoppingCart.total_carts += 1  # Increment total carts on creation

    def add_to_cart(self, product, quantity):
        """Adds a product to the cart if the quantity is available."""
        if quantity <= product.quantity_in_stock:
            # Add product and quantity to the cart
            self.items.append((product, quantity))
            product.quantity_in_stock -= quantity  # Update stock
            print(f"Added {quantity} of {product.product_name} to the cart.")
        else:
            print(f"Insufficient stock for {product.product_name}.")

    def remove_from_cart(self, product):
        """Removes a product from the cart."""
        for item in self.items:
            if item[0] == product:
                self.items.remove(item)
                product.quantity_in_stock += item[1]  # Restock the removed quantity
                print(f"Removed {product.product_name} from the cart.")
                break
        else:
            print(f"{product.product_name} not found in the cart.")

    def display_cart(self):
        """Displays all items in the cart."""
        if not self.items:
            print("Cart is empty.")
        else:
            print("Items in your cart:")
            for item in self.items:
                product, quantity = item
                print(f"{product.product_name}: {quantity} units @ ${product.price} each")

    def calculate_total(self):
        """Calculates and returns the total price of items in the cart."""
        total = sum(product.price * quantity for product, quantity in self.items)
        print(f"Total amount: ${total:.2f}")
        return total

product1 = Product("Laptop", 2500.00, 50)
product2 = Product("Headphones", 900.00, 30)
product3 = Product("Smartphone", 1000.00, 25)

# Display product information
product1.display_product_info()
product2.display_product_info()
product3.display_product_info()

cart1 = ShoppingCart()
cart2 = ShoppingCart()

# Cart 1 operations
cart1.add_to_cart(product1, 1)  # Add 1 Laptop to cart1
cart1.add_to_cart(product2, 2)  # Add 2 Headphones to cart1
cart1.remove_from_cart(product1)  # Remove Laptop from cart1
cart1.add_to_cart(product3, 2)  # Add 2 Smartphones to cart1

# Cart 2 operations
cart2.add_to_cart(product2, 3)  # Add 3 Headphones to cart2
cart2.add_to_cart(product1, 2)  # Add 2 Laptops to cart2

print("\nCart 1 details:")
cart1.display_cart()
cart1.calculate_total()

print("\nCart 2 details:")
cart2.display_cart()
cart2.calculate_total()
