def last_early(my_str):
    return my_str.lower().count(my_str[-1].lower()) > 1

print(last_early("happy birthday"))  # True
print(last_early("best of luck"))  # False
print(last_early("Wow"))  # True
print(last_early("X"))  # False
print(last_early(""))