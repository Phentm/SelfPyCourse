# Assuming correct input TODO: implement input checks

user_temp = input("Insert the temperature you would like to convert: ")
last_char = user_temp[-1:].lower()
temp_num = float(user_temp[:-1])

if last_char == 'c':
    temp_num = (9 * temp_num + 160) / 5
    print(str(temp_num) + 'f')
elif last_char == 'f':
    temp_num = (5 * temp_num - 160) / 9
    print(str(temp_num) + 'c')
else:
    print("Invalid syntax")

