def check_valid_input(letter_guessed, old_letters_guessed):
    return (len(letter_guessed) == 1
            and letter_guessed.isalpha()
            and letter_guessed.isascii()
            and letter_guessed.lower() not in old_letters_guessed)

def main():
    old_letters = ['a', 'b', 'c']
    print(check_valid_input('C', old_letters))
    print(check_valid_input('ep', old_letters))
    print(check_valid_input('$', old_letters))
    print(check_valid_input('s', old_letters))

if __name__ == "__main__":
    main()