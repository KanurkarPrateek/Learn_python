"""
1
2 1
3 2 1
4 3 2 1
5 4 3 2 1
"""
def print_triangle(rows):
    for i in range(1, rows + 1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()


num_rows = int(input("Enter a Number"))


print_triangle(num_rows)


