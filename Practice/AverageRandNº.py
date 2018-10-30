"""Determine the average of 4 random numbers"""

import random
y=0
for abc in range (4):
    z=random.randint(1, 100)
    y=y+z

print(y/4)