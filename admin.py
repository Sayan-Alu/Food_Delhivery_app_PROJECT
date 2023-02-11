

import json

class Food:
    def __init__(self, food_id, name, quantity, price, discount, stock):
        self.food_id = food_id
        self.name = name
        self.quantity = quantity
        self.price = price
        self.discount = discount
        self.stock = stock

    def __str__(self):
        return f"{self.food_id} - {self.name} ({self.quantity}) [INR {self.price}]"

class Admin:
    def __init__(self):
        self.food_items = []
        try:
            with open("food_data.json", "r") as f:
                data = json.load(f)
                for item in data:
                    self.food_items.append(Food(item["food_id"], item["name"], item["quantity"], item["price"], item["discount"], item["stock"]))
        except:
            pass

    def add_food_item(self, food):
        self.food_items.append(food)
        self.save_data()

    def edit_food_item(self, food_id, name=None, quantity=None, price=None, discount=None, stock=None):
        for food in self.food_items:
            if food.food_id == food_id:
                if name:
                    food.name = name
                if quantity:
                    food.quantity = quantity
                if price:
                    food.price = price
                if discount:
                    food.discount = discount
                if stock:
                    food.stock = stock
                self.save_data()
                return
        print("Food item not found.")

    def remove_food_item(self, food_id):
        for i, food in enumerate(self.food_items):
            if food.food_id == food_id:
                self.food_items.pop(i)
                self.save_data()
                return
        print("Food item not found.")

    def view_food_items(self):
        for food in self.food_items:
            print(food)

    def save_data(self):
        data = []
        for food in self.food_items:
            data.append({"food_id": food.food_id, "name": food.name, "quantity": food.quantity, "price": food.price, "discount": food.discount, "stock": food.stock})
        with open("food_data.json", "w") as f:
            json.dump(data, f)

def menu():
    print("1. Add new food item")
    print("2. Edit food item")
    print("3. View all food items")
    print("4. Remove food item")
    print("5. Quit")
    return int(input("Enter your choice: "))

def main():
    admin = Admin()
    while True:
        choice = menu()
        if choice == 1:
            food_id = len(admin.food_items) + 1
            name = input("Enter the name of the food item: ")




admin = Admin()

# Add new food items
admin.add_food_item(Food(1, "Tandoori Chicken", "3 pieces", 200, 5, 50))
admin.add_food_item(Food(2, "Chole Bhature", "1 plate", 50, 10, 40))
admin.add_food_item(Food(3, "Tuffel Cake", "500 gram", 900, 2, 60000))

# View all food items
print("All food items:")
admin.view_food_items()



'''# Edit a food item

print("\nEditing food item with ID 2")
admin.edit_food_item(2, price=55)


print("\nAll food items after editing:")
admin.view_food_items()

# Remove a food item

print("\nRemoving food item with ID 1")
admin.remove_food_item(1)

print("\nAll food items after removing:")
admin.view_food_items()'''