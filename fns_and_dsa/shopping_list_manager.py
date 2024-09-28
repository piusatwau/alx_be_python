# a simple shopping list manager that allows users to add items, view the current list, and remove items.


def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            added_item = input("please write the name of the item to add: ").lower()
            shopping_list.append(added_item)            
        elif choice == '2':
            # Prompt for and remove an item
            removed_item = input("please enter the name of the item to remove: ")
            if removed_item in shopping_list:
                shopping_list.remove(removed_item)
                print(shopping_list)
            else:
                print(f"{removed_item.lower()} is not in the list.")

        elif choice == '3':
            # Display the shopping list
            display_menu()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()
    
    
