"""Determine the maximum value out of 4 given numbers"""

x=float(input("Give me a number: "))
y=float(input("Give me a second number: "))
z=float(input("Give me a third number: "))
w=float(input("Give me a fourth number: "))

if x>=y and x>=z and x>=w:
    print ("Highest number: ",x)

if y>=x and y>=z and y>=w:
    print ("Highest number: ",y)

if z>=y and z>=x and z>=w:
    print ("Highest number: ",z)

if w>=y and w>=z and w>=x:
    print ("Highest number: ",w)


"""Another form
x,y,z,w
a=[]
a.append(x)
a.append(y)
a.append(z)
a.append(w)
max(a)"""