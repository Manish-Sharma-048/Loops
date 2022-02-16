# WAP to print calculate the factorial of number entered through keyboard

n = int(input("Please enter the number: "))
num = 1

for i in range(1,n+1):
    num = num * i

print("The factoral value of", n, "is:", num)
