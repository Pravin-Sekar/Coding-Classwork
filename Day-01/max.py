import math
arr=list(map(int,input("Enter the numbers separated by space: ").split()))
max=math.inf
for i in arr:
    if i>max:
        max=i
    print("The maximum number is:",max)     
    