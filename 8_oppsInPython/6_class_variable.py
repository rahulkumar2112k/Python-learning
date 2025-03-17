class Car:
    total_car=0
    def __init__(self,brand,model): #constructor class
        self.__brand=brand # making atrribute private with __
        self.model=model
        Car.total_car +=1 # count increase when construtor call
        
    def get_brand(self):
        return  self.__brand 
        
    def full_name(self):  #function to display
        return f"{self.__brand} {self.model}"
    
    
    def fuel_type(self):
        return "petrol or Diesel"
    
class ElectricCar(Car): #electricCar will inherit car 
    def __init__(self, brand, model,battery_size):
        super().__init__(brand, model) #invoking parent class atrribute with super and have all the access
        self.battery_size=battery_size
        
    def fuel_type(self):
        return "Electric Charge"
        


my_tesla=ElectricCar("Tesla","Model-S","85kwh")
my_car=Car("Toyota","Safari")
print(my_tesla.fuel_type())
print(my_car.fuel_type())

print(Car.total_car)

     
    