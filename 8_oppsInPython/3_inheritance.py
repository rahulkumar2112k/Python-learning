class Car:
    def __init__(self,brand,model): #constructor class
        self.brand=brand
        self.model=model
        
    def full_name(self):  #function to display
        return f"{self.brand} {self.model}"
    
class ElectricCar(Car): #electricCar will inherit car 
    def __init__(self, brand, model,battery_size):
        super().__init__(brand, model) #invoking parent class atrribute with super and have all the access
        self.battery_size=battery_size
        


my_tesla=ElectricCar("Tesla","Model-S","85kwh")
print(my_tesla.full_name())

     
    