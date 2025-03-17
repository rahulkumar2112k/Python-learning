# class Car:
#     total_car=0
#     def __init__(self,brand,model): #constructor class
#         self.__brand=brand # making atrribute private with __
#         self.__model=model
#         Car.total_car +=1 # count increase when construtor call
        
#     def get_brand(self):
#         return  self.__brand 
        
#     def full_name(self):  #function to display
#         return f"{self.__brand} {self.__model}"
    
    
#     def fuel_type(self):
#         return "petrol or Diesel"
    
#     #decorator
#     @staticmethod  #only access by class but not object of class so no need of self parameter
#     def general_description():
#         return "Cars are means of transport"
    
#     @property #decorator insure no object can overwitte the model once created
#     def model(self):
#         return self.__brand
    
# class ElectricCar(Car): #electricCar will inherit car 
#     def __init__(self, brand, model,battery_size):
#         super().__init__(brand, model) #invoking parent class atrribute with super and have all the access
#         self.battery_size=battery_size
        
#     def fuel_type(self):
#         return "Electric Charge"
    
    
    
# class Battery:
#     def battery_info(self):
#         return "This is battery"
    
# class Engine:
#     def engine_info(self):
#         return "This is engine"
    
# class ElectricCarTwo(Car,Battery,Engine):
#     def electric_Car2(self):
#         return "This is electric Car2 Class"
    



# my_tesla=ElectricCarTwo("Tesla","Model-S")
# print(my_tesla.battery_info())
# print(my_tesla.engine_info())
# print(my_tesla.electric_Car2())




class Car:
    total_car = 0

    def __init__(self, brand, model):  # Constructor
        self.__brand = brand
        self.__model = model
        Car.total_car += 1  # Count increase when constructor is called

    def get_brand(self):
        return self.__brand

    def full_name(self):  # Function to display
        return f"{self.__brand} {self.__model}"

    def fuel_type(self):
        return "Petrol or Diesel"

    @staticmethod  # Only accessible by class, no need for `self`
    def general_description():
        return "Cars are means of transport"

    @property  # Ensures no object can overwrite the model once created
    def model(self):
        return self.__model


class ElectricCar(Car):  # ElectricCar will inherit Car
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)  # Invoke parent class constructor
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"


class Battery:
    def __init__(self, battery_type="Lithium-Ion"):
        self.battery_type = battery_type

    def battery_info(self):
        return f"This is a {self.battery_type} battery"


class Engine:
    def __init__(self, engine_type="Electric Motor"):
        self.engine_type = engine_type

    def engine_info(self):
        return f"This is an {self.engine_type}"


class ElectricCarTwo(Car, Battery, Engine):  # Multiple Inheritance
    def __init__(self, brand, model, battery_type="Lithium-Ion", engine_type="Electric Motor"):
        # Initialize parent class Car
        Car.__init__(self, brand, model)

        # Initialize Battery and Engine classes
        Battery.__init__(self, battery_type)
        Engine.__init__(self, engine_type)

    def electric_Car2(self):
        return "This is Electric Car 2 Class"


# Creating an object for ElectricCarTwo
my_tesla = ElectricCarTwo("Tesla", "Model-S")

print(my_tesla.full_name())           # Tesla Model-S
print(my_tesla.battery_info())        # This is a Lithium-Ion battery
print(my_tesla.engine_info())         # This is an Electric Motor
print(my_tesla.electric_Car2())       # This is Electric Car 2 Class
