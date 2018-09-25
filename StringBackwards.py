string=input("Write a string: ")

index=len(string)-1

while index >=0:

   print (string[index])

   index=index-1


   """Easiest form:"""

   print(string[::-1])


"""Slice strings:"""

s="Hello World"
s[0:2]="He"
s[3:6]="llo"
s[:]="Hello World"
s[4:0:-1]= "olle"

