class Car:
    def __init__(self,brand,model): #constructor class
        self.__brand=brand # making atrribute private with __
        self.model=model
        
    def get_brand(self):
        return  self.__brand 
        
    def full_name(self):  #function to display
        return f"{self.__brand} {self.model}"
    
class ElectricCar(Car): #electricCar will inherit car 
    def __init__(self, brand, model,battery_size):
        super().__init__(brand, model) #invoking parent class atrribute with super and have all the access
        self.battery_size=battery_size
        


my_tesla=ElectricCar("Tesla","Model-S","85kwh")
print(my_tesla.get_brand())

     
    