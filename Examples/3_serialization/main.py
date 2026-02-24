from file_handler import FileHandler
from item import Item

class Main:
    def __init__(self):

        filename = "inventory.csv"
        inventory_file = FileHandler(filename)
        rows = inventory_file.read()
        print("#### inventory ####")
        inventory: list[Item] = []
        for row in rows:
            _item = Item.deserialize(row)
            _item.displayPrice()
            inventory.append(_item)
        print("#### inventory ####")
        feed = input(f"Change item value (enter 1 - {len(inventory)}): ")
        try:
            index = int(feed) - 1
            feed = input (f"Set new value for {inventory[index].name}: ")
            inventory[index].setValue(float(feed))
        except Exception:
            print("Oops, something went wrong!")
        
        print("Serializing items into rows.")
        print("#### rows ####")
        for _item in inventory:
            row = _item.serialize()
            print(row)
        print("#### rows ####")

if __name__ == "__main__":
    main = Main()