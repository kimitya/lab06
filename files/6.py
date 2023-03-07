import os

path = os.getcwd()

os.mkdir(f'{path}/alphabet')
os.chdir(f'{path}/alphabet')

for i in range (65,91):
    open(chr(i) + '.txt', 'w')