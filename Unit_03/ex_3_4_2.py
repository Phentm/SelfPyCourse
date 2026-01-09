user_string = input("Please enter a string: ")
if len(user_string) != 0:
    first_char = user_string[0]

print(first_char + user_string[1:].replace(first_char, 'e'))