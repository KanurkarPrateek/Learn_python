def swap_first_and_last(lst):
    if len(lst) >= 2:
        lst[0], lst[-1] = lst[-1], lst[0]
    return lst

# Take input of list from the user
user_input = input("Enter elements of the list separated by spaces: ")
my_list = user_input.split()

# Convert input elements to integers
my_list = [int(x) for x in my_list]

print("Original list:", my_list)
print("List after swapping first and last elements:", swap_first_and_last(my_list))
