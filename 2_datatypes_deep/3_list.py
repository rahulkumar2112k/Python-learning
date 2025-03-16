
tea_varities=["Black", "Green", "White", "Oolong", "Herbal"]

# print(tea_varities[-1]) # Output: Herbal

# print(tea_varities[1:4]) # Output: ['Green', 'White', 'Oolong']

# print(tea_varities[:3]) # Output: ['Black', 'Green', 'White']

# print(tea_varities[2:]) # Output: ['White', 'Oolong', 'Herbal']

# print(tea_varities[::2]) # Output: ['Black', 'White', 'Herbal']
# # slicing with step 2

# print(tea_varities[::-1]) # Output: ['Herbal', 'Oolong', 'White', 'Green', 'Black']
# # reverse the list
# # slicing with step -1

# tea_varities[1:2] = ["masala"]
# print(tea_varities) # Output: ['Black', 'masala', 'White', 'Oolong', 'Herbal']
# # replace elements in the list using slicing

# tea_varities[1:3] = ["Green", "White"]

# print(tea_varities) # Output: ['Black', 'Green', 'White', 'Oolong', 'Herbal']

# tea_varities[1:1] = ["test","test","test"]
# print(tea_varities) # Output: ['Black', 'test', 'test', 'test', 'Green', 'White', 'Oolong', 'Herbal']

# # tea_varities[1:4] = ["test","test","test"]
# # print(tea_varities) # Output: ['Black', 'test', 'test', 'test', 'Green', 'White', 'Oolong', 'Herbal']

# tea_varities[1:4] = []  # remove elements from the list using slicing
# print(tea_varities) # Output: ['Black', 'Green', 'White', 'Herbal']

# for tea in tea_varities:
#     print(tea, end="-") # Output: Black Green White Herbal
    
    
# if "Black" in tea_varities:
#     print("\nYes there is black tea in the list") # Output: Yes
    
# if "Masala" not in tea_varities:
#     print("there is no masala tea in the list") # Output: No
    
    
# tea_varities.pop() # remove the last element from the list
# print(tea_varities) # Output: ['Black', 'Green', 'White']

# tea_varities.pop(1) # remove the element at index 1

# print(tea_varities) # Output: ['Black', 'White']

# tea_varities.remove("Black") # remove the element by value

# print(tea_varities) # Output: ['White']

# del tea_varities[0] # remove the element at index 0

# print(tea_varities) # Output: []

# tea_varities.clear() # remove all elements from the list

# tea_varities.append("Black") # add an element to the end of the list
# print(tea_varities) # Output: ['Black']

# tea_varities.insert(1, "Green") # add an element at a specific index
# print(tea_varities) # Output: ['Black', 'Green']

# tea_varities_copy = tea_varities.copy() # create a copy of the list 

# print(tea_varities_copy) 
# print(tea_varities) # Output: ['Black', 'Green']  

# tea_varities_copy.append("White") # add an element to the end of the list   

# print(tea_varities_copy) # Output: ['Black', 'Green', 'White']
# print(tea_varities) # Output: ['Black', 'Green']

squared_numbers = [x*x for x in range(10)] # list comprehension

print (squared_numbers) # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

even_numbers = [x for x in range(10) if x % 2 == 0] # list comprehension with condition

print(even_numbers) # Output: [0, 2, 4, 6, 8]

cube_numbers = [x*x*x for x in range(5)] # list comprehension with condition 

print(cube_numbers) # Output: [0, 1, 8, 27, 64]
