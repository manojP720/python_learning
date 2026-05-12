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
            print(f"- {item.name}: ${item.price:.2f}")