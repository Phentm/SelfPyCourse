def mult_tuple(tuple1, tuple2):
    ret_tuple = ()

    for i in range(0, len(tuple1)):
        for j in range(0, len(tuple2)):
            ret_tuple += ((tuple1[i], tuple2[j]),)

    for i in range(0, len(tuple1)):
        for j in range(0, len(tuple2)):
            ret_tuple += ((tuple2[j], tuple1[i]),)

    return ret_tuple

def main():
    first_tuple = (1, 2, 3)
    second_tuple = (4, 5, 6)
    print(mult_tuple(first_tuple, second_tuple))

if __name__ == "__main__":
    main()