import input_manager # get_main_menu_choice() - get_item_details() - get_search_term()
import validator # validate_item_name(name) - validate_quantity(qty)
import inventory_operations # add_item(inventory, item_name, quantity) - remove_item(inventory, item_name) - update_quantity(inventory, item_name, new_qty)
import search # - search_item(inventory, search_term)
import stats # - get_inventory_count(inventory) - get_total_quantity(inventory) - get_top_item(inventory)
import persistence # - save_inventory(inventory, filename="inventory_data.txt") - load_inventory(filename="inventory_data.txt")

# 1 - add_item - adds a item to the inventory
# Modules needed to run (Input_manager, validator, Inventory_operations)
def add_item(inventory):
    try:
        item_name, qty = input_manager.get_item_details()

        valid_name, name_msg = validator.validate_item_name(item_name)
        if not valid_name:
            print(f'{name_msg}')
            return False
        
        valid_qty, qty_msg = validator.validate_quantity(qty)
        if not valid_qty:
            print(f'{qty_msg}')
            return False
    except Exception as e:
        print(f'Failed to get item details: {e}')
        return False
    
    inventory_operations.add_item(inventory, item_name, int(qty))
    return True

# 2 - remove_item - removes a item from the inventory
# Modules needed to run (Input_manager, validator, Inventory_operations)
def remove_item(inventory):
    try:
        item_name = input_manager.remove_item_name()

        valid_name, name_msg = validator.validate_item_name(item_name)
        if not valid_name:
            print(f'{name_msg}')
            return False
        
    except Exception as e:
        print(f'Failed to get item details: {e}')
        return False
    
    inventory_operations.remove_item(inventory, item_name)
    return True

# 3 - update_item - updates a current item in the inventory
# Modules needed to run (Input_manager, validator, Inventory_operations)
def update_item(inventory):
    try:
        item_name, qty = input_manager.get_item_details()

        valid_name, name_msg = validator.validate_item_name(item_name)
        if not valid_name:
            print(f'{name_msg}')
            return False
        
        valid_qty, qty_msg = validator.validate_quantity(qty)
        if not valid_qty:
            print(f'{qty_msg}')
            return False
    except Exception as e:
        print(f'Failed to get item details: {e}')
        return False
    
    inventory_operations.update_quantity(inventory, item_name, int(qty))
    return True
    # try:
    #     valid_update_item = inventory_operations.update_quantity(inventory, item_name, qty)
    #     if not valid_update_item:
    #         print(f"The item '{item_name}' could not be updated")
    #         return False
    #     print(f"'{item_name}' has been successfully removed")
    #     return True
    # except Exception as e:
    #     print(f'Failed to update Item quantity: {e}')
    #     return False

# 4 - search items - prints a list of items which name contain a given search_term
# modules required - (Input_manager, validator, search)
def search_items(inventory):
    try:
        search_term = input_manager.get_search_term()

        valid_name, name_msg = validator.validate_item_name(search_term)
        if not valid_name:
            print(f'{name_msg}')
            return False
        matches = search.search_item(inventory, search_term)

    except Exception as e:
        print(f'Failed to search items: {e}')
        return False
    
    if matches == -1:
        return -1
    if not matches:
        print(f"There were no matches with '{search_term}'")
    else:
        print("\nItem(s) Found: ")
        for index, item_dict in enumerate(matches):
            print(f'{index+1}) {item_dict}')
    return True

# 5 - show stats - prints out the distinct number of items in the inventory, sum of all items, and the item with the highest quantity
# modules required - (stats)
def show_stats(inventory):
    try:
        inventory_count = stats.get_inventory_count(inventory)
        total_quantity = stats.get_total_quantity(inventory)
        top_item = stats.get_top_item(inventory)
        avg_qty = stats.get_average_quantity(inventory)
    except Exception as e:
        print(f'Failed to load stats: {e}')
        return False
    
    if not top_item or avg_qty is None:
        print(f'The inventory is empty!')
        return False

    print(f'\nInventory Statistics:')
    print(f'Total Distinct Items: {inventory_count}')
    print(f'Total Items: {total_quantity}')
    print(f'Highest Quantity Item: {top_item}')
    print(f'Average Item Quantity: {avg_qty}')
    return True

# commented till persistence is ready

# 6 - save inventory - updates the inventory file with the current in-memory data struture 'inventory'
# modules required - (persistence)
def save_inventory_main(inventory, inv_file):
    try:
        if inv_file:
            persistence.save_inventory(inventory, inv_file)
        else:
            persistence.save_inventory(inventory)
    except Exception as e:
        print(f'Failed to save inventory: {e}')
        return False
    return True

# 7 - load inventory - loads the inventory file into the current in-memory data struture 'inventory'
# modules required - (persistence)
def load_inventory_main(inventory, inv_file):
    try:
        if inv_file:
            inventory = persistence.load_inventory(inv_file)
        else:
            inventory = persistence.load_inventory()
    except Exception as e:
        print(f'Failed to load inventory: {e}')
        return False
    return inventory

if __name__ == "__main__":
    end = False
    print("\nInventory Manager:")
    inv_file = input("Select Inventory file (leave blank for default): ")
    try:
        inventory = []
        inventory = load_inventory_main(inventory, inv_file)
    except Exception as e:
        print(f"Warning, could not preload inventory! load inventory before continuing: {e}")
    while not end:
        result = True
        input("\n(Press enter to continue)")
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
        try:
            user_selection = input_manager.get_main_menu_choice()
        except Exception as e:
            print(f"Could not interpret previous user input: {e}")
            continue
        try:
            match user_selection:
                case '1' | "add item":
                    result = add_item(inventory)
                case '2' | "remove item":
                    result = remove_item(inventory)
                case '3' | "update item":
                    result = update_item(inventory)
                case '4' | "search items":
                    result = search_items(inventory)
                case '5' | "show stats":
                    result = show_stats(inventory)
                case '6' | "save inventory":
                    result = save_inventory_main(inventory, inv_file)
                case '7' | "load inventory":
                    inv_file = input("Select Inventory file (leave blank for default): ")
                    inventory = load_inventory_main(inventory, inv_file)
                    if inventory == False:
                        result = False
                case '8' | "exit":
                    end = True
            
            if not result:
                print(f"Could not process last selection")
        except Exception as e:
            print(f"Could not process last selection: {e}")
