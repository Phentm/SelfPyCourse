def sort_prices(list_of_tuples):
    return sorted(list_of_tuples, key=get_price, reverse=True)

def get_price(product_tuple):
    return float(product_tuple[1])

def main():
    products = [('milk', '5.5'), ('candy', '2.5'), ('bread', '9.0')]
    print(products[0][1])
    print(sort_prices(products))

if __name__ == "__main__":
    main()