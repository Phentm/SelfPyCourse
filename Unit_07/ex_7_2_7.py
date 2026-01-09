def arrow(my_char, max_length):
    return_string = ""
    for i in range(max_length * 2 - 1):
        return_string += (my_char + " ") * (max_length - abs(max_length-i-1)) + "\n"

    return return_string

def main():
    print(arrow('*', 10))

if __name__ == "__main__":
    main()