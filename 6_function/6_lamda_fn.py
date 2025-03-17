# When to Use a Lambda Function?
# ✅ When the function logic is simple and short.
# ✅ For one-time use with functions like map(), filter(), and sorted().

# When NOT to Use a Lambda Function?
# ❌ When the function logic is complex — prefer a regular def function for readability.

# Would you like examples specific to data science, web development, or another area? 😊





cube =lambda x:x**3  #use only one time

num=int(input("Enter a number: "))

print (cube(num))


add=lambda x,y:x+y
print(add(5,3))


# auto add=[](int a,int b){return a+b}; in c++