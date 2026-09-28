a = input("Enter string: ")

b = a.lower()

left = 0
right = len(b) - 1
c = 0

while left < right:
    if b[left] == b[right]:
        left = left + 1
        right = right - 1
    else:
        c = 1
        break

if c == 0:
    print("Palindrome")
else:
    print("Not Palindrome")
"""if a == a[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")"""



