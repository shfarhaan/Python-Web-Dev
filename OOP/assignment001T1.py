

class CentralDB:
    def __init__(self, server_address = "www.fuudpandu.com", port = "125.255.003.001"):
        self.server_address = server_address
        self.port = port
        print(f"Connecting to {self.server_address}")
        print(f"Port Connected at: {self.port} ")

    def serviceType(self, service):
        self.service = service
        print(f"Connecting to {self.service} database. ")
    
# #how to optimize the below code
class PostgreSQL(CentralDB):
    def __init__(self,service):
        super().serviceType(service= "Orders")
        
class Redis(CentralDB):
    def __init__(self,service):
        super().serviceType(service="Cache")
        

class ElasticSearch(CentralDB):
    def __init__(self,service):
        super().serviceType(service="Analytics")



cDB = CentralDB(server_address = "www.fuudpandu.com", port = "125.255.003.001")

pgsq = PostgreSQL("Orders")
rds = Redis("Cache")
es = ElasticSearch("Analytics")

# for x in(pgsq, rds, es):
#     x.serviceType()
