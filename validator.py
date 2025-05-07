'''
This module conatins functions for validating names of items and quantity.

Functions:

validate_item_name: checks if each item has a valid name.

validate_quantity: checks if integer is a positive number

Usage:

You can use this module to validate item names and quantities. The name of the item has to be a string, spaces will be removed and any string with anything other than alphabets will result in an error message.

 The quantity has to be a positive integer to yield True results. Floats(decimals), negative numbers, and alphabets will yield False results.
'''

# Validating item names

def validate_item_name(name):
    if not isinstance(name, str) or not name.strip():
        return False, "Item name cannot be empty."
    if not name.replace(" ", "").isalpha():
        return False, "Item name must contain only letters and spaces."
    return True, ""

# Validating quantity

def validate_quantity(qty):
    try:
        qty = int(qty)
        if qty < 0:
            return False, "Quantity must be zero or greater."
        return True, ""
    except ValueError:
        return False, "Quantity must be an integer."

# Sample inputs
if __name__ == "__main__":
    print(validate_item_name("  "))
    print(validate_item_name("Apple"))
    print(validate_item_name("Apple123"))
    print(validate_quantity(-5))
    print(validate_quantity(10))
    print(validate_quantity("abc"))

