# sum of all number passed in function

# def sum_of_all(*args):
#     return sum(args) #here sum is inbuilt fn

# print (sum_of_all(1,2,3))


def sum_of_all(*args):
    Sum=0
    print(*args) #it give all argument passed in fn
    print(args) #it actually in form of tuple(1,2,3) as it in tuple we can use iterate and sum it without using sum fn
    for i in args:
        Sum +=i
    return(Sum)
    # return sum(args) 
print (sum_of_all(1,2,3))
     