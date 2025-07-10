def sum(*args): # 1,2,3,4,5
    pass

def greet(username, is_loggedIn = None):
    if is_loggedIn is not None:
        print(f"Hello {username}")
    else:
        print("Please log in")
        
greet(username="Rakib", is_loggedIn=True) 
greet(username="Sakib")