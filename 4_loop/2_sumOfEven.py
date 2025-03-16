number=int(input("Enter a number: "))

sum_even=0

for num in range(1,number+1):
    if(num%2==0):
        sum_even +=num
print ("Sum of even number:",sum_even)