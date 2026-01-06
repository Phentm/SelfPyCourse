def main():
    print(shift_left([0, 1, 2]))
    print(shift_left(['monkey', 2.0, 1]))

def shift_left(my_list):
    a, b, c = my_list
    return [b, c, a]

if __name__ == "__main__":
    main()