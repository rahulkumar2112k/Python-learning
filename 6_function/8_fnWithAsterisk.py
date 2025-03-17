

# def print_kwargs(name,power):
#     print("name :",name,"power :",power)
    

# print_kwargs(name="rahul",power="lazer") #it works
# print_kwargs(power="lazer",name="rahul") #it works

# print_kwargs(name="rahul",power="lazer",enemy="dr.strange") #here get error


#we can handle all the parameter with kwargs using key value

def print_kwargs(**kwargs): 
    for key ,value in kwargs.items():
        print (f"{key}:{value}")
    


print_kwargs(name="rahul")
print_kwargs(name="rahul",power="lazer") #it works
print_kwargs(power="lazer",name="rahul") #it works

print_kwargs(name="rahul",power="lazer",enemy="dr.strange") #here get error
