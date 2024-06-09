# Creates an initial list at program launch containing 0 items, allows user to add their own
items_list = []

# Function that adds items to the list
def add_item():
    item = input("Enter item name: ")
    price = float(input("Enter item price: "))
    items_list.append((item, price))

# Function to clears ALL items from the list
def clear_items():
    items_list.clear()
    print("All items cleared.")

# Function to display all added items and calculate total price
def display_items():
    if not items_list:
        print("No items in the list.")
    else:
        total = 0
        print("Items in the list:")
        for item, price in items_list:
            print(f"{item}: ${price}")
            total += price
        print('                        ')  
        print('-----------')  
        print('              ')
        print(f"Total: ${total}")
        input("Press Enter to continue...")

# Main for loop used to run the POS program
#Options dictionary to be later used in for each loop
options = {
    '1': add_item,
    '2': clear_items,
    '3': display_items,
    '4': lambda: print("Exiting POS program. Thank you!") #Couldnt find a workaround for this, it is used to exit the program
}

sentinel = '4' #sentinel variable
while True:
    print("\nOptions:")
    for key, value in options.items():
        print(f"{key}. {value.__name__.replace('_', ' ').title()}")

    choice = input("Enter option: ")

    # Loop through the options dictionary using a for each loop
    for key, func in options.items():
        if choice == key:
            func()  # Execute the desired function
            break  # Exit the loop after executing the function

    if choice == sentinel:
        break  # Exit the main loop when the sentinel value is entered
    elif choice not in options:
        print("Invalid option. Please try again.")
#This one made me sad honestly, i dont like coding :)        