from ex_6_4_1 import check_valid_input

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed.lower())
        return True

    print("X\n" + " -> ".join(sorted(old_letters_guessed)))

    return False


def main():

    old_letters = ['a', 'p', 'c', 'f']
    print(try_update_letter_guessed('A', old_letters))  # X
                                                                    # a -> c -> f -> p
                                                                    # False

    print(try_update_letter_guessed('s', old_letters))  # True

    print(old_letters)                                              # ['a', 'p', 'c', 'f', 's']

    print(try_update_letter_guessed('$', old_letters))  # X
                                                                    # a -> c -> f -> p -> s
                                                                    # False

    print(try_update_letter_guessed('d', old_letters))  # True

    print(old_letters)                                              # ['a', 'p', 'c', 'f', ‘s’, 'd']

if __name__ == "__main__":
    main()