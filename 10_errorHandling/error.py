file = open('test.txt', 'w')  # in write mode, if the file doesn't exist, it will be created automatically

try:
    file.write('chai aur code')
finally:
    file.close()

# Using 'with' statement for automatic file handling
# with open('test.txt', 'w') as file:
#     file.write('learning python')

# Reading the content of the file
with open('test.txt', 'r') as file:
    content = file.read()
    print(content)  # Output the content to see the result
