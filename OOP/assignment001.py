

class CentralDB:
    def __init__(self, server_address = "www.fuudpandu.com", port = "125.255.003.001", number_of_orders = 0, service = "" ):
        self.server_address = server_address
        self.port = port
        self.number_of_orders = number_of_orders
        self.service = service
        print(f"Connecting to {self.server_address}")
        print(f"Port Connected at: {self.port} ")

    def serviceType(self):
        print(f"Connecting to {self.service} database. ")
    
#how to optimize the below code
class PostgreSQL(CentralDB):
    def __init__(self,number_of_orders):
        super().__init__(number_of_orders, service="Orders")
        
# class Redis(CentralDB):
#     def __init__(self,model):
#         super().__init__(vehicleType="Rickshaw", mode = "paddle", model = model)
        

# class ElasticSearch(CentralDB):
#     def __init__(self,model):
#         super().__init__(vehicleType="Air", mode = "fly", model = model)

# car1 = Car("c1")
# rick = Rickshaw("r1")
# air = Air("a1")


cDB = CentralDB(server_address = "www.fuudpandu.com", port = "125.255.003.001")

pgsql = PostgreSQL(number_of_orders=10)

# for x in(pgsql):
#     x.serviceType()
