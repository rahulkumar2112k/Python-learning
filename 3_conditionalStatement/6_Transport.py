distance =int(input("Enter the Distance betwen (1-200) km: "))

if(distance<=0):
    print ("Enter valid Distance")
    exit()


if distance<3:
    mode="walk"
elif distance<15:
    mode="Bike"
elif distance >=15:
    mode="Car"


print("Your mode of transportation is ",mode)