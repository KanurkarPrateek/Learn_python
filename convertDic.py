def create_dictionary():
    num_pairs = int(input("Enter the number of key-value pairs: "))
    dictionary = {}

    for _ in range(num_pairs):
        key = input("Enter key: ")
        value = input("Enter value: ")

        
        if value.isdigit():
            value = int(value)
        elif value.replace('.', '', 1).isdigit():
            value = float(value)
        else:
            # If the value is not numeric, keep it as a string
            pass

        dictionary[key] = value

    return dictionary


if __name__ == "__main__":
    my_dict = create_dictionary()
    print("Dictionary:", my_dict)
