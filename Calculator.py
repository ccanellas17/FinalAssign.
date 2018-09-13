print("1. Addition")
print("2. Substraction")
print("3. Multiplication")
print("4. Division")

command = int(input("Enter the desired command: "))

if command == 1:
    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter second number: "))
    print("Solution: ", n1+n2)

if command == 2:
    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter second number: "))
    print("Solution: ", n1-n2)

if command == 3:
    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter second number: "))
    print("Solution: ", n1*n2)

if command == 4:
    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter second number: "))
    print("Solution: ", n1/n2)