
a = open("a.txt", "r")
k=a.read()
with open("b.txt", "w") as b:
    b.write(k)
        