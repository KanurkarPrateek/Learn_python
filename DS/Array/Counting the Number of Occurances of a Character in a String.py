word = input("enter a word")
searchChar = input("input a char")


def CountOcc(str, character):
    count = 0
    for i in word:
        if i == searchChar:
            count += 1

    return count

print("Count",CountOcc(word,searchChar))
