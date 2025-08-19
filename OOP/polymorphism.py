

class Vehicle:
    def __init__(self, vehicleType, model, mode):
        self.vehicleType = vehicleType
        self.model = model
        self.mode = mode
        print(f"Vehicle Type {self.vehicleType}")
        print(f"Mode: {self.mode} ")

    def move(self):
        print(f"The {self.vehicleType} is moving using the {self.mode} mode. ")
    
#how to optimize the below code
class Car(Vehicle):
    def __init__(self,model):
        super().__init__(vehicleType="Car", mode = "drive", model = model)
        
class Rickshaw(Vehicle):
    def __init__(self,model):
        super().__init__(vehicleType="Rickshaw", mode = "paddle", model = model)

class Air(Vehicle):
    def __init__(self,model):
        super().__init__(vehicleType="Air", mode = "fly", model = model)

car1 = Car("c1")
rick = Rickshaw("r1")
air = Air("a1")

for i in(car1,rick,air):
    i.move()
    
    
# v = Vehicle(vehicleType="Rickshaw", mode= "paddle", model= "r1")