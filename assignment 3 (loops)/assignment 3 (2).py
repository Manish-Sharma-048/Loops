# WAP to print all even and odd numbers between 100 and 1

even = 0
odd = 0
print("Even\tOdd")
for i in range(100,1,-1):
    if i%2 == 0:
        print(i, end = "")
        even+=1
        
    else:
        print("\t", i)
        odd+=1
        
print("\n\nTotal even numbers: ",even, "\nTotal odd numbers: ",odd)
