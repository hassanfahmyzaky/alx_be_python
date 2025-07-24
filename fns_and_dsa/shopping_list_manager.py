# shopping_list_manager.py

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []  # Initialize an empty shopping list
    
    while True:
        display_menu()  # Display the menu

        # Ensuring the choice input is treated as a number (1 to 4)
        choice = input("Enter your choice: ").strip()
        
        # Check if the input is a valid integer and within range
        if choice.isdigit() and 1 <= int(choice) <= 4:
            choice = int(choice)  # Convert to integer after validation
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
            continue  # Skip the rest of the loop if the input is not valid

        if choice == 1:
            # Add item to the shopping list
            item = input("Enter the item to add: ").strip()  # Exact prompt format
            shopping_list.append(item)
            print(f"'{item}' has been added to the shopping list.")

        elif choice == 2:
            # Remove item from the shopping list
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from the shopping list.")
            else:
                print(f"'{item}' is not in the shopping list.")
        
        elif choice == 3:
            # View the current shopping list
            if shopping_list:
                print("Shopping List:")
                for item in shopping_list:
                    print(f"- {item}")
            else:
                print("Your shopping list is empty.")
        
        elif choice == 4:
            # Exit the program
            print("Goodbye!")
            break
        
if __name__ == "__main__":
    main()
