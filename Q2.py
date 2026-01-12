from threading import Lock

class Coffee:
    def __init__(self, name, price, ingredients):
        self.name = name
        self.price = price
        self.ingredients = ingredients

class VendingMachine:
    def __init__(self):
        self.coffees = {
            "espresso": Coffee("Espresso", 2.5, {"coffee": 1, "water": 1}),
            "cappuccino": Coffee("Cappuccino", 3.5, {"coffee": 1, "milk": 2, "water": 1}),
            "latte": Coffee("Latte", 4.0, {"coffee": 1, "milk": 3, "water": 1})
        }
        self.inventory = {"coffee": 10, "milk": 10, "water": 10}
        self.lock = Lock()
    
    def show_menu(self):
        print("\n=== Coffee Menu ===")
        for name, coffee in self.coffees.items():
            print(f"{name.capitalize()}: ${coffee.price}")
    
    def check_inventory(self, coffee):
        for item, qty in coffee.ingredients.items():
            if self.inventory.get(item, 0) < qty:
                return False
        return True
    
    def update_inventory(self, coffee):
        for item, qty in coffee.ingredients.items():
            self.inventory[item] -= qty
    
    def dispense(self, coffee_name, payment):
        with self.lock:
            if coffee_name not in self.coffees:
                return "Invalid coffee type"
            
            coffee = self.coffees[coffee_name]
            
            if payment < coffee.price:
                return f"Insufficient payment. Need ${coffee.price}"
            
            if not self.check_inventory(coffee):
                return "Ingredients low. Cannot dispense"
            
            self.update_inventory(coffee)
            change = payment - coffee.price
            
            return f"Dispensing {coffee.name}. Change: ${change:.2f}"
    
    def check_low_inventory(self):
        low = [item for item, qty in self.inventory.items() if qty < 3]
        if low:
            print(f"Warning: Low inventory - {', '.join(low)}")


vm = VendingMachine()
vm.show_menu()
print(vm.dispense("espresso", 3.0))
print(vm.dispense("latte", 5.0))
vm.check_low_inventory()