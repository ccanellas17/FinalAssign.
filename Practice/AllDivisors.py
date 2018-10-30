"""Write a function that takes an integer as parameter and returns a list of all the divisors of that number:
ex: 47->[1, 47] , 28->[1,2,4,7,14,28]"""


def Divisor(n):
    numbers=[]
    for x in range(1, n+1):
        if n % x==0:
            numbers.append(x)

    print (numbers)

n=int(input("Write an integer number: "))
Divisor(n)