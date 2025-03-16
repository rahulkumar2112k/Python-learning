import math

number =int(input("Enter a number to check for prime: "))



flag=True

for i in range (2,number):
    if number%i==0:
        flag=False
        break

print(flag)

# if number<=1:
#     flag=False

# if number==2 or number==3:
#     flag=True

# if number%2==0 or number%3==0:
#     flag=False
    
# for i in range (5,int(math.sqrt(number))+1,6):
#     if number%i==0 or number%(i+2)==0:
#         flag=False
        


# print(flag)
    

