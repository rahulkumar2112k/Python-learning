

# def sum_of_two (num1,num2):
#     return num1+num2

# print(sum_of_two(5,3))


# ---------------------------------------------------------

# using user input

# # Function to calculate the sum of two numbers
# def add_numbers(num1, num2):
#     return num1 + num2

# # Taking user input
# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))

# # Calling the function and displaying the result
# result = add_numbers(num1, num2)
# print(f"The sum of {num1} and {num2} is {result}")

# ---------------------------------------------------------------------

# Function to calculate the sum of two numbers
# Python doesn't require a main() function like C, C++, or Java, 
# but it follows a common convention using:
# Why Use if __name__ == "__main__"?
# ✅ Ensures the code runs only when executed directly, not when imported as a module.
# ✅ Helps in organizing larger programs with multiple files.


def add_numbers(num1, num2):
    return num1 + num2

# Main function
def main():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = add_numbers(num1, num2)
    print(f"The sum of {num1} and {num2} is {result}")

# Ensuring main runs only when executed directly
if __name__ == "__main__":
    main()

