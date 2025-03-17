

# def even (limit):
#     for i in range (1,limit+1):
#         if i%2==0:
#             print(i)
            
# even(10)

def even_generator(limit):
    for i in range(2,limit+1,2):
        yield i  

for num in even_generator(10):
    print (num)
   


# The **yield** keyword in Python is used to create generator functions.
# A generator is a special type of iterator that allows you to iterate over
# data one value at a time without storing the entire dataset in memory.   
    

"""Feature	                       yield	                                        return

Type of Function	Creates a generator function.	                          Creates a regular function.

Execution	        Pauses the function, remembers the state,                 Stops the function immediately and returns a value.
                    and continues from there on the next call. 
            
            
Memory Usage	    More memory efficient for large data.	                  Stores the entire result in memory.            

Iteration	        Used with loops like for to fetch values one by one.	  Only returns once, no iteration."""