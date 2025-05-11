#Save inventory function that takes an inventory dictionary and a filename as parameters.
#The function opens the file in write mode and writes each item and quantity to the file.
#If an error occurs during the saving process, the function prints an error message.

def save_inventory(inventory, filename="inventory_data.txt"):
    """Save inventory dictionary to a plain text file."""
    try:
        with open(filename, "w") as f:
            for item, quantity in inventory.items():
                f.write(f"{item},{quantity}\n")
        print(f"Inventory saved to '{filename}'")
    except Exception as e:
        print(f"Error saving inventory: {e}")

#Load inventory function that takes a filename as a parameter and returns an empty dictionary
#if the file is not found or invalid.
#The function reads each line in the file, splits it into item and quantity,
#and adds the item and quantity to the inventory dictionary.


def load_inventory(filename="inventory_data.txt"):
    """Load inventory from a plain text file. Return an empty dict if file not found or invalid."""
    inventory = {}
    try:
        with open(filename, "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    try:
                        item, quantity = line.split(",")
                        inventory[item] = int(quantity)
                    except ValueError:
                        print(f"Skipping invalid line: {line}")
        print(f"Inventory was loaded from '{filename}'")
    except FileNotFoundError:
        print(f"No inventory file found so an empty inventory was created.")
    except Exception as e:
        print(f"Error loading inventory: {e}")
    return inventory

