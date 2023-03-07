import os


path = os.getcwd()

for i in os.listdir(path):
    if os.path.isdir(f'{path}/{i}'):
        print(i)
print()  
for i in os.listdir(path):
    if os.path.isfile(f'{path}/{i}'):
        print(i)
print()       
for i in os.listdir(path):
        print(i)


    