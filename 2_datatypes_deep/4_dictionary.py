chai_types={"lemon chai":10, "ginger chai":20, "masala chai":30}

# print (chai_types)

# print(chai_types["lemon chai"]) # Output: 10
# # print(chai_types["gingera chai"]) #error

# print(chai_types.get("ginger chai")) # Output: 20
# print(chai_types.get("masalaa chai")) # Output: None

# chai_types["ginger chai"]=25 # update the value

# print(chai_types)

# for chai in chai_types:
#     print(chai) # Output: lemon chai ginger chai masala chai


# for chai in chai_types:
#     print(chai, ":", chai_types[chai]) # Output: lemon chai : 10 ginger chai : 25 masala chai : 
    

# for chai, price in chai_types.items():
#     print(chai, ":", price) # Output: lemon chai : 10 ginger chai : 25 masala chai : 30
    
# if "lemon chai" in chai_types:
#     print("Yes, lemon chai is available") # Output: Yes, lemon chai is available
    
# chai_types["green chai"]=35 # add a new key value pair
# print (chai_types) # Output: {'lemon chai': 10, 'ginger chai': 25, 'masala chai': 30, 'green chai': 35}

# chai_types.pop("green chai") # remove a key value pair
# print (chai_types) # Output: {'lemon chai': 10, 'ginger chai': 25, 'masala chai': 30}

# chai_types.popitem() # remove the last key value pair
# print (chai_types) # Output: {'lemon chai': 10, 'ginger chai': 25}  

# del chai_types["ginger chai"] # remove a key value pair by key

# print(chai_types) # Output: {'lemon chai': 10, 'masala chai': 30}

# # chai_types.clear() # remove all key value pairs   

# chai_types_copy=chai_types.copy() # create a copy of the dictionary 

# print(chai_types_copy) # Output: {'lemon chai': 10, 'masala chai': 30}

# # 

# squared_numbers = {x: x*x for x in range(10)} # dictionary comprehension

# print(squared_numbers) # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81} 

# even_numbers = {x: x for x in range(10) if x % 2 == 0} # dictionary comprehension with condition

# print(even_numbers) # Output: {0: 0, 2: 2, 4: 4, 6: 6, 8: 8}

# cube_numbers = {x: x*x*x for x in range(5)} # dictionary comprehension with condition

# print(cube_numbers) # Output: {0: 0, 1: 1, 2: 8, 3: 27, 4: 64}

# squared_numbers.clear() # remove all key value pairs
# print(squared_numbers) # Output: {}

keys=["a","b","c"]
default_values=1

dictionary = dict.fromkeys(keys, default_values) # create a dictionary with default values    

print (dictionary) # Output: {'a': 1, 'b': 1, 'c': 1}

new_dictionary=dict.fromkeys(keys,keys) # create a dictionary with default values as None

print(new_dictionary)  # Output: {'a': ['a', 'b', 'c'], 'b': ['a', 'b', 'c'], 'c': ['a', 'b', 'c']}