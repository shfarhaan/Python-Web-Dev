def get_value(any_list, key):
    for item in any_list:
        print(any_list[key])
        
        
ls = [
    ("Alice",25),
    ("Bob", 5),
    ("Marly", 30)
]

get_value(any_list=ls, key=1)