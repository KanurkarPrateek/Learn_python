def PalindromeIterative(str):
    for i in range(0,int(len(str)/2)):
        if str[i] != str[int(len(str))-i-1]:
            return False
        return True


str1 = input("enter a string")
ans = PalindromeIterative(str1)
if ans == True:
    print("Palindrom")
else:
    print("not Palindrome")