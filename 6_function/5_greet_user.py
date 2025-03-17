# def greet(name="user"):
#     return "Hello ,"+name+"!"

# print(greet("Rahul")) # if name is provide it print with name
# print(greet()) #print default value 




# ---------------------------------------------------

def greet(name="User"):
    return "Hello, " + name + "!"

# Taking user input and handling empty input
name = input("Enter your name: ").strip()  # .strip() removes extra spaces

# Use the default value if the input is empty
print(greet(name if name else "User"))
# print(greet())
