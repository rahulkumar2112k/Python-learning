class Car:
    total_car=0
    def __init__(self,brand,model): #constructor class
        self.__brand=brand # making atrribute private with __
        self.__model=model
        Car.total_car +=1 # count increase when construtor call
        
    def get_brand(self):
        return  self.__brand 
        
    def full_name(self):  #function to display
        return f"{self.__brand} {self.__model}"
    
    
    def fuel_type(self):
        return "petrol or Diesel"
    
    #decorator
    @staticmethod  #only access by class but not object of class so no need of self parameter
    def general_description():
        return "Cars are means of transport"
    
    @property #decorator insure no object can overwitte the model once created
    def model(self):
        return self.__brand
    
class ElectricCar(Car): #electricCar will inherit car 
    def __init__(self, brand, model,battery_size):
        super().__init__(brand, model) #invoking parent class atrribute with super and have all the access
        self.battery_size=battery_size
        
    def fuel_type(self):
        return "Electric Charge"
        


my_tesla=ElectricCar("Tesla","Model-S","85kwh")

print(isinstance(my_tesla,Car)) # true
print(isinstance(my_tesla,ElectricCar)) #true