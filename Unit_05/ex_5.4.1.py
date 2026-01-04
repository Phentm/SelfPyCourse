def main():
    print(dist(35, -0.675))
    help(dist)

def dist(num1, num2):
    """
    Function returns the absolute difference (distance) between two numbers,
    num1 and num2.
    :param num1: 1st number
    :type num1: float
    :param num2: 2nd number
    :type num2: float
    :return: The absolute difference between two numbers
    :rtype: float
    """
    return abs(num1 - num2)

if __name__ == "__main__":
    main()