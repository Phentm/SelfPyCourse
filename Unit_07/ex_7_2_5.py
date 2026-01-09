def sequence_del(my_str):
    if not len(my_str):
        return ''

    return_string = ""

    previous_char = my_str[0]
    for char in my_str:
        if previous_char != char:
            return_string += previous_char
        previous_char = char
    return_string += my_str[-1]
    return return_string

def main():
    print(sequence_del("ppyyyyythhhhhooonnnnn"))
    print(sequence_del("SSSSsssshhhh"))
    print(sequence_del("Heeyyy   yyouuuu!!!"))
    print(sequence_del(''))

if __name__ == "__main__":
    main()
