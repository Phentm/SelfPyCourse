def extend_list_x(list_x, list_y):
    list_x[:0] = list_y
    return list_x

def main():
    x = [1, 2, 3]
    y = [4, 5, 6]
    print(x, " - ", y)
    print(extend_list_x(x, y))
    print(x, " - ", y)

if __name__ == "__main__":
    main()