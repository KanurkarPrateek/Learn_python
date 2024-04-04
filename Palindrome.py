def isPalindrom(str1):
    return str1 == str1[::-1]

str1 = "abcddcba abcddcba"

ans = isPalindrom(str1)

if(ans ==True):
    print("Palindrome")
else:
    print("Not Palindrome")

