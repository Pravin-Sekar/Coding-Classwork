import math
arr=list(map(int,input("Enter the numbers separated by space: ").split()))
min=-math.inf
for i in arr:
    if i<min:
        min=i
print("The minimum number is:",min)
