order=input("Enter your cofee order size [small,medium,large] : ").strip().lower()

extra_shot=(input("Do you want Extra short(Yes/No) : ")).lower()

if extra_shot=="yes":
    print(order.upper(),"cofee with an Extra short is ordered")
elif extra_shot=="no":
    print(order.upper(),"coffee is ordered")
else:
    print("Please enter your choice properly")
    