a = input("Enter string: ")
b = a.lower()

v = 0
c = 0

for i in range(len(b)):
    if b[i] in "aeiou":
        v += 1
    else:
        c += 1

print("Vowels:", v)
print("Consonants:", c)