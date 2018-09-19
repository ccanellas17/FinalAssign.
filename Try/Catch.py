n1=int(input("Give me a number: "))
n2=int(input("Give me a second number: "))

solution=int(n1/n2)

try: print("Solution: ", solution)

except ValueError:
    print("Give a valid number.")

except ZeroDivisionError:
    print("The second number cannot be 0.")