MAIN_MENU = """--- Main Menu ---
 * 1. Print out the current shopping list
 * 2. Count all items
 * 3. Check for an item
 * 4. Count an item
 * 5. Remove an item from the shopping list
 * 6. Add a new item to the shopping list
 * 7. Print all illegal items
 * 8. Cleanup shopping list (remove duplicate items)
 * 9. Exit program
 Choose one of the following options (1-9): """

def get_user_input():
    return int(input(MAIN_MENU))

def menu_handler(menu_index, shopping_list = ['']):
    if menu_index == 1:
        return print_shopping_list(shopping_list)
    elif menu_index == 2:
        return print_all_item_count(shopping_list)
    elif menu_index == 3:
        return print_item_check(shopping_list)
    elif menu_index == 4:
        return print_item_count(shopping_list)
    elif menu_index == 5:
        return remove_item(shopping_list)
    elif menu_index == 6:
        return add_item(shopping_list)
    elif menu_index == 7:
        return print_illegal_items(shopping_list)
    elif menu_index == 8:
        return clean_duplicates(shopping_list)

def print_shopping_list(shopping_list):
    print(shopping_list)

def print_all_item_count(shopping_list):
    print(len(shopping_list))

def print_item_check(shopping_list):
    print(shopping_list.count(input("Enter item name: ").lower()) >= 1)

def print_item_count(shopping_list):
    print(shopping_list.count(input("Enter item name: ").lower()))

def remove_item(shopping_list):
    shopping_list.remove(input("Enter item name: ").lower())

def add_item(shopping_list):
    shopping_list.append(input("Enter item name: ").lower())

def print_illegal_items(shopping_list):
    for item in shopping_list:
        if len(item) < 3 or not str(item).isalpha:
            print(item)

def clean_duplicates(shopping_list):
    for item in shopping_list:
        if shopping_list.count(item) > 1:
            shopping_list.remove(item)

def main():
    shopping_list = input("Enter a shopping list of comma separated items: ").lower().split(',')

    user_choice = get_user_input()
    while user_choice != 9:
        menu_handler(user_choice, shopping_list)
        user_choice = get_user_input()


if __name__ == "__main__":
    main()