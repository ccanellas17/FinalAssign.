gross=int(input("Give the gross salary: "))
kids=int(input("Give the number of kids: "))

try:
    if gross<1000:
        tax=0.1

    elif gross<2000:
        tax=0.12

    elif gross<4000:
        tax=0.14

    elif gross>4000:
        tax=0.18

except:
 print("error")

if gross<2000:
    tax=tax-kids*0.01

else:
    tax=tax-kids*0.005



net=int(gross-gross*tax)

print("Net salary: ",net)
