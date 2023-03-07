a = input()
ucnt =0
lcnt=0
for i in a:

    if ord(i)>=65 and ord(i)<=90:
        ucnt += 1
    else:
        lcnt+=1
        
print("Lowercase letters:", lcnt)
print("Uppercase letters:", ucnt)