from abc import abstractmethod, ABC

class SmartDevice(ABC):
    def __init__(self, deviceName, status):
        self.deviceName = deviceName
        self.status = status

    def getDeviceName(self):
        return self.deviceName

    def getStatus(self):
        print(self.status)

    @abstractmethod
    def operate(self):
        pass

    @abstractmethod
    def getState(self):
        pass

class SmartLight(SmartDevice):
    def __init__(self):
        super().__init__("Light1", "functional")
        self._illumination = False

    def operate(self):
        if self.isOn():
            self.turnOff()
        else:
            self.turnOn()

    def isOn(self):
        return self._illumination

    def turnOn(self):
        if not self._illumination:
            print("turning the light on")
        self._illumination = True

    def turnOff(self):
        if self._illumination:
            print("turning off the light")
        self._illumination = False

    def getState(self):
        if self._illumination:
            return "On"
        else:
            return "Off"        

class SmartThermostat(SmartDevice):
    def __init__(self):
        super().__init__("Thermostat1", "functional")
        self._cooling = False

    def operate(self):
        if self.isOn():
            self.turnOff()
        else:
            self.turnOn()

    def isOn(self):
        return self._cooling
    
    def turnOn(self):
        if not self._cooling:
            print("Heating up")
        self._cooling = True

    def turnOff(self):
        if self._cooling:
            print("Cooling down")
        self._cooling = False

    def getState(self):
        if self._cooling:
            return "On"
        else:
            return "Off"

class SmartLock(SmartDevice):
    def __init__(self):
        super().__init__("Lock1", "functional")
        self._lock = False

    def operate(self):
        if self.isLocked():
            self.unlocked()
        else:
            self.locked()

    def isLocked(self):
        return self._lock
    
    def locked(self):
        if not self._lock:
            print("Locking up")
        self._lock = True
    
    def unlocked(self):
        if self._lock:
            print("Unlocking")
        self._lock = False

    def getState(self):
        if self._lock:
            return "Locked"
        else:
            return "Unlocked"

'''SmartLight().getDeviceName()
SmartLight().getStatus()
SmartLock1().getDeviceName()
SmartLock1().getStatus()
SmartLock2().getDeviceName()
SmartLock2().getStatus()'''

'''light = SmartLight()
light.getStatus()
print("light is on:",light.isOn())
light.turnOn()
print("light is on:",light.isOn())
light.turnOff()
print("light is on:",light.isOn())'''

''''thermostat = SmartThermostat()
thermostat.getStatus()
print("Thermostat on:", thermostat.isOn())
thermostat.turnOn()
print("Thermostat on:", thermostat.isOn())'''