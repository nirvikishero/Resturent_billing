from foods import food
import difflib

class Client:
    def __init__(self, n: str, a: int):
        self.name: str = n
        self.age: int = a
        self.order: list = []
        self.rate: list = []
        self.price: list = []
        self.order_number: int = 0
        self.no_of_items: list = []

    def display_details(self):
        # Writing the details to a text file
        with open("client_order.txt", "w") as f:
            f.write(f"""
XYZ Restaurant Pvt. Ltd.
Address: ......
Phone No.: 09090909

Name: {self.name}
Age: {self.age}

S.N.  |  Particulars     |  Rate  |  Qt.  |  Price
--------------------------------------------------
""")
            for i in range(self.order_number):
                item_price = self.rate[i] * self.no_of_items[i]
                """Space creating in the between """
                f.write(f"{i+1:<5} |  {self.order[i]:<15} |  {self.rate[i]:<6} |  {self.no_of_items[i]:<4} |  {item_price:<7}\n")

        # Reading from the text file and printing the content
        with open("client_order.txt", "r") as f:
            print(f.read())

# Function to print hardcopy
def print_hardcopy(file_name):
    import os
    os.startfile(file_name, "print")  # For Windows, use the lp command for macOS/Linux

# Input client details
nam = input("Enter the name of client: ")
ag = int(input("Enter the age: "))
nam = nam.capitalize()
client = Client(nam, ag)

# Taking orders
while True:
    o = input("Enter the order from client (type 'exit' to finish): ").lower()
    
    if o == "exit":
        break
    elif o in food:
        client.order.append(o)
        client.rate.append(food[o])
        qty = int(input(f"Enter quantity for {o}: "))
        client.no_of_items.append(qty)
        client.order_number += 1
    else:
        # Check for misspellings
        closest_match = difflib.get_close_matches(o, food.keys(), n=1)
        
        if closest_match:
            suggestion = closest_match[0]
            print(f"Did you mean '{suggestion}'? (yes/no)")
            response = input().lower()
            if response == "yes":
                client.order.append(suggestion)
                client.rate.append(food[suggestion])
                qty = int(input(f"Enter quantity for {suggestion}: "))
                client.no_of_items.append(qty)
                client.order_number += 1
            else:
                print(f"{o} is not available on the menu.")
        else:
            print(f"{o} is not available on the menu.")

# Display the client details and store them in a text file
client.display_details()

# Print a hardcopy
print_hardcopy("client_order.txt")
