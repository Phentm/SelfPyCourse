def show_hidden_word(secret_word, old_letters_guessed):
    return_string = ""
    for char in secret_word:
        if char in old_letters_guessed:
            return_string += char
        else:
            return_string += "_"

    return " ".join(return_string)

def main():
    secret_word = "mammals"
    old_letters_guessed = ['s', 'p', 'j', 'i', 'm', 'k']

    print(show_hidden_word(secret_word, old_letters_guessed))

if __name__ == "__main__":
    main()