def Sumdigits( num ):
    sum =0
    while num != 0:
        rem = num % 10
        sum = sum + rem
        num = num // 10

    return sum

num = int(input("enter a num"))
sumDigit= Sumdigits(num)
print(sumDigit)