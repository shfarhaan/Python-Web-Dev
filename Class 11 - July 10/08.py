# **kwargs

def greet(**kwargs):
    # if kwargs.get("username") is not None:
        print(kwargs.get("username"))
        print(kwargs.get("logged_id"))
        print(kwargs.get("is_cookies"))
        
        print("________________")
    
greet()
greet(username="Rakib")
greet(username="Sakib", logged_id = True)
greet(username="Rakib", logged_id = True, is_cookies="Yes")