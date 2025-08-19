class CentralDB:
    # server_address = input("Please enter server address: ")
    # port_address = input("Please enter port address: ")
    
    def __init__(self, server_address = "www.fuudpandu.com", port_address = "125.255.003.001", service = ""):
        self.server_address = server_address
        self.port_address = port_address
        self.service = service
        
    def serverLocation(self):
        print(f"Connecting to {self.server_address} at port: {self.port_address} \n")

    def connectingDB(self):
        print(f"Connecting to {self.service} database... ")
    
# #how to optimize the below code
class PostgreSQL(CentralDB):
    def __init__(self):
        super().__init__(service= "Orders")
        # print(f"Connecting to {self.service} database. ")
        # print("This DB stores orders, restaurants, customers data.")
        # super().serverLocation()


class Redis(CentralDB):
    def __init__(self):
        super().__init__(service="Cache")
        # print(f"Connecting to {self.service} database. ")
        # print("This DB maintains caching for active orders for fast delivery tracking. ")
        # super().serverLocation()


class ElasticSearch(CentralDB):
    def __init__(self):
        super().__init__(service="Analytics")
        # print(f"Connecting to {self.service} database. ")
        # print("This service is used for searching reports.")
        # super().serverLocation()


pgs = PostgreSQL()
pgs.serverLocation()
rds = Redis()
es = ElasticSearch()


# print(f"Server Address: {CentralDB().server_address}")
# print(f"Port Number: {CentralDB().server_address}")


for service in(pgs, rds, es):
    service.connectingDB()