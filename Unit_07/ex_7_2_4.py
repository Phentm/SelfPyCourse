def contains_seven(num):
    while num > 0:
        if num % 10 == 7:
            return True
        num //= 10
    return False

def seven_boom(end_number):
    return_list = list(range(end_number + 1))
    for num in return_list:
        if contains_seven(num) or num % 7 == 0:
            return_list[num] = "BOOM!"
    return return_list

def main():
    print(seven_boom(71))

if __name__ == "__main__":
    main()