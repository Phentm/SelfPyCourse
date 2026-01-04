def chocolate_maker(small, big, x):
    return (x <= small) or (x % 5 <= small and (x // 5) <= big)

print(chocolate_maker(3, 1, 8))  # Output: True
print(chocolate_maker(3, 1, 9))  # Output: False
print(chocolate_maker(3, 2, 10)) # Output: True

print(chocolate_maker(27, 0, 27))
