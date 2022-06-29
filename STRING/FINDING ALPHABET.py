#FINDING ALPHABET
a=str(input("Enter string : "))
count=0
for i in a:
  if i.isalpha():
   count=count+1
print("Alphabets in the string: ",count)   