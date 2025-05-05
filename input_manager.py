def get_main_menu_choice():
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
    # The while loop will keep prompting the user to select a menu option and will only stop once the user inputs a valid number
    while True:
        try:
            choice = int(
                input("Enter a menu option to navigate to [1-8]: "))
            if choice > 0 and choice <= 8:
                return choice   # Returning will break out of the loop as well as the method
            else:
                print("The number you provided is not within the range of menu options")
        except ValueError:
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
    choice = get_main_menu_choice()
    print("You Chose:", choice)
