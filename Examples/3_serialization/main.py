from file_handler import FileHandler
from item import Item

filename = "inventory.csv"
inventory_file = FileHandler(filename)      # creates the object
rows = inventory_file.read()                # use read method for the created object
print(f"#### START {filename} ####")

for row in rows:
    #print(row)
    item = Item.deserialze(row)
    item.displayCategory()
    item.displayPrice()
    item.displayWeight()
print(f"#### END {filename} ####")
