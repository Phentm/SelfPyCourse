def main():
    print(is_valid_input('a'))  # True
    print(is_valid_input('A'))  # True
    print(is_valid_input('$'))  # False
    print(is_valid_input("ab"))  # False
    print(is_valid_input("app$"))  # False

def is_valid_input(letter_guessed):
    letter_guessed = str(letter_guessed)
    return (len(letter_guessed) == 1
            and letter_guessed.isalpha()
            and letter_guessed.isascii())

if __name__ == "__main__":
    main()