import os

path = input()

print("Existance:", os.path.exists(path))

if os.path.exists(path):
    print ("Directory:", os.path.dirname(path))
    print ("Filename:", os.path.basename(path))