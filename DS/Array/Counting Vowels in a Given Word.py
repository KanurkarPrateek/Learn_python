vowels = ["a", "e", "i", "o", "u"]
word = input("enter an value")
count = 0


def CountVowels(str):
    count = 0
    for i in word:
        if i in vowels:
            count += 1
    return count


def CountConsonents(str):
    count = 0
    for i in word:
        if i not in vowels:
            count += 1
    return count


print("Vowels",CountVowels(word) )
print("Consonets",CountConsonents(word))
