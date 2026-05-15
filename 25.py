class Coffee:

    def __init__(self,name,price):
        self.name = name
        self.price = price


class Order: 

    def __init__(self):
        self.items = []

    def add_item(self,coffee):
        self.items.append(coffee)

        print(f"Added {coffee.name} to order.")

    def total(self):
        return sum(item.price for item in self.items)



    def show_order(self):
        if not self.items:
            print("Your order is empty.")
            return
        print("\n Your order:")
        for i,item in enumerate(self.items,1):
            print(f"{i}. {item.name} - ${item.price}")
        print(f"Total: ${self.total()}\n")
        
    def check_out(self):
        if not self.items:
            print("Your order is empty.")
            return
        print("Checking out...")
        self.show_order()
        confirm = input("Confirm order? (yes/no): ").strip().lower()    
        if confirm == 'yes':
            print("Order confirmed! Thank you for your purchase.")
            self.items.clear()
        else:
            print("Order cancelled.")


    def main():
        menu = [
            Coffee("Espresso", 2.5),
            Coffee("Latte", 3.5),
            Coffee("Cappuccino", 3.0),
            Coffee("Americano", 2.0),
            Coffee("Mocha", 4.0)
        ]
   
        order = Order()
        while True:
            print("\n-----coffee menu-----")
            for i, coffee in enumerate(menu, 1):
                print(f"{i}. {coffee.name} - ${coffee.price}")
            print("5. View Order")
            print("6. Check Out")
            print("7. Exit") 
            choice = input("Select an option: ").strip()
            if choice in ['1', '2', '3', '4']:
                order.add_item(menu[int(choice) - 1])