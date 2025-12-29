num_of_bricks = int(input("Enter a 3 digit number (each digit is the number of bricks for one pig): "))

digit_one = int(num_of_bricks / 100)
digit_two = int(num_of_bricks / 10 % 10)
digit_three = num_of_bricks % 10

sum_of_bricks = digit_one + digit_two + digit_three
print(sum_of_bricks)
print(int(sum_of_bricks/3))
print(sum_of_bricks%3)
print(sum_of_bricks % 3 == 0)