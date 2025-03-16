tea_type=("Black", "Green", "White", "Oolong", "Herbal")
# print(tea_type)

# print(tea_type[0]) # Output: Black

# print(tea_type[1:4]) # Output: ('Green', 'White', 'Oolong')

# print(tea_type[:3]) # Output: ('Black', 'Green', 'White')

# print(tea_type[2:]) # Output: ('White', 'Oolong', 'Herbal')

# print(tea_type[::2]) # Output: ('Black', 'White', 'Herbal')
# # slicing with step 2

# print (tea_type[::-1]) # Output: ('Herbal', 'Oolong', 'White', 'Green', 'Black')
# # reverse the tuple

# tea_types[0]="Masala" # error as tuple is 

print(len(tea_type)) # Output: 5

more_tea=("Masala", "Earl Grey")

all_teas=tea_type+more_tea

print(all_teas) # Output: ('Black', 'Green', 'White', 'Oolong', 'Herbal', 'Masala', 'Earl Grey')

if "Black" in all_teas:
    print("Yes, Black tea is available") # Output: Yes, Black tea is available
    
if "Masala" not in all_teas:
    print("No, Masala tea is not available") # Output: No, Masala tea is not available
    
# del all_teas[0] # error as tuple is immutable

# all_teas[0:2]=["test","test"] # error as tuple is immutable

# all_teas.pop() # error as tuple is immutable
# all_teas.remove("Black") # error as tuple is immutable

# all_teas.append("test") # error as tuple is immutable
# all_teas.clear() # error as tuple is immutable

# all_teas.pop(1) # error as tuple is immutable

print(more_tea.count("Masala")) # Output: 1
print (more_tea.index("black")) # Output: 0


