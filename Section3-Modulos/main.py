import math_operations as mo
from math_operations import subtract
import os

print("\n####### Using math_operations module #######\n")
print("The sum is:", mo.sum(10, 5))
print("The difference is:", subtract(10, 5))
print("Current working directory:", os.getcwd())
print("Directory contents:", os.listdir())
#print("System command output:", os.system("systeminfo"))
print("System command output:", os.system("dir"))

print(len("####### End of math_operations module usage #######"))

