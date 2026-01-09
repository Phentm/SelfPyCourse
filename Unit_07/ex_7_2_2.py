def numbers_letters_count(my_str):
    numeric = non_numeric = 0
    for char in my_str:
        if char.isnumeric():
            numeric+=1
        else:
            non_numeric+=1
    return [numeric, non_numeric]

def main():
    print(numbers_letters_count("Python 3.6.3"))

if __name__ == "__main__":
    main()