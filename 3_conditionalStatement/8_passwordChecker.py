password=input("Enter your password : ")

if len(password)<6:
    passwordIs="weak"
elif len(password)<=10:
    passwordIs="Medium"
elif len(password)>10:
    passwordIs="strong"

print("your password is :",passwordIs)

