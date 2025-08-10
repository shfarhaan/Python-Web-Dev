

class Vehicle:
    def __init__(self, vehicleType):
        self.vehicleType = vehicleType
        print(f"Vehicle Type: {self.vehicleType}")
        
    def move(self, mode):
        self.mode = mode
        print(f"Mode: {self.mode}")
    
#how to optimize the below code
class Car(Vehicle):
    def __init__(self,model):
        super().__init__(vehicleType="Car")
        self.model = model
        super().move("drive")

        
class Rickshaw(Vehicle):
    def __init__(self,model):
        super().__init__(vehicleType="Rickshaw")        
        self.model = model
        super().move("paddle")

class Air(Vehicle):
    def __init__(self,model):
        super().__init__(vehicleType="Air")
        self.model = model
        super().move("fly")       


car1 = Car("c1")
rick = Rickshaw("r1")
air = Air("a1")

# for x in(car1,rick,air):
#     x.move()