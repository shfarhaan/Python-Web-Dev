

class CentralDB:
    # server_address = input("Please enter server address: ")
    # port_address = input("Please enter port address: ")
    
    def __init__(self, server_address = "www.fuudpandu.com", port_address = "125.255.003.001", service = ""):
        self.server_address = server_address
        self.port_address = port_address
        self.service = service
        
    def serverLocation(self):
        return f"Connecting to {self.server_address} at port: {self.port_address} \n"

    def connectingDB(self):
        print(f"Connecting to {self.service} database... ")
    


    # def serviceType(self, service):

# #how to optimize the below code
class PostgreSQL(CentralDB):
    def __init__(self):
        super().__init__(service= "Orders")
        # print("This DB stores orders, restaurants, customers data.")

        
class Redis(CentralDB):
    def __init__(self):
        super().__init__(service="Cache")
        # print(f"Connecting to {self.service} database. ")
        # super().serverLocation()
        # print("This DB maintains caching for active orders for fast delivery tracking. ")


class ElasticSearch(CentralDB):
    def __init__(self):
        super().__init__(service="Analytics")
        # print(f"Connecting to {self.service} database. ")
        # print("This service is used for searching reports.")


class DifferentModules():
    def __init__(self):
        pass

# cDB = CentralDB()

pgsq = PostgreSQL()
rds = Redis()
es = ElasticSearch()

pgsq1 = PostgreSQL().serverLocation()
# dm = DifferentModules()

# print(f"Server Address: {CentralDB().server_address}")
# print(f"Port Number: {CentralDB().server_address}")


for x in(pgsq, rds, es):
    x.connectingDB()



# for x in(dm):
#     x.connectingDB()