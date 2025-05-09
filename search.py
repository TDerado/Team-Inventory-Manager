def search_item(inventory, search_term, exact_match_flag):
    """ Checks given list of dictionaries for items with name value containing a search_term """
    matching_items = []
    try:
        if exact_match_flag == 'y':
            for item_dict in inventory:
                if search_term == item_dict["name"]:
                    matching_items.append(item_dict)
        else:
            for item_dict in inventory:
                if search_term.lower() in item_dict["name"].lower():
                    matching_items.append(item_dict)
        return matching_items
    except KeyError:
        print("Error: Item was expected to have 'name' key, was not found. cancelling...")
        return -1

if __name__ == "__main__":
    inv = [{"name":"test", "quantity": 3}, {"name":"object", "quantity": 1}, {"name":"tests", "quantity": 33}, {"name":"None", "quantity": 33}]
    term = input("Test Search Term: ")
    result = search_item(inv, term, 'n')
    if result == -1:
        print(f"Could not process last selection")
        raise SystemExit
    if not result:
        print(f"There were no matches with '{term}'")
    else:
        print("\nItems Found: ")
        for index, item_dict in enumerate(result):
            print(f'{index+1}) {item_dict}')