# WAP to print a pattern

num = 1
for i in range(1, 4):
    for j in range(4, 0, -1):
        if j > i:
            print(" ", end = " ")
        else:
            print(num, end = " ")
            num+=1
    print(" ")
