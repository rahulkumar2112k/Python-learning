class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
        
     
    
my_car =Car("toyota","corolla")
print(my_car.brand)
print(my_car.model)

my_car2=Car("Tata","Safari")
print(my_car2.model,my_car2.brand)