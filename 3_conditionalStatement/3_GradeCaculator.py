score=int(input("Enter your marks :"))

if(score>=101):
    print ("Enter valid marks")
    exit()
  

# if score>=90 and score<=100:
#     print ("your grade is A")
# elif score>=80 and score<90:
#     print ("your grade is B")
# elif score>=70 and score<80:
#     print ("your grade is C")
# elif score>=60 and score<70:
#     print ("your grade is D")
# else :
#     print("your grade is F")

if score>=90:
    grade="A"
elif score>=80:
    grade="B"
elif score>=70:
    grade="c"
elif score>=60:
    grade="D"
else :
    grade="F"
    
print("your grade is ",grade)