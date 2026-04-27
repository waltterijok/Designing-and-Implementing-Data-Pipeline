from devices import *

def pickDevice(choice):
    if choice == 1:
        return SmartLight()
    elif choice == 2:
        return SmartThermostat()
    elif choice == 3:
        return SmartLock()
    else:
        print("Invalid choice, please choose a device to add!")
        return None




def operateDevice(device1, device2):
    print("Checking the devices...")
    print(f"Device {device1.getDeviceName()} is currently {device1.getState()}")
    device1.operate()
    print(f"Device {device2.getDeviceName()} is currently {device2.getState()}")
    device2.operate()



def main():
    print("Welcome to 'Generic Smart Home Devices' control panel!")
    print("--- Control your smart home devices ---")

    devices = []
    while True:
        print("1 - Add smart device - ")
        print("2 - Operate your devices - ")
        print("0 - Exit - ")

        try:
            choice = int(input("Choose your action: "))

            if choice == 0:
                print("Thank you for using 'Generic Smart Home Devices' control panel!")
                print("Exiting program...")
                break

            elif choice == 1:
                print("Choose a device to add:")
                print("1 - Smart Light - ")
                print("2 - Smart Thermostat - ")
                print("3 - Smart Lock - ")

                device_choice1 = int(input("First device: "))
                devices.append(pickDevice(device_choice1))
                device_choice2 = int(input("Second device: "))
                devices.append(pickDevice(device_choice2))

            elif choice == 2:
                operateDevice(devices[0], devices[1])

            else:
                print("Please insert a valid input (0 - 2)")

        except ValueError:
            print("Invalid input, please try again!")

main()