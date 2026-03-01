import json
inventory = []
# Task 1 : Read inventory file
with open('inventory.json', 'r') as file:
    inventory = json.load(file)
#print Total Number of Books
print("Total number of books:",len(inventory))


# Task 2 : adding new book

new_book = {"title": "Atomic Habits", "author": "James Clear", "price": 14.99, "in_stock": True}

# append new value

inventory.append(new_book)

# write new book entry in invertory json file

with open('inventory.json', 'w') as file:
    json.dump(inventory,file,indent=4)

# Task 3 : Read updated entry from inventory json file
updated_inventory = []
with open('inventory.json', 'r') as file:
    updated_inventory = json.load(file)
#print Total Number of Books
print("Total number of books after addition:",len(updated_inventory))

# Display all records from json file
for book in updated_inventory:
    print(f"Title: {book['title']} | Author: {book['author']} | Price: {book['price']:.2f}")
