# username="Rahul"

# def fun():
#     # username="rahul"
#     print(username)  # in case fun ko username nahi milega to wo global use karega
    
# print (username)
# fun()




# x=99

# def fun(y):
#     z=x+y  #x global se lega aur y parameter se
#     return z

# result=fun(1)
# print(result)



# x=99

# def fun():
#     x=88


# fun()    
# print(x) #print 99 fun not affect global variable



# x=99

# def fun():
#     global x # means use global x and make changes
#     x=88


# fun()    
# print(x) #print 88 as it changes global variable


# x=99

# def fun():
#     # x=88
#     def fun2():
#         print(x)
#     fun2()
    
# fun() #print 88


def fun1(num):
    def fun2(x):
        return x**num
    return fun2

f=fun1(2) # fun come with x**2
g=fun1(3) # fun come with x**3

print(f(3))  # output 9
print(g(3))  # output 27