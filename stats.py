# List of dictionaries for inventory
inventory = [
    {'name': 'apple', 'quantity': 10},
    {'name': 'banana', 'quantity': 5},
    {'name': 'orange', 'quantity': 10},
    {'name': 'grape', 'quantity': 3}
]

# Function to count distinct items in the inventory
def get_inventory_count(inventory):
    return len(inventory)

# Function to calculate the total quantity of all items
def get_total_quantity(inventory):
    total = 0
    for item in inventory:
        total += item['quantity']
    return total

# Function to find the item(s) with the highest quantity
def get_top_item(inventory):
    if not inventory:
        return None  # Handle empty inventory
    max_quantity = max(item['quantity'] for item in inventory)
    top_items = [item['name'] for item in inventory if item['quantity'] == max_quantity]
    if len(top_items) == 1:
        return top_items[0]
    else:
        return top_items
    
# Function to calculate the average quantity per item
def get_average_quantity(inventory):
    if not inventory:
        return None  # Handle empty inventory
    total_quantity = get_total_quantity(inventory)
    count = get_inventory_count(inventory)
    return total_quantity / count

# Example usage
if __name__ == "__main__":
    print("Inventory:")
    for item in inventory:
        print("- " + item['name'] + ": " + str(item['quantity']))
print("Inventory:")
for item in inventory:
    print(f"- {item['name']}: {item['quantity']}")

print("\nDistinct items:", get_inventory_count(inventory))
print("Total quantity:", get_total_quantity(inventory))
print("Top item(s):", get_top_item(inventory))

#  For Main tests

print("Inventory:")
for item in inventory:
    print("- " + item['name'] + ": " + str(item['quantity']))

print("\nDistinct items:", get_inventory_count(inventory))
print("Total quantity:", get_total_quantity(inventory))
top_item = get_top_item(inventory)
print("Top item(s):", top_item)
average_quantity = get_average_quantity(inventory)
if average_quantity is not None:
    print("Average quantity per item:", round(average_quantity, 2))
else:
    print("Average quantity per item: None (inventory is empty)")