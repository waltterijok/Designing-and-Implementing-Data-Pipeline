'''class Vehicle {
    _engineOn = False
    _turnEngineOn() {
        this.engineOn = true;
    }
    _getEngineStatus() {
        return this.engineOn
    }
}

class Car(Vehicle): {
    isRunning() {
        console.log(this.getEngineStatus());
    }
}

const car1 = new Car():
car1.isRunning():'''

class Vehicle:
    _engineOn = False
    def turnEngineOn(self):
        self._engineOn = True
    
    def getEngineStatus(self):
        return self._engineOn

class Car(Vehicle):
    def isRunning(self):
        print(f"Engine status: ", self.getEngineStatus());

car1 = Car();
car1.isRunning();
car1.turnEngineOn();
print("Turning on the engine...")
car1.isRunning();