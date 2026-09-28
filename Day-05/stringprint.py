a=input("ENTER A STRING: ")
for i in range(len(a)):
  print("Character ",i,": ",a[i],"\n")
"OR"
for idx,char in enumerate(a):
  print(idx,char)