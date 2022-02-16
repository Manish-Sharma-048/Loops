# WAP to print all even and odd numbers between 1 and 100

even = 0
odd = 0
print("Even\tOdd")
for i in range(1,100):
    if i%2 == 0:
        print(i, end = "")
        even+=1
        
    else:
        print("\t", i)
        odd+=1
        
print("\nTotal even numbers: ",even, "\nTotal odd numbers: ",odd)
