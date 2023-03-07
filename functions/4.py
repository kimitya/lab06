import math
import time
num = int(input())
milsec = int(input())

time.sleep(milsec/1000)

ans=math.sqrt(num)

print(f"Square root of {num} after {milsec} miliseconds is {ans}")