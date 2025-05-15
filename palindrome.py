
s = input("Enter a string: ")
i = 0
j = len(s) - 1
is_palindrome = True
while i < j:
    if s[i] != s[j]:
        is_palindrome = False
        break
    i += 1
    j -= 1
if is_palindrome:
    print("Palindrome")
else:
    print("Not a palindrome")
