class SodaBottle:
    brand: str
    capopen: bool

    def __init__(self, brand) -> None:
        self.brand = brand
        self.capopen = False

    def openBottle(self) -> None:
        if not self.capopen:
            print("Sihhh...")
            self.capopen = True
    
    def drink(self) -> None:
        if not self.capopen:
            print("Cant drink from a closed bottle...")
        else:
            print(f"Mmm, tastes like {self.brand}")