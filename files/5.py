import os

a = input().split()

with open ("list.txt", "w") as f:
    for i in range(len(a)):
        f.write(a[i])