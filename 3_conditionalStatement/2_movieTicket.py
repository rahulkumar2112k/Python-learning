# age = int(input("Enter your age: "))
# day = input("Enter today's day: ").strip().lower()

# if age < 18:
#     if day == "wednesday":
#         print("Your ticket price is $6")
#     else:
#         print("Your ticket price is $8")
# elif age >= 18:
#     if day == "wednesday":
#         print("Your ticket price is $10")
#     else:
#         print("Your ticket price is $12")


age = int(input("Enter your age: "))
day = input("Enter today's day: ").strip().lower()

price =12 if age>=18 else 8

if day=="wednesday":
    price -=2
    
print ("Ticket price for you $",price)