from file_handler import FileHandler

filename = "inventory.csv"
inventory_file = FileHandler(filename)      # creates the object
rows = inventory_file.read()                # use read method for the created object
print(f"#### START {filename} ####")

for row in rows:
    print(row)
print(f"#### END {filename} ####")
