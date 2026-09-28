class Solution:
    def areAnagrams(self, s1, s2):
        if len(s1) != len(s2):
            return False

        count = {}

        for i in s1:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1

        for i in s2:
            if i in count:
                count[i] -= 1
            else:
                return False

        for i in count:
            if count[i] != 0:
                return False

        return True
    


"or"
from collections import Counter
re4turn Counter(s1) == Counter(s2)

"Or"
a = input("Enter: ")
b = input("Enter: ")


result = True

c1 = [0] * 26
c2 = [0] * 26

for i in a:
    c1[ord(i) - ord('a')] += 1

for i in b:
    c2[ord(i) - ord('a')] += 1

for i in range(26):
    if c1[i] != c2[i]:
        result = False
        break

print(result)
