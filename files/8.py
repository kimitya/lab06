import os

path = input()

print("Access:", os.access(path, os.W_OK))

if (os.access(path, os.W_OK)): 
    os.remove(path)
    print("Existance:", os.path.exists(path))

