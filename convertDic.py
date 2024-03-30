def create_dictionary():
    num_pairs = int(input("Enter the number of key-value pairs: "))
    dictionary = {}

    for _ in range(num_pairs):
        key = input("Enter key: ")
        value = input("Enter value: ")
        dictionary[key] = value

    return dictionary


if __name__ == "__main__":
    my_dict = create_dictionary()
    print("Dictionary:", my_dict)
