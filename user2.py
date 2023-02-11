
import json
from admin3 import Admin

class User:
    def __init__(self):
        self.user_data = {}
    
    def register(self):
        print("Welcome to Food Ordering Application!")
        print("Please enter the following details for registration:")
        
        full_name = input("Full Name: ")
        phone_number = input("Phone Number: ")
        email = input("Email: ")
        address = input("Address: ")
        password = input("Password: ")
        
        self.user_data["full_name"] = full_name
        self.user_data["phone_number"] = phone_number
        self.user_data["email"] = email
        self.user_data["address"] = address
        self.user_data["password"] = password
        
        with open("user_data.json", "w") as f:
            json.dump(self.user_data, f)
        
        print("\nRegistration Successful!\n")
    
    def login(self):
        with open("user_data.json", "r") as f:
            self.user_data = json.load(f)
        
        entered_email = input("Enter your email: ")
        entered_password = input("Enter your password: ")
        
        if entered_email == self.user_data["email"] and entered_password == self.user_data["password"]:
            print("\nLogin Successful!\n")
            return True
        else:
            print("\nLogin Failed! Incorrect Email or Password.\n")
            return False
    
    def place_new_order(self, admin):
        if self.login():
            print("Place New Order")
            print("----------------")
            if hasattr(admin, 'food_items'):
                if len(admin.food_items) > 0:
                    print("\nThe following food items are available in the menu:\n")
                    for i, food in enumerate(admin.food_items, start=1):
                        print(f"{i}. {food['Name']} ({food['Quantity']}) [INR {food['Price']}]")

                    food_numbers = list(map(int, input("\nEnter the food numbers you want to order (separated by space): ").split()))
                    selected_food = [admin.food_items[number-1] for number in food_numbers if number-1 < len(admin.food_items)]

                    if len(selected_food) > 0:
                        print("\nThe following food items have been selected:")
                        for i, food in enumerate(selected_food, start=1):
                            print(f"{i}. {food['Name']} ({food['Quantity']}) [INR {food['Price']}]")

                        confirm_order = input("\nDo you want to place the order (yes/no)? ")
                        if confirm_order == "yes":
                            print("\nOrder Placed Successfully!\n")
                            return selected_food
                        else:
                            print("\nOrder Cancelled!\n")
                            return []
                    else:
                        print("\nInvalid food numbers. Please try again.\n")
                else:
                    print("\nNo food items available in the menu.\n")
            else:
                print("\nThe admin object does not have the 'food_items' attribute.\n")
        else:
            return []

    def view_order_history(self):
        if self.login():
            try:
                with open("order_history.json", "r") as f:
                     order_history = json.load(f)
                print("\nOrder History\n-------------")
                for order_id, order_data in order_history.items():
                     print(f"Order ID: {order_id}")
                     print(f"Date: {order_data['Date']}")
                     print(f"Food Items: {order_data['Food Items']}")
                     print(f"Total Cost: INR {order_data['Total Cost']}\n")
               
            except:
                print("\nNo order history found.\n")
            
        else:
            print("\nPlease login to view your order history.\n")
        
               
        
            
def main():
    admin = Admin() 
    user = User() 

    while True:
        print("\nWelcome to Food Ordering Application\n")
        print("1. Register")
        print("2. Place a new order")
        print("3. View order history")
        print("4. Exit")
        choice = int(input("\nEnter your choice: "))
    
        if choice == 1:
            user.register()
        elif choice == 2:
            selected_food = user.place_new_order(admin)
            if selected_food:
                admin.update_order_history(selected_food)
        elif choice == 3:
            user.view_order_history()
        elif choice == 4:
            break
        else:
            print("\nInvalid choice. Please enter a valid number (1-4).\n") 
        
          
if __name__ == "__main__":
    main()

   


