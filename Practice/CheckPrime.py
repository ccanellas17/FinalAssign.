"""This program asks for a number and checks if its a prime"""


def isPrime(n):
 for i in range (2, n // 2+1):
    if n % i==0:
       return False
 return True

n=int(input("Insert number: "))

if isPrime(n):
    print(n, "is prime.")
else:
    print(n, "is NOT prime.")






