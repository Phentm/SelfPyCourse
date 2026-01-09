def longest(my_list):
    return max(my_list, key=len)

def main():
    list1 = ["111", "234", "2000", "goru", "birthday", "09"]
    print(longest(list1))

    list2 = ["a", "Z"]
    print(longest(list2))

if __name__ == "__main__":
    main()