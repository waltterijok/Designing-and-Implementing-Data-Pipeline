from dataclasses import dataclass   # comes from the standard library module dataclasses. Has to be imported.s

@dataclass
class Item:
    SEPARATOR = ','
    name: str
    value: float
    category: str
    weight: float

    @staticmethod
    def deserialze(row:str) -> 'Item':
        columns = row.split(Item.SEPARATOR)         # comma separated values
        item = Item(
            columns[0],     # Name
            columns[1],     # Value
            columns[2],     # category
            columns[3],     # Weight
        )
        return item
    
    def displayPrice(self):
        print(f"{self.name} costs {self.value} €.")

    def displayCategory(self):
        print(f"{self.name} is {self.category}.")

    def displayWeight(self):
        print(f"{self.name} weighs {self.weight} kg.")