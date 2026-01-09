def squared_numbers(start, stop):
    return_list = []
    while start <= stop:
        return_list.append(pow(start, 2))
        start+=1
    return return_list

def main():
    print(squared_numbers(4, 8))
    print(squared_numbers(-3, 3))

if __name__ == "__main__":
    main()