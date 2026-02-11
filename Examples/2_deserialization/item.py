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
    
    def serialize(self) -> str:
        columns : list[str] = []
        columns.append(self.name)
        columns.append(str(self.value))
        columns.append(self.category)
        columns.append(str(self.weight))
        row = self.SEPARATOR.join(columns)
        return row
    
    def setValue(self, new_value: float) -> None:
        if new_value < 0:
            print("Value cant be negative")
        else:
            self.value = new_value
        return None

    def displayPrice(self):
        print(f"{self.name} costs {self.value} €.")

    def displayCategory(self):
        print(f"{self.name} is {self.category}.")

    def displayWeight(self):
        print(f"{self.name} weighs {self.weight} kg.")