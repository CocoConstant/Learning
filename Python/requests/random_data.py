import random
import pandas as pd

# ID
random.seed(819)
data = set()
for i in range(50):
    first_letter = random.randint(65,90)
    second_letter = random.randint(65,90)
    number = random.randint(100, 999)
    data.add(chr(first_letter) + chr(second_letter) + str(number))
    
print(len(data))

# name 
