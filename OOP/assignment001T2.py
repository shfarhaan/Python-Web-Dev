

class CentralDB:
    def __init__(self, server_address = "www.fuudpandu.com", port = "125.255.003.001", service = ""):
        self.server_address = server_address
        self.port = port
        self.service = service
        
    def serverLocation(self):
        print(f"Connecting to {self.server_address}")
        print(f"Port Connected at: {self.port} ")

    def connectingDB(self):
        print(f"Connecting to {self.service} database... ")
    


    # def serviceType(self, service):

# #how to optimize the below code
class PostgreSQL(CentralDB):
    def __init__(self):
        super().__init__(service= "Orders")

        
class Redis(CentralDB):
    def __init__(self):
        super().__init__(service="Cache")
        # print(f"Connecting to {self.service} database. ")
        # super().serverLocation()


class ElasticSearch(CentralDB):
    def __init__(self):
        super().__init__(service="Analytics")
        # print(f"Connecting to {self.service} database. ")


# class DifferentModules(PostgreSQL, Redis, ElasticSearch):
#     def __init__(self):
#         super().__init__(server_address = "www.fuudpandu.com", port = "125.255.003.001")

# cDB = CentralDB()

pgsq = PostgreSQL()
rds = Redis()
es = ElasticSearch()

pgsq1 = PostgreSQL()


for x in(pgsq, rds, es):
    x.connectingDB()


# dm = DifferentModules()

# for x in(dm):
#     x.connectingDB()