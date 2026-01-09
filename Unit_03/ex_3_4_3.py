user_input = input("Please enter a string: ")

middle_point = len(user_input) // 2
first_half = user_input[:middle_point].lower()
second_half = user_input[middle_point:].upper()

print(first_half + second_half)