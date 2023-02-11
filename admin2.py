


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
    print("1. Add food item")
    print("2. Edit food item")
    print("3. Remove food item")
    print("4. View food items")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    return choice

def main():
    admin = Admin()
    while True:
        choice = menu()
        if choice == 1:
            food_id = len(admin.food_items) + 1
            name = input("Enter the name of the food item: ")
            quantity = input("Enter the quantity of the food item: ")
            price = float(input("Enter the price of the food item: "))
            discount = float(input("Enter the discount on the food item (if any): "))
            stock = int(input("Enter the stock of the food item: "))
            food = Food(food_id, name, quantity, price, discount, stock)
            admin.add_food_item(food)
        elif choice == 2:
            food_id = int(input("Enter the food ID: "))
            name = input("Enter the new name of the food item (if any): ")
            quantity = input("Enter the new quantity of the food item (if any): ")
            price = input("Enter the new price of the food item (if any): ")
            if price.isdigit():
                price = float(price)
            else:
                price = None
            discount = input("Enter the new discount on the food item (if any): ")
            if discount.isdigit():
                discount = float(discount)
            else:
                discount = None
            stock = input("Enter the new stock of the food item (if any): ")
            if stock.isdigit():
                stock = int(stock)
            else:
                stock = None
            admin.edit_food_item(food_id, name, quantity, price, discount, stock)
        elif choice == 3:
            food_id = int(input("Enter the food ID: "))
            admin.remove_food_item(food_id)
        elif choice == 4:
            admin.view_food_items()
        elif choice == 5:
            break
        else:
            print("Invalid choice.")       


if __name__ == "__main__":
    main()



















