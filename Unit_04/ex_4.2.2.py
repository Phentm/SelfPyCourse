user_input = input("Input a string: ").lower().replace(' ', '')

first_half = user_input[:len(user_input)//2]
second_half = user_input[len(user_input)//2*-1:]

if first_half == second_half[::-1]:
    print("OK")
else:
    print("NOT")