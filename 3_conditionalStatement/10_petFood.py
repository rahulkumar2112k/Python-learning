pet=input("Enter your pet (Dog,cat) : ").strip().lower()
age=int(input(f"Enter {pet} age :"))

if (pet=="dog"):
    if(age<2):
        print("give puppy food")
    else:
        print ("give dog food")
        
elif (pet=="cat"):
    if(age<5):
        print("give kitten food")
    else:
        print("give senior cat food")
        
        
else:
    print("soory,we recommend only cat and dog food")