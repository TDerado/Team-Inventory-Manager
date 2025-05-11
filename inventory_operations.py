# Inventory Operations

def add_item(inventory, item_name, quantity):
    # Look for the item in the inventory
    found = False
    for item in inventory:
        if item["name"] == item_name:
            item["quantity"] = item["quantity"] + quantity
            found = True
            break
    # If not found, add it as a new item
    if not found:
        new_item = {"name": item_name, "quantity": quantity}
        inventory.append(new_item)

def remove_item(inventory, item_name):
    # Look for the item and remove it
    for item in inventory:
        if item["name"] == item_name:
            inventory.remove(item)
            break

def update_quantity(inventory, item_name, new_quantity):
    # Update the quantity of the item
    found = False
    for item in inventory:
        if item["name"] == item_name:
            item["quantity"] = new_quantity
            found = True
            break
    # If item not found, add it as a new item
    if not found:
        inventory.append({"name": item_name, "quantity": new_quantity})

# Testing the functions
if __name__ == "__main__":
    inventory = []

    add_item(inventory, "Apple", 5)
    add_item(inventory, "Banana", 3)
    add_item(inventory, "Apple", 2)

    print("Inventory after adding items:")
    print(inventory)

    remove_item(inventory, "Banana")
    print("Inventory after removing Banana:")
    print(inventory)

    update_quantity(inventory, "Apple", 10)
    update_quantity(inventory, "Grapes", 4)

    print("Final Inventory:")
    print(inventory)
