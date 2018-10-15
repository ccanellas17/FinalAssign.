"""Create a game based on a maze where every move the character makes can only be North South West or East.
The only way to wi is if the user makes the correct sequence which is: SSNEW"""

while True:

 move=input("Which way you want to go? (N, S, E, W)")
 if move == "s":
     break
 else:
     print("Wrong way.")

while True:

 move=input("Which way you want to go? ")
 if move == "s":
     break
 else:
     print("Wrong way.")

while True:
  move=input("Which way you want to go? ")
  if move == "n":
    break
  else:
         print("Wrong way.")

while True:
    move=input("Which way you want to go? ")
    if move == "e":
     break
    else:
         print("Wrong way.")

while True:
     move=input("Which way you want to go? ")
     if move == "w":
         break
     else:
         print("Wrong way.")

print ("You've won the maze. ")