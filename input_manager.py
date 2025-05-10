def confirm_input(user_input):
    answer = input(f"Did you mean to enter '{user_input}'? ")
    if answer.lower().strip() == "yes" or answer.lower().strip() == "y":
        return True
    else:
        return False


def get_main_menu_choice():
    # The while loop will keep prompting the user to select a menu option and will only stop once the user inputs a valid number
    while True:
        try:
            choice = input(
                "Enter a menu option to navigate to [1-8]: ").strip()
            if confirm_input(choice):
                if int(choice) > 0 and int(choice) <= 8:
                    return choice   # Returning will break out of the loop as well as the method
                else:
                    print(
                        "The number you provided is not within the range of menu options")
        except ValueError:
            if choice.lower() == "add":
                return 1
            elif choice.lower() == 'remove':
                return 2
            elif choice.lower() == 'update':
                return 3
            elif choice.lower() == "search":
                return 4
            elif choice.lower() == "view":
                return 5
            elif choice.lower() == "save":
                return 6
            elif choice.lower() == "load":
                return 7
            elif choice.lower() == "exit":
                return 8
            else:
                print(
                    "Please type the number alone to indicate which menu option you would like to use.")


def get_item_details():
    item_name = input("Please provide an item name: ")
    quantity = input("Please provide a quantity: ")
    return (item_name, quantity)


def get_search_term():
    search_term = input("Enter a word to search for: ")
    return search_term


if __name__ == "__main__":
    print("""
*****************************
            Menu
*****************************
1: Add items
2: Remove items
3: Update item quantities
4: Search for items
5: View inventory statistics
6: Save inventory to file
7: Load inventory from file
8: Exit
          """)
    choice = get_main_menu_choice()
    print("You Chose:", choice)
    item = get_item_details()
    print("Here is the item info", item)
    search = get_search_term()
    print("Searching for:", search)
