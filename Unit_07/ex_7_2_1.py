def is_greater(my_list, n):
    return_list = list()
    for num in my_list:
        if num > n:
            return_list.append(num)
    return return_list

def main():
    result = is_greater([1, 30, 25, 60, 27, 28], 28)
    print(result) # [30, 60]

if __name__ == "__main__":
    main()