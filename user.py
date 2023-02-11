import json
from admin import Admin, Food

class User:
    def __init__(self):
        self.admin = Admin()
        self.full_name = None
        self.phone_number = None
        self.email = None
        self.address = None
        self.password = None

    def register(self):
        self.full_name = input("Enter your full name: ")
        self.phone_number = input("Enter your phone number: ")
        self.email = input("Enter your email: ")
        self.address = input("Enter your address: ")
        self.password = input("Enter your password: ")
        with open("user_data.json", "w") as f:
            json.dump({"full_name": self.full_name, "phone_number": self.phone_number, "email": self.email, "address": self.address, "password": self.password}, f)

    def login(self):
        try:
            with open("user_data.json", "r") as f:
                data = json.load(f)
                if data["password"] == self.password:
                    return True
                else:
                    print("Incorrect password.")
                    return False
        except:
            print("User not found.")
            return False

    def place_new_order(self):
        self.admin.view_food_items()
        food_ids = input("Enter the food IDs you want to order, separated by commas: ")
        food_ids = [int(x) for x in food_ids.split(",")]
        food_items = []
        for food_id in food_ids:
            for food in self.admin.food_items:
                if food.food_id == food_id:
                    food_items.append(food)
        for food in food_items:
            print(food)
        confirm = input("Do you want to place this order? (y/n) ")
        if confirm == "y":
            print("Order placed.")
        else:
            print("Order cancelled.")

user = User()
while True:
    action = input("What would you like to do? (register/login/exit) ")
    if action == "register":
        user.register()
    elif action == "login":
        if user.login():
            while True:
                action = input("What would you like to do? (place order/exit) ")
                if action == "place order":
                    user.place_new_order()
                elif action == "exit":
                    break
                else:
                    print("Invalid command.")
    elif action == "exit":
        break
    else:
        print("Invalid command.")