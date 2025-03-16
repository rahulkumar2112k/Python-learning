number=int(input("Enter a number : "))
num=number

factorial=1

while number>0:
    factorial =factorial*number
    number -=1
    
print("Factorial of",num, "is",factorial)