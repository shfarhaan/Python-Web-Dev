# Problem 1

# Remove Duplicates from a list

"""
1. by indexing
2. brute forcing 
3. unique vals - empty list

"""

names = ["adnan", "biplop", "sazzad", "partha","sazzad", "partha", "adnan"]
unique_names = []

for name in names:
    if name not in unique_names:
        unique_names.append(name)
        
print(unique_names)