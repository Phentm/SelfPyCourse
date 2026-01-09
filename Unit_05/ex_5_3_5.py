def distance(num1, num2, num3):
    dist1_2 = abs(num1 - num2)
    dist1_3 = abs(num1 - num3)
    dist2_3 = abs(num2 - num3)

    close_to_num1 = dist1_2 == 1 or dist1_3 == 1
    num2_far = dist1_2 >= 2 and dist2_3 >= 2
    num3_far = dist1_3 >= 2 and dist2_3 >= 2
    return close_to_num1 and (num2_far or num3_far)


print(distance(1, 2, 10)) # True
print(distance(4, 5, 3)) # False
print(distance(-1, 0, 0))
