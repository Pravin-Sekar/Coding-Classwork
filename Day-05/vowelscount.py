a = input("Enter string: ")
b = a.lower()

v = 0
c = 0

for i in b:
    if i in "aeiou":
        v += 1
    else:
        c += 1

print("Vowels:", v)
print("Consonants:", c)

"Or"




a = input("Enter string: ")

v = 0
c = 0

for i in a:
    if i == "A" or i == "E" or i == "I" or i == "O" or i == "U" or i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        v += 1
    else:
        c += 1

print("Vowels:", v)
print("Consonants:", c)